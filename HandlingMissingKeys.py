class HandlingDictionary:
    def missing_key_handling(self, missing_key):
        
        #Using get get(key, default_value) function
        print(missing_key.get('India', 'Not found'))
        print(missing_key.get('Japan', 'Not found'))
        
        #using the setdefault(key, default_value) functions- a new key is created with the def_value 
        #associated to the key passed in arguments.
        missing_key.setdefault('India', 'Not found')
        print(missing_key['India'])
        missing_key.setdefault('America', 'Not found')
        print(missing_key['America'])
    
    
# driver code 
dict = {}

country_code = {'India' : '0091', 'Australia' : '0025', 'Nepal' : '00977'}

#creating object of the class 

instHandle = HandlingDictionary()
instHandle.missing_key_handling(country_code)