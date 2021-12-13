def factorial(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * factorial(number - 1)


# driver code
print("Please enter any number: ")
number = int(input())
print("The factorial is: ", factorial(number))

