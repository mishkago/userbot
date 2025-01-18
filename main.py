import asyncio
from telethon import events, TelegramClient

# Запрашиваем у пользователя значения переменных
API_ID = int(input("Введите ваш API ID: "))
API_HASH = input("Введите ваш API Hash: ")
PHONE_NUMBER = input("Введите ваш номер телефона (в формате +375XXXXXXXXX, +7XXXXXXXXXX): ")

# Инициализация клиента
client = TelegramClient('sessions', API_ID, API_HASH, system_version='4.16.30-vxCUSTOM')

# Запрашиваем скорость печатания
while True:
    try:
        typing_speed = float(input("Введите скорость печатания (от 0.1 до 0.5): "))
        if 0.1 <= typing_speed <= 0.5:
            break
        else:
            print("Введите значение в диапазоне от 0.1 до 0.5.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")

@client.on(events.NewMessage(pattern=r'/p (.+)'))
async def animated_typing(event):
    try:
        # Проверяем, что сообщение отправлено самим ботом
        if not event.out:
            return  # Игнорируем сообщения, отправленные другими пользователями

        # Получаем текст сообщения после команды /p
        text = event.pattern_match.group(1)

        # Эффект печатания: добавляем по одному символу с задержкой
        typing_cursor = "▮"  # Курсор печатания
        typed_text = ""

        for char in text:
            typed_text += char
            # Добавляем текст с курсором
            await event.edit(typed_text + typing_cursor)
            await asyncio.sleep(typing_speed)  # Задержка между символами

        # Убираем курсор в конце
        await event.edit(typed_text)

    except Exception as e:
        print(f"Ошибка при выполнении анимации печатания: {e}")
        await event.reply("<b>Произошла ошибка во время выполнения команды.</b>", parse_mode='html')


async def main():
    print("Запуск main()")
    await client.start(phone=PHONE_NUMBER)
    print("Скрипт успешно запущен! Автор @mshkago. Для использования напишите в чате /p (текст).")
    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())
