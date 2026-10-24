import os, telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

@bot.message_handler(commands=["start"])
def start(m):
    bot.reply_to(m, "Hello from FadeHost 🎉")

    @bot.message_handler(func=lambda m: True)
    def echo(m):
        bot.reply_to(m, f"You said: {m.text or ''}")

        bot.infinity_polling(skip_pending=True)