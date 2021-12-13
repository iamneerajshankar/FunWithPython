#python program to demonstarte taking multiple inputs at one time
\


class TakingMultipleInput(object):

    #function to take two inputs using the split function
    def ThreeInput(self):
        print("Please enter the two numbers: ")
        num1, num2 = input().split()

        print("The number of boys: ", num1)
        print("The number of girls", num2)


    def MultipleInput(self):
        #using the list function to store any desirable number of inputs
        print("Please enter any number of inputs separated by space: ")
        num = list(map(int, input().split()))

        print("The generated output is: ", num)

    # Function member to two take two inputs using the List Comprehension 
    def UsingListComprehension(self):

        #use of list comprehension
        print("Please enter the two values: ")
        num1, num2 = [int(x) for x in input().split()]

        # print the inout taken
        print("The number of chats taken: ",num1)
        print("The number of Emails taken: ", num2)
#driver code 
if __name__ == "__main__":
    objMultIn = TakingMultipleInput()

    #calling the member functions of the class TakingMultipleInput
    #objMultIn.ThreeInput()
    #objMultIn.MultipleInput()
    objMultIn.UsingListComprehension()
