# ro'yxatdagi unli harf bilan boshlanadigan so'zlarni yangi ro'yxatga joylashtiring

def unlilar():
    sozlar = ["olma", "anor", "uzum", "nok", "gilos"]
    vowels = "aeuio"
    new_sozlar = []
    for soz in sozlar:
        if soz[0].lower() in vowels:
            new_sozlar.append(sozlar)
        
        print("Natija", new_sozlar)
unlilar()






# berilgan ro'yxatdagi juft sonlarni yangi ro'yxatga joylashtiring


def sun():
    sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    juft_sonlar = []

    for son in sonlar:
        if son % 2 == 0:
            juft_sonlar.append(son)
    print("juft sonlar", juft_sonlar)
sun()



# berilgan matndagi so'zlarni sonini hisoblang. Bunda bir xil so'zlar soni qo'shib hisoblanadi
def soz_soni():
    matn = "salom dunyo salom odamlar dunyo"
    sozlar = matn.split()


