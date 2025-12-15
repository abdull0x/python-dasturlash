# faylga ma'lumot yozish va o'qish mashqi
# funksiyalar yordamida

def get_name():
    name = input("Ismingizni kiriting:").replace(" ", "")
    return name


def get_fav_fruits():
    fruits = []
    print("Yoqtirgan meva nomini kiriting(chiqish uchun q yoki quit)")
    while True:
        fruit = input(">>>")
        if fruit == "q" or fruit == "quit":
            break

        fruits.append(fruit)
    return fruits


def create_file_with_name(name: str):
    f = open(name + ".txt", "w")
    f.close()


def fill_file_with_data(fruits: list, file_name: str):
    with open(file_name + ".txt", "a") as file:
        for fruit in fruits:
            file.write(str(fruit) + "\n")
    print("Ma'lumotlar yozildi!")


def read_data(file_name: str):
    import os
    is_exist = os.path.exists(file_name + ".txt")
    if not is_exist:
        return False
    with open(file_name + ".txt", "r") as file:
        data = file.read()
        return data


def main():
    name = get_name()
    fruits = get_fav_fruits()
    create_file_with_name(name)
    fill_file_with_data(fruits, name)
    print("Faylni o'qishni xoxlaysizmi?")
    yes_or_no = input("(yes/no)>>>")
    if yes_or_no.lower() == "yes":
        data = read_data(name)
        if not data:
            print("Bunday fayl topilmadi")
        else:
            print(data)
    print("Dastur tugadi")


main()
