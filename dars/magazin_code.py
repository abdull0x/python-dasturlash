magazin = {
    "mahsulotlar": [
        {"nomi": "Olma", "kategoriya": "mevalar", "narxi": 15000, "sotuvdami": True},
        {"nomi": "Banan", "kategoriya": "mevalar", "narxi": 20000, "sotuvdami": True},
        {"nomi": "Sabzi", "kategoriya": "sabzavotlar", "narxi": 10000, "sotuvdami": True},
    ],
    "xodimlar": [
        {"ismi": "Abdulloh", "lavozim": "direktor", "maosh": 0},
        {"ismi": "Ubaydulloh", "lavozim": "sotuvchi", "maosh": 1000000},
    ]
}


print("""
    Assalomu alaykum! Xush kelibsiz
    Oshxona boshqaruv tizimi
    Amallar:
    1) Mahsulotlarni ko'rish.
    2) Mahsulot qo'shish.
    3) Mahsulot sotuvdan olib tashlash/qo'yish.
    4) Xodimlarni ko'rish.
    5) Xodimlarni o'chirish.
    6) bosh menyuga qaytish.

""")

while True:
    print("Amalni tanlang:>")
    amal = input()

    if amal == "1":
        for mahsulot in magazin["mahsulotlar"]:
            if mahsulot["sotuvdami"]:
                sotuvdami = "Sotuvda"
            else:
                sotuvdami = "Sotuvda emas"
            print(f"{magazin["mahsulotlar"].index(mahsulot) + 1}) {mahsulot["nomi"]} - {mahsulot["narxi"]} - {sotuvdami}")
    elif amal == "2":
        for mahsulot in magazin["mahsulotlar"]:
            if mahsulot["sotuvdami"]:
                sotuvdami = "Sotuvda"
            else:
                sotuvdami = "Sotuvda emas"
            print(f"{magazin['mahsulotlar'].index(mahsulot) + 1})  {mahsulot["nomi"]} - {sotuvdami}")
    elif amal == "3":
        for mahsulot in magazin["mahsulotlar"]:
            print(f"Bizda bor hozir: {mahsulot["nomi"]}  bor.")
            print("Yana nimalar qo'shmoqchisiz?")
    elif amal == "4":
          for hodimlar in magazin["xodimlar"]:
            print(f"{magazin['xodimlar'].index(hodimlar) + 1} {hodimlar["ismi"]}")
    elif amal == "5":
        for hodimlar in magazin["xodimlar"]:
            print(f"{magazin['xodimlar'].index(hodimlar) + 1} {hodimlar["ismi"]}") 
        print("Kimni o'chirmoqchisiz?")
    elif amal == "6":
        print("Bosh menyuga qaytildi")
        break