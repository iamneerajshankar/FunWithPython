def fibonnaci(number):
    if number in [0, 1]:
        return 1
    else:
        return fibonnaci(number - 1) + fibonnaci(number - 2)


# driver code
print("Please enter the number: ")
number = int(input())
print(fibonnaci(number))
