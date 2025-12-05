# Pythonda fayllarni import va export qilish
# Import qilish uchun 'import' kalit so'zidan foydalanamiz

# Import qilish degani boshqa fayldagi kodni joriy faylga kiritishdir
# Bu kodni qayta ishlatish va modullar yaratish imkonini beradi

# Modul - bu Python kodini o'z ichiga olgan fayl bo'lib, undagi funksiyalar,
# classlar va o'zgaruvchilarni boshqa fayllarda ishlatish mumkin
# yana import qilish mumkin bo'lgan fayllar to'plami ham modul deb ataladi
# Masalan, math moduli matematik funksiyalarni o'z ichiga oladi

import math
print("Pi soni:", math.pi)
print("Kvadrat ildiz 16:", math.sqrt(16))
# Yuqoridagi misolda math modulidan pi soni va kvadrat ildiz funksiyasilarini ishlatdik
# Lekin bunda math modulidagi barcha funksiyalar va o'zgaruvchilar import qilinadi


# Moduldan faqat kerakli funksiyalarni yoki o'zgaruvchilarni import qilish mumkin
from math import factorial, pow
print("5 ning faktoriali:", factorial(5))
print("2 ning 3-darajasi:", pow(2, 3))
# Yuqoridagi misolda math modulidan faqat factorial va pow funksiyalarini import qildik

# Agar moduldagi barcha funksiyalar va o'zgaruvchilarni import qilish kerak bo'lsa,
# quyidagi sintaksisdan foydalanish mumkin
from math import *
# Lekin bunday qilish tavsiya etilmaydi, chunki nomlar to'qnashuvi yuzaga kelishi mumkin
# Masalan, agar boshqa modulda ham factorial nomli funksiya bo'lsa, u holda qaysi biri ishlatilishini aniqlash qiyin bo'ladi

# Eng yaxshi amaliyot - kerakli funksiyalar va o'zgaruvchilarni aniq ko'rsatib import qilishdir
# Faylni modul sifatida yaratish
# Har qanday Python fayli modul bo'lib xizmat qilishi mumkin
# Masalan. import_me.py faylidagi funksiyalar va o'zgaruvchilarni shu faylda import qilib ishlatish mumkin

from import_me import salom_ber, kvadrat, age, factorial
salom_ber("Vali")
print("4 ning kvadrati:", kvadrat(4))
print("Yosh:", age)
print("6 ning faktoriali:", factorial(6))

# Yuqoridagi misolda import_me.py faylidan salom_ber, kvadrat funksiyalari va age o'zgaruvchisini import qildik
# Shuningdek, import_me.py faylidan factorial funksiyasini ham import qildik va ishlatdik
# Bu orqali kodni qayta ishlatish va modullar yaratish imkonini oldik
# Fayllarni import va export qilish dastur tuzilishini yaxshilaydi va kodni tartibga soladi

# Fayllarni import va export qilish orqali katta loyihalarda kodni boshqarish osonlashadi
# Fayllarni import va export qilish orqali kodni modullarga bo'lish mumkin
# Bu esa kodni qayta ishlatish va saqlashni osonlashtiradi

# Yana import qilishda as kalitidan foydalanish mumkin

from import_me import salom_ber as greet, kvadrat as square
greet("Sardor")
print("5 ning kvadrati:", square(5))


# Yuqoridagi misolda import_me.py faylidagi salom_ber funksiyasini greet nomi bilan,
# kvadrat funksiyasini esa square nomi bilan import qildik
# Bu nomlar bilan funksiyalarni chaqirish mumkin
# Bu usul nomlar to'qnashuvini oldini olish uchun foydalidir