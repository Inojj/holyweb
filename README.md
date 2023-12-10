# Подготовка к запуску

## Poetry
### Установка poetry

Выполнить установку согласно ([документации](https://python-poetry.org/docs/#installation))
# Установка зависимостей
`cd holyweb`

`poetry install`

## Установить playwright
`playwright install`

# Запуск тестов
`poetry run pytest --alluredir allure-results --reruns 1 tests`

# pre-commit

## Запуск линтеров
`poetry run pre-commit run --all-files`

### Нет совместимости с python 3.12. https://github.com/csachs/pyproject-flake8/issues/30
