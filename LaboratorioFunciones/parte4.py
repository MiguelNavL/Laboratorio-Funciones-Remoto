def almost_perfect_number(number):
    sum = 0

    for n in range(1, number):
        # Si el residuo es cero, es divisor de number
        if number % n == 0:
            sum = sum + n

    diff = abs(number-sum)
    return diff >= 1 and diff <= 3


number = int(input('Write a number: '))
result = almost_perfect_number(number)

if  result == True:
    print("Is a almost perfect number")
else:
    print("Is NOT a almost perfect number")
