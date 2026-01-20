import telebot

TOKEN = "BU_YERGA_TOKENINGNI_QOY"

bot = telebot.TeleBot(token="token")

savollarga_javob = {
    "salom": "Salom! Qalaysiz?",
    "isming nima": "Mening ismim Savol-Javob Bot",
    "python nima": "Python — mashhur va oson dasturlash tili.",
    "qayerdansan": "Men Python dasturlash tilida yozilganman.",
    "xayr": "Xayr! Yana savol bolsa yozing"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom qalesan!\ntuzumisan!"
    )

@bot.message_handler(func=lambda message: True)
def answer(message):
    user_text = message.text.lower()

    for question in savollarga_javob:
        if question in user_text:
            bot.send_message(message.chat.id, savollarga_javob[question])
            return

    bot.send_message(
        message.chat.id,
        "Kechirasiz, bu savolga javob topa olmadim."
    )

print("Bot ishga tushdi...")
bot.infinity_polling()
