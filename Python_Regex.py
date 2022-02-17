from ast import Expression
from nis import match

import re


class ExploringRegex:

    @staticmethod
    # search() method is used to find the first occurrence of strings
    def search_method(input_string):

        # search() method is used to find the first occurrence of strings
        print("Please enter any character or string to search", end="\n")
        item = input()

        index_of = re.search(item, input_string)
        print("The information of first occurence of {} is as follows:{} ".format(
            item, index_of), end="\n")

    # match() attempts to match a pattern to the whole string. The re.match function returns a
    # match object on success, None on failure.
    @staticmethod
    def match_method(input_string):

        # ******************************Set operations in combination with match()********************
        print("\n*************************************************************************************")
        p = re.compile('[a-z]+', re.IGNORECASE)
        white_space = " "
        result = p.match(white_space)
        print("The match result of white space {}".format(result))
        word = input_string
        result = p.match(word)
        match_group = result.group()
        print("The match for {} in the given pattern: {}".format(word, result))
        print("The match group of {} is: {}".format(word, match_group))
        start_index = result.start()
        print("The starting index of {} is: {}".format(word, start_index))
        end_index = result.end()
        print("The starting index of {} is: {}".format(word, end_index))
        word_span = result.span()
        print("The total span of the {} is: {}".format(word, word_span))


# driver code
if __name__ == "__main__":

    print("Please enter a string to test:", end='\n')
    input_string = input()

    # calling the static methods of the class ExploringRegex
    # ExploringRegex.search_method(input_string)
    ExploringRegex.match_method(input_string)
