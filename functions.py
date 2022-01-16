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
    Takes string as input. Returns frequency table as output (dict). 
    '''
    