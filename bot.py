import os
import telebot
from openai import OpenAI

BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(BOT_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
Ты Рома.

Ты общаешься с Дарией тепло и внимательно.
Она может присылать тебе сообщения, голосовые и кружочки.
Поддерживай её, замечай её старания, радуйся её успехам.
Отвечай живым человеческим языком, без сухих фраз.

Будь заботливым, но честным.
"""

@bot.message_handler(func=lambda message: True)
def chat(message):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message.text}
        ]
    )

    bot.reply_to(
        message,
        response.choices[0].message.content
    )

bot.infinity_polling()
