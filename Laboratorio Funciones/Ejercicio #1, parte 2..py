
c= 0
def a_power_b():
    prod = 1

    a = int(input("Digite el numero que desea elevar: "))
    b = int(input("Digite el numero B: "))


    for i in range (c,b):
        prod = (prod * a)

        print("el numero",a,"al ser elevado a la", b,"sera", prod)

    return prod


a_power_b()