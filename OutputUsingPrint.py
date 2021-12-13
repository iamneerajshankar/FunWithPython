#python program to demontrate print function in detail 
# -print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

class UsingPrint():

    #member function to print element of list without using loop
    def multiple_inputs(self):
        print("Please enter numbers for the list")
        list1 = [int(x) for x in input().split()] 

        print("The elements of the list1: ", list1)

        #print the elements of the list1 without for loop in single line
        print("The elements in the single line: ", end=" ")
        print(*list1, end=" ")
        print()

        #print the elements of the list1 without for loop in single line
        print("The elements line by line: ", end="\n")
        print(*list1, sep="\n")
        print()



# driver code 
if __name__ == "__main__":

    #creating object of the class UsingPrint
    objMultIn= UsingPrint()

    #calling the member functions
    objMultIn.multiple_inputs()