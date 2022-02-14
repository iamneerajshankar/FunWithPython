"""
****************************************************************************************************
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static method in python.

**Class method vs Static Method**

1. A class method takes cls as the first parameter while a static method needs no specific parameters.
2. A class method can access or modify the class state while a static method can’t access or modify it.
3. In general, static methods know nothing about the class state. They are utility-type methods 
   that take some parameters and work upon those parameters. On the other hand class methods must have 
   class as a parameter.

****************************************************************************************************

"""

class Calculator:

    def __init__(self, first_number, second_number, average):
        self. first_number = first_number
        self.second_number = second_number
        self.average = average

        print("Calling from constructor: ")
        print("The first number from class is {}.".format(first_number))
        print("The second number from class is {}.".format(second_number))
        print("The averge of these two numbers is {}".format(average))

    @classmethod
    def finding_average(cls, first_number, second_number):
        print("*********************************************************************")
        print("Calling from class method: ")
        return cls(first_number, second_number, average)
    

    @staticmethod
    def find_table(first_number):
        print("*********************************************************************")
        print("The first number is {}.".format(first_number))
        print("Priting the table of {} as: ".format(first_number), end=" ")
        for i in range(1,11):
            print(i*first_number, end=" ")
        print()

if __name__ == "__main__":

    first_number = 10
    second_number = 20
    average = (first_number+second_number)/2


    calculator = Calculator(first_number, second_number, average)
    # passing different values to first_number and second in finding_average will change value
    # first_number and second_name in  class constructor. But the value average remains same 
    # as we have not passed average value in finding_average.
    average = Calculator.finding_average(30, 40)

    table = Calculator.find_table(15)