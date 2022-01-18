'''
TODO:
# Must implement a series of checks; while True, try, except, must be string, etc. 
# Check for weird spaces, gaps, tabs etc. and issue errors to user. Double spaces should count as a single space / split sentence. 
# Count number of punctuations per sentence, too. And plot that as well. 
# Cleanly print: Average sentence length, the output punctuation, and the charts. Formatted.
# Clean up charts, add titles 
# Calculate algorithmic complexity. 
# Add timeit functionss, and print it every time. 
# Clean up and compartmentalize code. 
# Write tests in pytest, for each function. 
# Build streamlit app. 
'''

import functions
import matplotlib.pyplot as plt
from timeit import Timer
import re
import numpy as np

punctuation_marks = [',', '.', '—', '-', ':', ';', '(', ')', "'", '[', ']', '{', '}', '...']
sentence_ends = ['.', '!', '?']

test_string = "The gobbledy gook, I dare say, is abhorrent—but isn't that the price to pay, my love?"
test_string2 = "The gobbledy gook, I dare say, is abhorrent—but isn't that the price to pay, my love? Now I'm trying with a second sentence."
test_string3 = """This is a story about love and death in the golden land, and begins with the country. The San Bernardino Valley lies only an hour east of Los Angeles by the San Bernardino Freeway but is in certain ways an alien place: not the coastal California of the subtropical twilights and the soft westerlies off the Pacific but a harsher California, haunted by the Mojave just beyond the mountains, devastated by the hot Santa Ana wind that comes down through the passes at 100 miles an hour and whines through the eucalyptus windbreaks and works on the nerves. October is the bad month for the wind, the month when breathing is difficult and the hills blaze up spontaneously. There has been no rain since April. Every voice seems a scream. It is the season of suicide and divorce and prickly dread, wherever the wind blows."""
moby_dick = "I stuffed a shirt or two into my old carpet-bag, tucked it under my arm, and started for Cape Horn and the Pacific. Quitting the good city of old Manhatto, I duly arrived in New Bedford. It was a Saturday night in December. Much was I disappointed upon learning that the little packet for Nantucket had already sailed, and that no way of reaching that place would offer, till the following Monday. As most young candidates for the pains and penalties of whaling stop at this same New Bedford, thence to embark on their voyage, it may as well be related that I, for one, had no idea of so doing. For my mind was made up to sail in no other than a Nantucket craft, because there was a fine, boisterous something about everything connected with that famous old island, which amazingly pleased me. Besides though New Bedford has of late been gradually monopolising the business of whaling, and though in this matter poor old Nantucket is now much behind her, yet Nantucket was her great original—the Tyre of this Carthage;—the place where the first dead American whale was stranded. Where else but from Nantucket did those aboriginal whalemen, the Red-Men, first sally out in canoes to give chase to the Leviathan? And where but from Nantucket, too, did that first adventurous little sloop put forth, partly laden with imported cobblestones—so goes the story—to throw at the whales, in order to discover when they were nigh enough to risk a harpoon from the bowsprit? Now having a night, a day, and still another night following before me in New Bedford, ere I could embark for my destined port, it became a matter of concernment where I was to eat and sleep meanwhile. It was a very dubious-looking, nay, a very dark and dismal night, bitingly cold and cheerless. I knew no one in the place. With anxious grapnels I had sounded my pocket, and only brought up a few pieces of silver,—So, wherever you go, Ishmael, said I to myself, as I stood in the middle of a dreary street shouldering my bag, and comparing the gloom towards the north with the darkness towards the south—wherever in your wisdom you may conclude to lodge for the night, my dear Ishmael, be sure to inquire the price, and don’t be too particular. With halting steps I paced the streets, and passed the sign of “The Crossed Harpoons”—but it looked too expensive and jolly there. Further on, from the bright red windows of the “Sword-Fish Inn,” there came such fervent rays, that it seemed to have melted the packed snow and ice from before the house, for everywhere else the congealed frost lay ten inches thick in a hard, asphaltic pavement,—rather weary for me, when I struck my foot against the flinty projections, because from hard, remorseless service the soles of my boots were in a most miserable plight. Too expensive and jolly, again thought I, pausing one moment to watch the broad glare in the street, and hear the sounds of the tinkling glasses within. But go on, Ishmael, said I at last; don’t you hear? get away from before the door; your patched boots are stopping the way. So on I went. I now by instinct followed the streets that took me waterward, for there, doubtless, were the cheapest, if not the cheeriest inns. Such dreary streets! blocks of blackness, not houses, on either hand, and here and there a candle, like a candle moving about in a tomb. At this hour of the night, of the last day of the week, that quarter of the town proved all but deserted. But presently I came to a smoky light proceeding from a low, wide building, the door of which stood invitingly open. It had a careless look, as if it were meant for the uses of the public; so, entering, the first thing I did was to stumble over an ash-box in the porch. Ha! thought I, ha, as the flying particles almost choked me, are these ashes from that destroyed city, Gomorrah? But “The Crossed Harpoons,” and “The Sword-Fish?”—this, then must needs be the sign of “The Trap.” However, I picked myself up and hearing a loud voice within, pushed on and opened a second, interior door. It seemed the great Black Parliament sitting in Tophet. A hundred black faces turned round in their rows to peer; and beyond, a black Angel of Doom was beating a book in a pulpit. It was a negro church; and the preacher’s text was about the blackness of darkness, and the weeping and wailing and teeth-gnashing there. Ha, Ishmael, muttered I, backing out, Wretched entertainment at the sign of ‘The Trap!’ Moving on, I at last came to a dim sort of light not far from the docks, and heard a forlorn creaking in the air; and looking up, saw a swinging sign over the door with a white painting upon it, faintly representing a tall straight jet of misty spray, and these words underneath—“The Spouter Inn:—Peter Coffin.” Coffin?—Spouter?—Rather ominous in that particular connexion, thought I. But it is a common name in Nantucket, they say, and I suppose this Peter here is an emigrant from there. As the light looked so dim, and the place, for the time, looked quiet enough, and the dilapidated little wooden house itself looked as if it might have been carted here from the ruins of some burnt district, and as the swinging sign had a poverty-stricken sort of creak to it, I thought that here was the very spot for cheap lodgings, and the best of pea coffee. It was a queer sort of place—a gable-ended old house, one side palsied as it were, and leaning over sadly. It stood on a sharp bleak corner, where that tempestuous wind Euroclydon kept up a worse howling than ever it did about poor Paul’s tossed craft. Euroclydon, nevertheless, is a mighty pleasant zephyr to any one in-doors, with his feet on the hob quietly toasting for bed. “In judging of that tempestuous wind called Euroclydon,” says an old writer—of whose works I possess the only copy extant—“it maketh a marvellous difference, whether thou lookest out at it from a glass window where the frost is all on the outside, or whether thou observest it from that sashless window, where the frost is on both sides, and of which the wight Death is the only glazier.” True enough, thought I, as this passage occurred to my mind—old black-letter, thou reasonest well. Yes, these eyes are windows, and this body of mine is the house. What a pity they didn’t stop up the chinks and the crannies though, and thrust in a little lint here and there. But it’s too late to make any improvements now. The universe is finished; the copestone is on, and the chips were carted off a million years ago. Poor Lazarus there, chattering his teeth against the curbstone for his pillow, and shaking off his tatters with his shiverings, he might plug up both ears with rags, and put a corn-cob into his mouth, and yet that would not keep out the tempestuous Euroclydon. Euroclydon! says old Dives, in his red silken wrapper—(he had a redder one afterwards) pooh, pooh! What a fine frosty night; how Orion glitters; what northern lights! Let them talk of their oriental summer climes of everlasting conservatories; give me the privilege of making my own summer with my own coals. But what thinks Lazarus? Can he warm his blue hands by holding them up to the grand northern lights? Would not Lazarus rather be in Sumatra than here? Would he not far rather lay him down lengthwise along the line of the equator; yea, ye gods! go down to the fiery pit itself, in order to keep out this frost?"

def count_spaces(string):
    '''
    Takes string as input.
    Counts spaces between each '.', '!' or '?' character, and adds one, using str.split(). 
    Returns words per sentence, as an array. 
    '''
    len_distribution = []
    sentences = re.split("[!?.]+", string)

    counter = 0
    for sentence in sentences:            
        for character in sentence:
            if character == ' ' or character == '—':
                counter += 1
           
        len_distribution.append(counter)
        counter = 0

    len_distribution[0] += 1
    mean_length = np.mean(len_distribution)
    print("Mean sentence length: " + str(round(mean_length, 2)) + " words")
    return len_distribution[:-1]

def strip_string(string):
    '''
    Add text here.
    '''
    list_string = list(string)
    punctuations = []
    for i in range(len(list_string)):
        if list_string[i] in punctuation_marks or list_string[i] in sentence_ends:
            punctuations.append(list_string[i])
    punctuations_only = ''.join(str(x) for x in punctuations)
    return punctuations_only

def format_punctuations(string, set_width = 20):
    '''
    Documentation
    '''
    list_string = list(string)
    new_list = []
    for i in range(len(list_string)):
        if i % set_width == 0 and i != 0:
            new_list.append('\n')
        new_list.append(list_string[i])
        
    final_string = ''.join(new_list)
    return final_string

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

def make_bar_chart(counts):
    """
    Requires frequency table, of type(dict), as input. 
    Returns simple bar chart. 
    """
    plt.bar(*zip(*counts.items()))
    plt.show()

def make_histogram(sentence_lengths):
    """
    Documentation here.
    """
    plt.hist(sentence_lengths, density=False)
    plt.ylabel('No. of sentences')
    plt.xlabel('Sentence length, in words')

sentence_lengths = count_spaces(moby_dick)
output_1 = strip_string(moby_dick)
formatted_output = format_punctuations(output_1)
output_2 = count_punctuation(output_1)
print(formatted_output)
print(output_2)

# if __name__=='__main__':
#     t = Timer(lambda: squareRootBi(x, epsilon))
#     print("Time to run bisection search: " + str(t.timeit(number=1)))

make_bar_chart(output_2)
make_histogram(sentence_lengths)