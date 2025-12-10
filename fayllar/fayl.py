with open("matn .txt", "w") as fayl:
    while True:
        matn = input("Ismingizni kiriting: ")
        if matn == "q" or matn == "quit":
            break
        fayl.write(matn.capitalize() + "\n")


print("Dastur tugadi.endi matn.txt faylga o'ting!")
