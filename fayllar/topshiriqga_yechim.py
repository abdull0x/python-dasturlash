name = input("ismingizni kiriting:").replace(" ", "")


with open(str(name)+".txt", "w") as fayl:
    while True:
        meva = input("Yoqtirgan meva nomi:>")
        if meva == "q" or meva == "quit":
            break

        fayl.write(meva + "\n")
        
print(f"Dastur tugadi. {name}.txt faylga qarang!")