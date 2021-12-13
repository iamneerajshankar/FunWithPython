class PythonDictonary:
    
    def creatingDictonary(self):
        
        # creating dictionary with iteger keys 
        Int_Dict = {'1': "Neeraj", '2': "Shubham", '3': "Vaibhav", '4': "Chetan"}
        
        #printing the distionary with value and pair
        print("The and keys and corresponding value of the given dict: ")
        print(Int_Dict)
        
        #dictionary with mixed keys. 
        nested_dict = {'Neeraj' :{'first_name': "Neeraj", 'last_name':"Shankar", 'Roll_No': "001",}, 
        'Shubham':{'first_name': "Shubham", 'last_name':"Lakhar", 'Roll_No': "002"}, 
        'Vaibhav':{'first_name': "Vaibhav", 'last_name':"Tiwary", 'Roll_No': "003"},
        'Chetan':{'first_name': "Chetan", 'last_name':"Mandloi", 'Roll_No': "004"},}
             
        print(nested_dict)
        
    # function member to add and update element in dictionary
    def AddingElement(self):
        
        #creating empty dictionary
        empty_dict = {}
        
        #print the empty_dict
        print("\nThe intial empty dictionary:", empty_dict)
        
        #adding element one by one
        empty_dict[0] = "Neeraj"
        empty_dict[1] = "Shankar"
        empty_dict[2] = "002"
        
        #print dictionary after adding three values 
        print("The dictionary after adding three values: ", empty_dict)
        
     
        # Adding set of values to a single Key
        empty_dict['values_set'] = 2, 3, 4
        #print the dictionary after adding values_set
        print("The updated dictionary after adding values_set: ", empty_dict)
        
        
        #updating the existing key value
        empty_dict[1] = "Ranjan"
        
        #print the dictionary after updating the value at index 1
        print("The updated dictionary: ", empty_dict)
        
        # Adding Nested Key value to Dictionary
        empty_dict[4] = {1: 'World War', 'year': '1938'}
        #print the dictionary after Adding nested dictionary
        print("The updated dictionary: ", empty_dict)
        
    #accessing the elements of a dictionary
    def AccessingElement(self):
        #creating empty dictionary
        empty_dict = {}
        
        #adding element one by one
        empty_dict[0] = "Neeraj"
        empty_dict[1] = "Shankar"
        empty_dict[2] = "002"
        
        # accessing element using the Key
        print("Accessing the element using key: ")
        print(empty_dict[0])
        
        #accessing element using the get function
        print("Accessing element using get function: ")
        print(empty_dict.get(1))
        
        
        #dictionary with mixed keys. 
        nested_dict = {'Neeraj' :{'first_name': "Neeraj", 'last_name':"Shankar", 'Roll_No': "001",}, 
        'Shubham':{'first_name': "Shubham", 'last_name':"Lakhar", 'Roll_No': "002"}, 
        'Vaibhav':{'first_name': "Vaibhav", 'last_name':"Tiwary", 'Roll_No': "003"},
        'Chetan':{'first_name': "Chetan", 'last_name':"Mandloi", 'Roll_No': "004"},}
             
        #accessing elemts of nested dictionary
        print("The element of nested dictionary: ")
        print(nested_dict['Neeraj']['last_name'])
        
#dirver code 

#creating object of the PythonDictonary class
instDict = PythonDictonary()

# calling the member function of PythonDictonary using class instance 
instDict.AccessingElement()