matn = input("Matnni kiriting: ")
siljish = int(input("Siljish miqdorini kiriting: "))

kodlangan_matn = ""
for belgi in matn:
    if belgi.isalpha():
        boshlangich_kod = ord("a") if belgi.islower() else ord("A")
        yangi_belgi = chr(
            (ord(belgi) - boshlangich_kod + siljish) % 26 + boshlangich_kod
        )
        kodlangan_matn += yangi_belgi
    else:
        kodlangan_matn += belgi
print("Kodlangan matn:", kodlangan_matn)
