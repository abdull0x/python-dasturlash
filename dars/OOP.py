# print("=" * 30)
# print("Omborxona boshqaruv tizimi")
# print("=" * 30)


# class Category:
#     def __init__(self, name):
#         self.name = name

#     def write(self):
#         with open("category.txt", "r") as file:
#             file.write(f"{self.name}\n")
#         print("Kategorya qo'shildi")


# def get_categories():
#     with open("categories.txt", "r") as file:
#         data = file.read()
#         return data


# categories = get_categories().split("\n")
# categories.pop()


# class Product:
#     def __init__(
#         self, name: str, category: str, cost: int, unit: str, percent=20, stock=1
#     ):
#         self.name = name
#         self.category = category
#         self.cost = cost
#         self.percent = percent
#         self.stock = stock
#         self.unit = unit
#         self.price = (cost // 100) * 20 + self.cost
        
#     def write(self):
#         with open("products.txt", "a") as file:
#             file.write(f"{self.name} | {self.category} | {self.cost} | {self.unit} | {self.percent} | {self.stock} | {self.price}\n")
#         print("Mahsulot qo'shildi!!!")
        
# product1 = Product("Shaftoli", "meva", 15000, "kg", 20, 150)

# def get_products():
#     with open("products.txt", "r") as file:
#         data = file.read()
#         return data
# products = get_products().split("\n")
# products.pop()

# products = [
#     ["olma", "meva", 12000, "kg", 20, 100, 14400]
#     ["shaftoli", "meva", 15000, "kg", 20, 150, 18000]
#     ["sabzi", "sabzavot", 8000, "kg", 20, 200, 9600]
# ]




import telebot
from telebot.types import Message
from googletrans import Translator

translator = Translator()

languages = ["uz", "en", "ru", "ko", "ka"]

def translate_to(text: str, lang="uz"):
    return translator.translate(text=text, dest=lang).text


bot = telebot.TeleBot(token="tg token")

@bot.message_handler(commands=["start"])
def start_handler(message: Message):
    bot.send_message(message.chat.id, f"Assalomu alaykum {message.from_user.full_name}!\n"
                                      "Men tarjimon botman. Istalgan matnni rus tiliga tarjima qilaman.\n"
                                      "Yuborilgan matnni shunchaki qaysi tilga tarjima qilish kerakligini yuboring!\n")

@bot.message_handler()
def get_all_texts(message: Message):
    translated_text = translate_to(message.text, lang="en")
    bot.send_message(message.chat.id, translated_text)


print("bot ishga tushdi")
bot.infinity_polling()
