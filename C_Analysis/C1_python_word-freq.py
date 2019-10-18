########################################################################################################################
#
#   Simple example using NLTK to demonstrate preprocessing and word frequency.
#
#
########################################################################################################################

#file_name = './sample-text/declaration_of_ind.txt'
#file_name = './sample-text/1993-Clinton.txt'
#file_name = './sample-text/2001-GWBush-1.txt'



import string # adds some string manipulation functionality
from nltk.tokenize import word_tokenize # breaks text up into lists of words
from nltk.corpus import stopwords # removes unimportant words from text
from nltk import PorterStemmer # converts words to a stemmed form (with the ending broken off)
from nltk.stem import WordNetLemmatizer # converts words to their lemma (standardized) form
from nltk import FreqDist  # allows us to report frequency of words in text


file_name = './sample-text/demo-text.txt'


with open(file_name, 'r') as file:
  text = file.read()
print(text)
print('\n' + '*'*80 + '\n') # skip lines


# LOWERCASE AND REMOVE PUNCTUATION
text = text.lower() # make all lowercase
translator = str.maketrans(string.punctuation,' ' * len(string.punctuation))  # trick for stripping punctuation & replace w/ whitespace
text = text.translate(translator) # strip the punctuation
print(text)
print('\n' + '*'*80 + '\n') # skip lines


# TOKENIZE
word_tokens = word_tokenize(text) # tokenize the text
print(word_tokens)
print('\n' + '*'*80 + '\n') # skip lines


# STOPWORD REMOVAL
stop_words = set(stopwords.words('english'))
word_tokens = set(word_tokens) # convert the tokens from a list to a set to take advantage of easy set operations to remove stopwords
word_tokens = (word_tokens - stop_words)  # use set operation to remove stopwords
print(word_tokens) # note that word order is not preserved after this operation
print('\n' + '*'*80 + '\n') # skip lines


# STEMMING EXAMPLE
ps = PorterStemmer()
stemmed_text = "" # creating an empty string that will hold our text after the words have been stemmed
for word in list(word_tokens): # cast back to a list so we can take advantage of iterable functionality
  stemmed_text += ((ps.stem(word)) + ' ')
print('STEMMED TEXT:')
print(stemmed_text)
print('\n' + '*'*80 + '\n') # skip lines



# LEMMATIZATION EXAMPLE
lemmatizer = WordNetLemmatizer()
lemmatized_text = "" # empty string for storing the lemmatized text
for word in list(word_tokens): # cast back to a list so we can take advantage of iterable functionality
  lemmatized_text += ((lemmatizer.lemmatize(word)) + ' ')
print('LEMMATIZED TEXT:')
print(lemmatized_text)
print('\n' + '*'*80 + '\n') # skip lines



# COMPARE WORD FREQUENCY FOR STEMMED WORDS VS LEMMA
stemmed_text = word_tokenize(stemmed_text)
freq_stem = FreqDist(stemmed_text)
print("STEMMED WORDS")
print (freq_stem.most_common(5))

print('\n')
lemmatized_text = word_tokenize(lemmatized_text)
freq_lemma = FreqDist(lemmatized_text)
print("LEMMATIZED WORDS")
print (freq_lemma.most_common(5))



