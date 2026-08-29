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

## Формирование уведомления

Текст сообщения пишет не сам `tracker`, а субагент **`diffWriter`**. Разделение
такое: `tracker` обходит страницы, сравнивает прогоны и отбирает значимые
изменения, после чего передаёт готовый diff и правила оформления субагенту, а
тот возвращает короткий текст. Отправляет его снова `tracker` — через `send.py`.

Субагент ничего не сравнивает, не считает и не ходит в сеть: он работает только
с тем, что ему передали. Благодаря этому логика сравнения и формулировки
уведомления правятся независимо друг от друга.

## Что где лежит

| Путь | Назначение |
|---|---|
| `KNOWLEDGE.md` | Правила сравнения двух прогонов — что считать значимым изменением |
| `send.py` | Отправка текста в Telegram через Bot API, только стандартная библиотека |
| `.claude/skills/extract-price/` | Извлечение цены, скидки и наличия рассрочки с одной страницы по URL |
| `.claude/skills/tracker/` | Обход списка URL, сравнение прогонов, отправка сводки и сохранение результата |
| `.claude/agents/diffWriter.md` | Субагент, который превращает готовый diff в текст уведомления |
| `.claude/skills/_template/` | Заготовка для нового скила |
| `.claude/skills/README.md` | Соглашения по написанию скилов |
| `.github/workflows/` | Проверка проекта на стороне Hexlet, файл `hexlet-check.yml` не редактировать |

## Где что менять

- Как достаётся цена со страницы — `.claude/skills/extract-price/SKILL.md`.
- Как идёт обход списка и сохранение прогона — `.claude/skills/tracker/SKILL.md`.
- Пороги значимости изменений — `KNOWLEDGE.md`.
- Как формулируется текст уведомления — `.claude/agents/diffWriter.md`.
- Новый скил — скопировать `_template`, см. `.claude/skills/README.md`.
