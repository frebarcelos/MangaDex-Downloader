import os
import re
import streamlit as st

from config_types import MangaConfig
import melhoresVolumes as m
import salvarviaScript as s


def parse_url(url: str):
    parts = url.strip().split('/')
    if len(parts) >= 6 and parts[2].endswith("mangadex.org") and parts[3] == 'title':
        return parts[4], parts[5]
    return None, None


def parse_volumes(volumes_str: str):
    volumes = []
    for v in volumes_str.split(';'):
        v = v.strip()
        if v.isdigit():
            volumes.append(int(v))
    return volumes


st.title("MangaDex Downloader")

manga_url = st.text_input("URL do mangá", placeholder="https://mangadex.org/title/UUID/NOME")
if manga_url:
    uuid, manga_nome = parse_url(manga_url)
else:
    uuid = manga_nome = None

save_dir = st.text_input("Diretório de destino")
linguagem = st.text_input("Idioma (ex: pt-br)")

vol_info = None
if uuid and linguagem and st.button("Mostrar volumes disponíveis"):
    with st.spinner('Buscando volumes...'):
        dados = m.buscar_volumes(uuid, linguagem)
        vol_info = m.selecionar_melhor_idioma_por_volume(dados)
    if vol_info:
        for vol in vol_info:
            volume_num = vol['volume'] if vol['volume'] != '0' else 'Sem Volume'
            st.write(f"Volume {volume_num} - {vol['idioma'].upper()} ("\
                     f"{len(vol['capitulos'])} capítulos, {vol['total_paginas']} páginas)")
            caps = ', '.join(c['chapter'] for c in vol['capitulos'])
            st.write(f"Capítulos: {caps}")
    else:
        st.write("Nenhum volume encontrado")

volumes_str = st.text_input("Volumes para baixar (ex: 1;2;3)")
trocar_capa = st.checkbox("Trocar capa ao final")

if st.button("Iniciar download"):
    if not uuid:
        st.error("URL do mangá inválida.")
    elif not save_dir or not os.path.isdir(save_dir):
        st.error("Diretório de destino inválido.")
    else:
        volumes = parse_volumes(volumes_str)
        if not volumes:
            st.error("Nenhum volume válido informado.")
        else:
            config = MangaConfig(
                manga_id=uuid,
                manga_nome=manga_nome or 'manga',
                save_dir=save_dir,
                volumes=volumes,
                linguagem=linguagem or 'pt-br',
                trocar_capa=trocar_capa,
            )
            with st.spinner('Baixando...'):
                s.main(config)
            st.success('Concluído!')

