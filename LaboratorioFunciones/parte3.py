def is_prime(number):
    if number < 1:
        return 0

    if number == 2:
        return 1

    for n in range(2, number):
        if number % n == 0:
            return 0

    return 1

# Inicio del programa
counter = 0
while True:
    try:
        inputNumber = int(input("Digit a number: "))

        if inputNumber == 0:
            break

        result = is_prime(inputNumber)
        counter = counter + 1
    except:
        result = -1

    print "Result: ", result


print "Finish Execution"

print "Counter: ", counter
if is_prime(counter):
    print("Is prime")
else:
    print("Is NOT prime")
