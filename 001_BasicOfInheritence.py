# Python program to demonstrate Inheritence in Python
# (Generally, object is made ancestor of all classes)

class ArrayRotationByOne(object):
    def printArray(self, arr,lengthOfArray):
        #print the array elements 
        print("The elements of the array: ", end=" ")
        for i in range(lengthOfArray):

            print(arr[i], end=" ")
        print()

    def RoatateByOne(self, arr, lengthOfArray):
        #store value of array at index-0 
        temp = arr[0]
        
        #shift the element by one 
        for i in range(lengthOfArray-1):
            arr[i] = arr[i+1]
        
        # store back the element in temp at the end 
        arr[lengthOfArray-1] = temp
    
class RotateByFactor(ArrayRotationByOne):
    def RotateByFactor(self, arr, lengthOfArray, rotateFactor):
        for i in range(rotateFactor):
            ArrayRotationByOne.RoatateByOne(self, arr, lengthOfArray)
        
        



#driver code 
myArr = [1,2,3,4,5,6]
n = len(myArr)
d = 2

# creating object of the parent Class
#obj = ArrayRotationByOne()

#create object of the child class 
obj = RotateByFactor()


# calling the member function using the class instance 
obj.printArray(myArr, n)
obj.RotateByFactor(myArr, n, d)
obj.printArray(myArr, n)