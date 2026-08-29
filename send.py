#!/usr/bin/env python3
"""Отправка сообщения в Telegram через Bot API.

Только стандартная библиотека (urllib), без внешних зависимостей.

Переменные окружения:
    TELEGRAM_BOT_TOKEN  — токен бота от @BotFather
    TELEGRAM_CHAT_ID    — id чата (или @channelusername)

Запуск:
    python send.py "текст"
"""

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://api.telegram.org/bot{token}/sendMessage"
TIMEOUT = 30


def send_message(token, chat_id, text):
    """Отправляет текст в чат и возвращает объект отправленного сообщения."""
    data = urllib.parse.urlencode({"chat_id": chat_id, "text": text}).encode("utf-8")
    request = urllib.request.Request(
        API_URL.format(token=token),
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(request, timeout=TIMEOUT) as response:
        payload = json.loads(response.read().decode("utf-8"))
    return payload["result"]


def main(argv):
    if len(argv) != 2 or not argv[1].strip():
        print('Использование: python send.py "текст"', file=sys.stderr)
        return 2

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    missing = [
        name
        for name, value in (
            ("TELEGRAM_BOT_TOKEN", token),
            ("TELEGRAM_CHAT_ID", chat_id),
        )
        if not value
    ]
    if missing:
        print(
            "Не заданы переменные окружения: " + ", ".join(missing),
            file=sys.stderr,
        )
        return 2

    try:
        result = send_message(token, chat_id, argv[1])
    except urllib.error.HTTPError as error:
        body = error.read().decode("utf-8", "replace")
        try:
            description = json.loads(body)["description"]
        except (ValueError, KeyError):
            description = body.strip() or error.reason
        print("Telegram API вернул ошибку %s: %s" % (error.code, description), file=sys.stderr)
        return 1
    except urllib.error.URLError as error:
        print("Не удалось связаться с Telegram: %s" % error.reason, file=sys.stderr)
        return 1

    print("Сообщение отправлено, message_id=%s" % result.get("message_id"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
