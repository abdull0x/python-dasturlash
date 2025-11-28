
def calculator():
    son1 = float(input("Son kiriting: "))
    son2 = float(input("ikkinchi son kiriting: "))
    amal = input("+" "-" "*" "/")
    natija = 0
    if amal == "+":
        natija = son1 + son2
    elif amal == "-":
        natija = abs(son1 - son2)
    elif amal == "*":
        natija = son1 * son2
    elif amal == "/":
        if son2 != 0:
            natija = son1 / son2
        else:
            natija = son2 / son1
    
    print(natija)

calculator()