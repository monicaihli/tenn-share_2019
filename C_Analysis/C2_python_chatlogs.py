# Demonstrates more workflows with pandas
# this is a round-about way to get to a frequency count or produce another file for further processing,
# but it illustrates how to apply the techniques we've talked about across entire columns of data
# when working in pandas

import pandas
from nltk.corpus import stopwords # removes unimportant words
from nltk.stem import WordNetLemmatizer # converts words to their lemma (standardized) form
from nltk import FreqDist  # allows us to report frequency of words in text
import datetime

from nltk.tokenize import word_tokenize

data = pandas.read_csv('./utk_libchat.csv') # read data from a file

print(data.shape) # show us how many rows and columns there are.
print(data.columns.values) # display the columns that were imported

data = data.drop(columns=["Time","Details","Notes", "Question", "Question via", "Type of Question", "Entered By",
                          "How much time did it take?", "Ticket #", "Who asked?"]) # accepts a list of column names to drop
print(data.shape) # show us how many rows and columns there are.
print(data.columns.values) # display the columns that were imported

print(data.dtypes) # lets discover what the datatypes are


# we could subset data based on timeframe this way, if we wanted to
data['Date'] = pandas.to_datetime(data['Date']) # convert the Date column to proper datatype so we can do appropriate operations on it
print(data.dtypes)
print(data.head(5))


# clean html tags up with pandas version of replace.
data['Answer'] = pandas.Series(data['Answer'].str.lower())
print(data.head(5))


data['Answer'] = pandas.Series(data['Answer'].str.replace('<br />', '', regex=False))
print(data.head(5))

# Gets rid of names using regex, such as "John Doe: How can I help you?" It's not very good so far but it helps a little
data['Answer'] = data['Answer'].str.replace('^[^:]+:\s*','')
print(data.head(5))


data['Answer'] = pandas.Series(data['Answer'].str.replace('\n', ' ', regex=False)) # more cleanup of newlines and tabs
data['Answer'] = pandas.Series(data['Answer'].str.replace('\t', '', regex=False))

print(data.head(5))

data['Answer'] = data['Answer'].str.replace('\d+','') # get rid of numbers with regex
data['Answer'] = data['Answer'].str.replace('[^\w\s]','') # get rid of punctuation with regex
print(data.head(5))

data['Answer'] = data['Answer'].str.replace('\s{2,}',' ') # also deal with multiple spaces using regex
print(data.head(5))

data = data.dropna() # we have to drop rows with null values at this point or they will cause problems later.
print(data.shape)




#  SUBSET
data_subset = data[(data['Date']>datetime.date(2019,1,1)) & (data['Date']<datetime.date(2019,12,31))]
print(data_subset.head(5))
print(data_subset.shape)

# STOPWORDS - It's a little trickier here. Note: "lambda x" is just a fancy, compact way of applying a function to every value in the column
stop = stopwords.words('english')
data['Answer'] = data['Answer'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)])) # get rid of stopwords
print(data.head(5))

# LEMMA example demonstrating the use of apply() to apply a function against every row in the column
def lemmatize_text(text):
  return [lemmatizer.lemmatize(w) for w in word_tokenize(text)]
lemmatizer = WordNetLemmatizer()
data['text_lemmatized'] = data['Answer'].apply(lemmatize_text) #


# put the words back together in preparation for writing to file so we can do other analysis with it

def put_together(text):
  text_ = ""
  for word in text:
    text_ += word + ' '
  return(text_)
data['text_lemmatized'] = data['text_lemmatized'].apply(put_together)
print(data.head(5))
data.to_csv('chat_prepped.csv', index=False)


# going to combine everything in the dataframe to get word distribution
combined_text = data['Answer'].str.cat(sep=' ')
combined_text = word_tokenize(combined_text)
freq = FreqDist(combined_text)
with open('freq.csv', 'a') as freqfile:
  for key in freq:
    freqfile.write(key + ',' + str(freq[key]) + '\n')
