def is_prime(number):
    if number < 1:
        return False

    if number == 2:
        return True

    for n in range(2, number):
        if number % n == 0:
            return False

    return True


# Inicio del programa
input = int(input("Digite un numero: "))
result = is_prime(input)

if result == True:
    print('Es primo')
else:
    print('No es primo')
