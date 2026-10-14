"""Тесты модулей работы с файлами и логирования."""
import logging

from file_utils import read_text, write_text, read_json, write_json
from log_utils import get_logger


def test_write_and_read_text(tmp_path):
    path = tmp_path / "sub" / "note.txt"
    write_text(str(path), "Привет, мир")
    assert read_text(str(path)) == "Привет, мир"


def test_json_roundtrip(tmp_path):
    path = tmp_path / "data.json"
    write_json(str(path), {"задача": [1, 2, 3]})
    assert read_json(str(path)) == {"задача": [1, 2, 3]}


def test_read_json_missing_file(tmp_path):
    assert read_json(str(tmp_path / "missing.json")) == {}


def test_logger_writes_file(tmp_path):
    log_file = tmp_path / "app.log"
    logger = get_logger("test-file-logger", log_file=str(log_file))
    logger.info("сообщение")
    for handler in logger.handlers:
        handler.flush()
    assert "сообщение" in log_file.read_text(encoding="utf-8")


def test_logger_is_reused():
    assert get_logger("same-logger") is get_logger("same-logger")
    assert get_logger("same-logger").level == logging.INFO
