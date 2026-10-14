"""Утилиты для работы со строками."""
import re


def reverse_string(text: str) -> str:
    """Возвращает строку в обратном порядке."""
    return text[::-1]


def capitalize_words(text: str) -> str:
    """Делает первую букву каждого слова заглавной, не меняя остальные буквы."""
    return " ".join(word[:1].upper() + word[1:] for word in text.split())


def slugify(text: str) -> str:
    """Преобразует строку в идентификатор, пригодный для URL."""
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", text)


def truncate(text: str, length: int, suffix: str = "…") -> str:
    """Обрезает строку до заданной длины, добавляя многоточие."""
    if length <= 0:
        raise ValueError("Длина должна быть положительной")
    return text if len(text) <= length else text[: length - len(suffix)] + suffix


def count_words(text: str) -> int:
    """Возвращает количество слов в строке."""
    return len(text.split())


def is_palindrome(text: str) -> bool:
    """Проверяет, является ли строка палиндромом (без учёта регистра и пробелов)."""
    cleaned = re.sub(r"\W", "", text.lower(), flags=re.UNICODE)
    return cleaned == cleaned[::-1]
