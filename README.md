# Price Tracker

Мониторинг цен на карточках товаров интернет-магазина: обход списка ссылок,
сборка таблицы цен, сравнение с прошлым прогоном и короткая сводка об
изменениях в Telegram. Работает как набор скилов для Claude Code —
отдельного приложения запускать не нужно.

### Hexlet tests and linter status:
[![Actions Status](https://github.com/olegserbat/vibecoding-claudecode-project-388/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/olegserbat/vibecoding-claudecode-project-388/actions)

## Как запустить

Открыть проект в Claude Code и попросить «запусти tracker». Для отправки
сводки нужны переменные окружения `TELEGRAM_BOT_TOKEN` и `TELEGRAM_CHAT_ID`.

История прогонов хранится в отдельном репозитории
[`olegserbat/tracker-data`](https://github.com/olegserbat/tracker-data):
один прогон — один файл `YYYY-MM-DD.json`.

## Что где лежит

| Путь | Назначение |
|---|---|
| `KNOWLEDGE.md` | Правила сравнения двух прогонов — что считать значимым изменением |
| `send.py` | Отправка текста в Telegram через Bot API, только стандартная библиотека |
| `.claude/skills/extract-price/` | Извлечение цены, скидки и наличия рассрочки с одной страницы по URL |
| `.claude/skills/tracker/` | Обход списка URL, сравнение прогонов, отправка сводки и сохранение результата |
| `.claude/skills/_template/` | Заготовка для нового скила |
| `.claude/skills/README.md` | Соглашения по написанию скилов |
| `.github/workflows/` | Проверка проекта на стороне Hexlet, файл `hexlet-check.yml` не редактировать |

## Где что менять

- Как достаётся цена со страницы — `.claude/skills/extract-price/SKILL.md`.
- Как идёт обход списка и сохранение прогона — `.claude/skills/tracker/SKILL.md`.
- Пороги значимости изменений — `KNOWLEDGE.md`.
- Новый скил — скопировать `_template`, см. `.claude/skills/README.md`.
