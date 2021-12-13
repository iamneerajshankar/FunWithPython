# Python program to check  if the given number is a prime number or not


def is_prime(num, i=2):

    # when the user enters 0 or 1 or to for checking 0 and 1
    if num == 0 or num == 1:
        return False

    if num == i:
        return True
    if num % i == 0:
        return False

    return is_prime(num, i+1)


# driver code
print("Please enter any number: ")
num = int(input())
if is_prime(num):
    print("The provided number is prime")

else:
    print("The given number is not prime")
