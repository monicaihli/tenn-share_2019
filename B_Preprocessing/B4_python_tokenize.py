########################################################################################################################
#
# Demonstrates what tokenizing text looks like, in isolation of any other actual functionality that
# would do something with the tokenized data.
#
# The first time you go to work with NLTK, you'll have to download data, models, and other good stuff.
# The way to do that is to run a python command to initiate downloading the first time around.
# So either in a script or from python console start with "import nltk",
# Then "nltk.download()" which will launch a download utility. If you don't know what specific things you want
# and prefer to download everything (The option name in the menu is "All Packages"), just be warned it will
# eat up about 3.5 GB of space
#
# import nltk
# nltk.download()
#
########################################################################################################################


import nltk
import string

print('ORIGINAL TEXT:')
test_string = "Here is a demonstration using Natural Language Toolkit, or NLTK for short."
print(test_string)

print('\n')

print('ALL LOWERCASE:')
test_string = test_string.lower()
print(test_string)

print('\n')

print('PUNCTUATION REMOVED:')
translator = str.maketrans(string.punctuation,' ' * len(string.punctuation))  # trick for stripping punctuation & replace w/ whitespace
test_string = test_string.translate(translator)
print(test_string)


print('\n')

word_tokens = nltk.word_tokenize(test_string) # transforms the sentence into a list of words
print("TOKENIZED INTO A LIST OF WORDS:")
print(word_tokens)