"""Утилиты для работы с файлами."""
import json
import pathlib


def read_text(path: str, encoding: str = "utf-8") -> str:
    """Читает текстовый файл целиком."""
    return pathlib.Path(path).read_text(encoding=encoding)


def write_text(path: str, content: str, encoding: str = "utf-8") -> None:
    """Записывает текст в файл, создавая каталоги при необходимости."""
    p = pathlib.Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding=encoding)


def read_json(path: str) -> dict:
    """Читает JSON-файл; при отсутствии файла возвращает пустой словарь."""
    p = pathlib.Path(path)
    if not p.exists():
        return {}
    return json.loads(p.read_text(encoding="utf-8"))


def write_json(path: str, data: dict) -> None:
    """Сохраняет словарь в JSON-файл с отступами."""
    write_text(path, json.dumps(data, ensure_ascii=False, indent=2))
