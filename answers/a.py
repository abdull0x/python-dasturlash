
# 1-topshiriq

#foydalanuvchi 1 dan 12 gacha(12 ham) son kiritsin. Shu songa mos oy nomi ekranga chiqsin. 

# oy = int(input("Oy tartib raqamini kiriting: "))

# if oy == 1:
#     print(" Yanvar")
# elif oy == 2:
#     print(" Fevral")
# elif oy == 3:
#     print(" Mart")
# elif oy == 4:
#     print(" Aprel")
# elif oy == 5:
#     print(" May")
# elif oy == 6:
#     print(" Iyun")
# elif oy == 7:
#     print(" Iyul")
# elif oy == 8:
#     print(" Avgust")
# elif oy == 9:
#     print(" Sentabr")
# elif oy == 10:
#     print(" Oktabr")
# elif oy == 11:
#     print(" Noyabr")
# elif oy == 12:
#     print(" Dekabr")
# else:
#     print("Xatolik: 1 dan 12 gacha son kirit qovun!!!")
    
# 2-topshiriq
# Foydalanuvchidan bo'yini (metrda) va vaznini (kg da) so'rang. BMI (Body Mass Index) hisoblang va natijani baholang

# boy = float(input("Boy kirting (m): "))
# vazn = float(input("Vazn kirting (kg): "))

# bmi = vazn / (boy * boy)

# if bmi < 18.5:
#     print("Siz ozg'insiz")
# elif bmi < 25:
#     print("Sizning vazningiz normal")
# elif bmi < 30:
#     print("Siz ortiqcha vaznga egasiz")
# else:
#     print("Siz semizlik darajasidasiz")


# 4-topshiriq
# Studentlar haqida ma'lumot saqlovchi lug'at yarating. Har bir student uchun: ismi, yoshi, yo'nalishi va baholari (3 ta fan) saqlansin.

# Studentlar lug'ati
studentlar = {
    "student1": {
        "ismi": "Ali",
        "yoshi": 20,
        "yonalishi": "Dasturlash",
        "baholari": [5, 4, 5]
    },
    "student2": {
        "ismi": "Vali",
        "yoshi": 22,
        "yonalishi": "Axborot texnologiyalari",
        "baholari": [4, 5, 4]
    },
    "student3": {
        "ismi": "Sara",
        "yoshi": 21,
        "yonalishi": "Kompyuter injiniringi",
        "baholari": [5, 5, 5]
    }
}

# 1. Barcha studentlarni chiqarish
print("Barcha studentlar:")
for s in studentlar.values():
    print(s)

print("\n" + "-"*30)

# 2. Yoshi 20 dan katta bo'lgan studentlar
print("Yoshi 20 dan katta studentlar:")
for s in studentlar.values():
    if s["yoshi"] > 20:
        print(s["ismi"])

print("\n" + "-"*30)

# 3. O'rtacha bahosi eng yuqori bo'lgan student
eng_yuqori = 0
eng_student = ""

for s in studentlar.values():
    ortacha = sum(s["baholari"]) / len(s["baholari"])
    if ortacha > eng_yuqori:
        eng_yuqori = ortacha
        eng_student = s["ismi"]

print("O'rtacha bahosi eng yuqori student:")
print(eng_student, "-", eng_yuqori)
