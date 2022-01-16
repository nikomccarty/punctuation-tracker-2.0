import functions

"""
1) Set up lists of punctuation marks to include. 
2) Write functions that:
    Given string, removes character if it is not in the punctuation list. 
    For each space character, increment a space counter. 
    When a period is reached, store the space counter to a new array, and reset space counter to 0. 
    Increment dictionary frequency tables for each punctuation point. 
3) Build text-wrap function, auto-format at some pre-defined width.
3) Generate a bar chart using matplotlib, to start... 
"""

punctuation_marks = [',', '.', '—', '-', ':', ';', '(', ')', "'", '[', ']', '{', '}', '...']
sentence_ends = ['.', '!', '?']

test_string = "The gobbledy gook, I dare say, is abhorrent—but isn't that the price to pay, my love?"




print(strip_string(test_string))


"""
Text wrap function.
"""
# string = 'ABCDEFGHIJKLMNOPQRSTDSDJNKSAHUIDWDASHSKAJKDWDE'
# max_width = 4

# def wrap(string, max_width):
#     list_string = list(string)
#     new_list = []
#     for i in range(len(list_string)):
#         if i % max_width == 0 and i != 0:
#             new_list.append('\n')
#         new_list.append(list_string[i])
        
#     final_string = ''.join(new_list)
#     return final_string

# print(wrap(string, max_width))