import  array as myArr

class ArrayProblems:
    
    def ArrayInsertion(self, arr):
        
        #adding element at the speciied location
        arr.insert(0, 2)
        
        #printing the array element after insertion 
        print("The elements of the array after the insertion are: ",end=" ")
        for element in range(len(arr)):
            print(arr[element], end=" ")
        print()
            
    def ArrayDeletion(self, arr):
        # using remove() to remove 1st occurrence of 3
        arr.remove(3)
        
        #using pop() to remove element from certain position 
        arr.pop(0)
        
        #printing the array after deletion of element
        print("The elements of the array after deletion: ",end=" ")
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
            
    def AccessElement(self, arr):
        
        # logic to access the element
        print("The elements of the array can be accessed as: ", end=" ")
        for i in range(len(arr)):
            print("The element at index ", i, "is ", arr[i], end=" ")
        print()
            
    def SlicingArray(self, arr):
        slicedArray = arr[2:]
        print("The elements of the array after sliced from index 2 to end: ", end=" ")
        print(slicedArray)



# driver code 

# creating array with integer type
arr = myArr.array('i', [2,3,4, 5, 6])

#printing the array original array elements
print("The elements of the originl array are: ", end=" ")

# iterating each element of the Array 
for element in range(len(arr)):
    print(arr[element], end=" ")
print()

# crearting class object     
objOperation = ArrayProblems()

# Calling the function member using the class instance
objOperation.ArrayInsertion(arr)
#objOperation.SlicingArray(arr)
#objOperation.ArrayDeletion(arr)
#objOperation.AccessElement(arr)