# 1-topshiriq

# Fayldan matn o'qish va so'zlarni sanash
# Fayldan matn o'qib, undagi so'zlar sonini hisoblaydigan funksiya yozing.
# Fayl mavjud bo'lmasa, xatolik haqida xabar bering.
# Fayl nomi sifatida "matn.txt" dan foydalaning.
# Masalan, fayl tarkibi:
# Salom dunyo!
# Bugun dasturlashni o'rganamiz.
# Natija: 6 so'z

# def sanash(turi: str): # qila olmadim



# 2-topshiriq

# Foydalanuvchi ma'lumotlarini faylga yozish
# Foydalanuvchidan ism va yoshini so'rab,
# bu ma'lumotlarni "foydalanuvchilar.txt" fayliga yozadigan funksiya yozing.
# Har bir foydalanuvchi ma'lumotlari yangi qatorda saqlansin.
# Masalan, foydalanuvchi kiritadi:
# Ism: Ali
# Yosh: 25
# Fayl tarkibi:
# Ali, 25

def foydalanuvchi_malumotlarini_yozish():
    name = input("Ismingizni kiriting: ").replace(" ", "")
    age = input("Yoshingizni kiriting: ").replace(" ", "")
    with open("foydalanuvchilar.txt", "a") as file:
        file.write(f"{name}, {age}\n")
    print("Ma'lumotlar faylga yozildi.")
foydalanuvchi_malumotlarini_yozish()



# 3-topshiriq

# Foydalanuvchidan ikkita son kiritishni so'rang va ularni bo'lishni amalga oshiring.
# Agar foydalanuvchi nolga bo'lishga harakat qilsa,
# xatolik haqida xabar bering va foydalanuvchidan qayta son kiritishni so'rang
# aks holda natijani chop eting.

def bolish():  
    while True:
        try:
            son1 = float(input("Birinchi sonni kiriting: "))
            son2 = float(input("Ikkinchi sonni kiriting: "))
            natija = son1 / son2
        except ZeroDivisionError: # Exeption yozza ham bo'ladi!
            print("Nolga bo'lish mumkin emas. Iltimos, boshqa son kiriting.")
        except ValueError:
            print("Iltimos, son kiriting.")
        else:
            print(f"Natija: {natija}")
            break
bolish()



# 4-topshiriq

# "raqamlar.txt" faylidan raqamlarni o'qib,
# ularning yig'indisini hisoblaydigan funksiya yozing.
# Har bir raqam yangi qatorda joylashgan bo'lsin.
# Fayl mavjud bo'lmasa, xatolik haqida xabar bering.
# Masalan, fayl tarkibi:
# 10
# 20
# 30
# Natija: 60


# def raqamlar_yigindisi(): # qila olmadim