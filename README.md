# punctuation-tracker-2.0
Remove words and leave behind punctuation. Count the average length of a text's sentences, plot it as a histogram, and receive other information. Inspired by [Clive Thompson's](https://medium.com/creators-hub/what-i-learned-about-my-writing-by-seeing-only-the-punctuation-efd5334060b1) tool.

This tool is similar to Thompson's, albeit with a few changes:
a) It automatically generates charts as an output, akin to [this WIRED](https://www.wired.com/2016/02/charting-punctuation-usage-in-literary-classics/) article.
b) It counts the number of words and the number of punctuations per sentence, and saves these data as an array.
c) Consolidates utility into a series of functions.

### Instructions
This is a command line tool, built with Python 3. Simply run `app.py` from the command line and input a text to analyze. A paragraph from `Joan Didion` and `Moby Dick` are provided as test cases.
