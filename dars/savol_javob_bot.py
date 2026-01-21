import telebot
# from telebot.types import Massage
# from googletrans import Translator


TOKEN = "BU_YERGA_TOKENINGNI_QOY"

bot = telebot.TeleBot(token="token")

savollarga_javob = {
    "salom": "Salom! Qalesan nima gaplar",
    "ismin nima": "Mening ismim Savol-Javob Bot",
    "python nima": "Python — oson dasturlash tili.",
    "qattansan": "Men Python dasturlash tilida yozilganman.",
    "xayr": "Xayr"
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Salom qalesan!\ntuzumisan!"
    )