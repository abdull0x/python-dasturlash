from modul1 import matn,faktorial
from utils import add, subtract,divide,power,multiply



son1 = int(input("1-sonni kiriting:>"))
son2 = int(input("2-sonni kiriting:>"))

matn = input("Matn kiriting:>")


yigindi = add(son1, son2)
print("Yigindi=", yigindi)


ayirma = subtract(son1,son2)
print("Ayirma=", ayirma)


kopaytirish = multiply(son1,son2)
print("kopaytirish=", kopaytirish)

bolish = divide(son1,son2)
print("bolish=", bolish)

darajaga_kotarish = power(son1,son2)
print("kopaytirish=", darajaga_kotarish)


# =========================================================

matn1 = matn(matn)
print("Katta harflar:", matn1)

faktorial1 = faktorial(son1)
print("Faktorial:", faktorial1)