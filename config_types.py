from dataclasses import dataclass
from typing import List

@dataclass
class MangaConfig:
    manga_id: str
    manga_nome: str
    save_dir: str
    volumes: List[int]
    linguagem: str
    trocar_capa: bool = False  