import os
from pathlib import Path


# Корневая директория проекта
ROOT_DIR = os.path.dirname(__file__)

# Директория для файлов с данными
DATA_DIR = os.path.join(ROOT_DIR, "data", "vacansies.json")

ROOT_PATH = Path(__file__).parent
