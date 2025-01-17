import asyncio
import time
import re
import os
from telethon import events, TelegramClient
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.types import InputPeerChannel, User, Chat, Channel
from telethon.utils import get_display_name
from tinydb import TinyDB, Query

# Запрашиваем у пользователя значения переменных
API_ID = input("Введите ваш API ID: ")
API_HASH = input("Введите ваш API Hash: ")
PHONE_NUMBER = input("Введите ваш номер телефона (в формате +375XXXXXXXXX, +7XXXXXXXXXX): ")

# Инициализация клиента
client = TelegramClient('sessions', API_ID, API_HASH, system_version='4.16.30-vxCUSTOM')

@client.on(events.NewMessage(pattern=r'/p (.+)', func=lambda e: True))
async def animated_typing(event):
    try:
        # Получаем текст сообщения после команды /p
        text = event.pattern_match.group(1)

        # Очищаем текст команды (удаляем /p и пробел)
        await event.edit("▮")  # Очищаем текст команды и добавляем курсор печатания

        # Эффект печатания: добавляем по одному символу с задержкой
        typing_cursor = "▮"  # Курсор печатания
        typed_text = ""

        for char in text:
            typed_text += char
            # Добавляем текст с курсором
            await event.edit(typed_text + typing_cursor)
            await asyncio.sleep(0.1)  # Задержка между символами

        # Убираем курсор в конце
        await event.edit(typed_text)

    except Exception as e:
        print(f"Ошибка при выполнении анимации печатания: {e}")
        await event.respond("<b>Произошла ошибка во время выполнения команды.</b>", parse_mode='html')


async def main():
    print("Запуск main()")
    await client.start(phone=PHONE_NUMBER)
    print("Скрипт успешно запущен! Автор @mshkago. Для использования нужно написать любому человеку /p (текст)")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
