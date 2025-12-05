# 1-topshiriq

def faktorial(n):
    """Sonning faktorialini hisoblovchi funksiya"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
# natija = faktorial(5)
# print("Faktorial:", natija)


# 2-topshiriq


def fibonachi(n):
    """Sonning fibonachisini hisoblovchi funksiya"""
    if n == 0 or n == 1:
        return 1
    else:
        return n + fibonachi(n - 1)
# natija = fibonachi(5)
# print("Fibonachi:", natija)



# 3-topshiriq

def matn(n):
    """bitta matn qabul qilib, uni katta harflarga aylantirib qaytaradi."""
    return n.upper()
# natija = matn("")
# print("Natija:", natija)