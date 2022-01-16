import functions
import matplotlib.pyplot as plt

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

# Must implement a series of checks; while True, try, except, must be string, etc. 

punctuation_marks = [',', '.', '—', '-', ':', ';', '(', ')', "'", '[', ']', '{', '}', '...']
sentence_ends = ['.', '!', '?']

test_string = "The gobbledy gook, I dare say, is abhorrent—but isn't that the price to pay, my love?"

def strip_string(string):
    list_string = list(string)
    punctuations = []
    for i in range(len(list_string)):
        if list_string[i] in punctuation_marks or list_string[i] in sentence_ends:
            punctuations.append(list_string[i])
    punctuations_only = ''.join(str(x) for x in punctuations)
    return punctuations_only

def count_punctuation(string):
    '''
    Takes string as input. Calculates percentages for each punctuation type.
    '''
    total_punctuations = len(string)

    counts = {}

    for n in string:
        keys = counts.keys()
        if n in keys:
            counts[n] += 1
        else:
            counts[n] = 1

    return counts

def make_plots(counts):
    """
    Requires frequency table, of type(dict), as input. 
    Returns simple bar chart. 
    """

    plt.bar(*zip(*counts.items()))
    plt.show()

output_1 = strip_string(test_string)
output_2 = count_punctuation(output_1)
make_plots(output_2)


# Write functions that:
# Compute and return average number of spaces per sentence.
# Cleanly print: Average sentence length, the output punctuation, and the charts.



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