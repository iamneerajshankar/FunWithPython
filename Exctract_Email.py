"""
A python program to extract all the email from a given paragraph or text file

@author: Neeraj Shankar - codewithneeraj@outlook.com
"""
import re as my_regex
from unittest import result

class Extraction:

    
    """**************Returns a list emails from a given string*********************************"""
    @staticmethod
    def extract_email_from_string(input_string):

        p = my_regex.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")
        result = p.findall(input_string)
        print("*****************************************************************", end="\n")
        print("The extracted emails are listed below: ", end="\n")
        for email in result:
            
            print(email)
    
    """**************Read from text file and returns list emails present************************"""
    @staticmethod
    def extract_email_from_textfile():

        try:
            my_file = open("/home/nshankar/Documents/sample.txt", 'r')
            input_string = my_file.read() #reads the file content and store in input string
            
            #regex pattern to identify an email address
            p = my_regex.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+")

            result = p.findall(input_string) # returns a list of matching results
            print("\n*****************************************************************", end="\n")
            print("The extracted emails are listed below: ", end="\n")
            for email in result:
                print(email)
                
        except FileNotFoundError:
            print("File not found. Please check if the file exists.", end="\n")


       
#driver code
if __name__ == "__main__":

    input_string= "This is an email from neerajshankar@outlook.com. This is going to read by codewithneeraj@outlook.com"

    Extraction.extract_email_from_string(input_string)
    Extraction.extract_email_from_textfile()

