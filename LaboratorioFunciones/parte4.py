def perfect_number(number):
    sum = 0

    for n in range(1, number):
        if number % n == 0:
            sum = sum + n

    return sum == number


number = int(input('Write a number: '))
result = perfect_number(number)

if  result == True:
    print("Is a perfect number")
else:
    print("Is NOT a perfect number")
