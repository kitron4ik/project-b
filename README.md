# project-b-utils

Библиотека утилит для работы с датами и строками. Используется как зависимость
в проекте **project-a (Task Manager)**.

## Установка

```bash
pip install -e .
```

## Состав

| Модуль | Функции |
|---|---|
| `date_utils` | `get_current_date`, `format_date`, `days_between`, `add_working_days`, `is_weekend`, `start_of_month` |
| `string_utils` | `reverse_string`, `capitalize_words`, `slugify`, `truncate`, `count_words`, `is_palindrome` |
| `file_utils` | `read_text`, `write_text`, `read_json`, `write_json` |
| `log_utils` | `get_logger` |

## Запуск тестов

```bash
pytest tests/
```
