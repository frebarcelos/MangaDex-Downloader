from config_types import MangaConfig 
import salvarviaScript as s
import melhoresVolumes as m
import inputValidator as v

def main():
    uuid, manga_nome = v.obter_url_manga()
    save_dir = v.obter_diretorio_destino()
    linguagem = v.obter_linguagem()

    m.main(uuid, linguagem)
    if not v.confirmar_pergunta("Você quer baixar nesse idioma?"):
        print("Encerrando.")
        return

    volumes = v.obter_volumes()
    trocar_capa = v.confirmar_pergunta("Deseja trocar a capa ao final?")

    config = MangaConfig(
        manga_id=uuid,
        manga_nome=manga_nome,
        save_dir=save_dir,
        volumes=volumes,
        linguagem=linguagem,
        trocar_capa=trocar_capa
    )

    s.main(config)

if __name__ == "__main__":
    main()

        
