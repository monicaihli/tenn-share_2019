#
# This script takes an export from Web of Science in tab-delimited form, drops everything except for
# the Title (TI), Abstract, (AB), Publication Year (PY), and the system ID number for the document (UT).
# It creates a corpus object from the tm package and performs text cleaning steps, and then generates a
# TermDocumentMatrix which is used for aggregation of word counts. We use a wordcloud package for the visualization of
# our word frequency counts.
#

setwd('') # UPDATE with the path to your data file
df = read.delim('one.txt', header=TRUE, sep="\t", na.strings = "",row.names = NULL, stringsAsFactors = FALSE)
temp_df = read.delim('two.txt', header=TRUE, sep="\t", fill=TRUE,row.names = NULL, stringsAsFactors = FALSE)
df<-rbind(df, temp_df)
temp_df = read.delim('three.txt', header=TRUE, sep="\t", fill=TRUE,row.names = NULL, stringsAsFactors = FALSE)
df<-rbind(df, temp_df)
temp_df = read.delim('four.txt', header=TRUE, sep="\t", fill=TRUE,row.names = NULL, stringsAsFactors = FALSE)
df<-rbind(df, temp_df)
temp_df = read.delim('five.txt', header=TRUE, sep="\t", fill=TRUE,row.names = NULL, stringsAsFactors = FALSE)
df<-rbind(df, temp_df)
temp_df = read.delim('six.txt', header=TRUE, sep="\t", fill=TRUE,row.names = NULL, stringsAsFactors = FALSE)
df<-rbind(df, temp_df)
remove(temp_df)
##############################################################################################

library(dplyr)
library(tm)
library(wordcloud)

##############################################################################################
df<-mutate(df, TIAB = paste(TI, AB)) # combine title and abstract
df<-select(df,c('UT','PY', 'TIAB')) # get rid of all non-relevant columns
colnames(df)<-c('doc_id','PY', 'text') # rename to header values necessary for tm DataframeSource()
df_corpus <- VCorpus(DataframeSource(df)) # create a tm package volatile corpus.
#meta(df_corpus) # display the metadata columns associated with each document in the corpus (in this case, pub year)

##############################################################################################
df_corpus <- tm_map(df_corpus, stripWhitespace) # clean whitespace
df_corpus <- tm_map(df_corpus, content_transformer(tolower)) # transform to lowercase
df_corpus <- tm_map(df_corpus, removeWords, stopwords("english")) # stopword removal
df_corpus <- tm_map(df_corpus, content_transformer(removePunctuation))
df_corpus <- tm_map(df_corpus, content_transformer(removeNumbers))
df_corpus <- tm_map(df_corpus, stemDocument) # stemming
#df_corpus <- tm_map(df_corpus, lemmatize_strings) # lemmatize
df_corpus <- tm_map(df_corpus, PlainTextDocument)
df_corpus <- tm_map(df_corpus, removeWords, c("use", "via","first","allow","howev","one","also","may")) # manually select your words to exclude from the analysis
##############################################################################################

TDM <- TermDocumentMatrix(df_corpus)  # create a term document matrix (look it up!)
inspect(TDM) # show you some of the contents of the TDM
m <- as.matrix(TDM) # convert the contents of TDM to a matrix, which allows some different manipulations
v <- sort(rowSums(m),decreasing=TRUE) # aggregate the word counts
word_counts_df <- data.frame(word = names(v),freq=v) # move the words and their frequency counts into a dataframe
head(d, 10)

# make the wordcloud using the dataframe as an input:
set.seed(1234)
wordcloud(words = word_counts_df$word, freq = word_counts_df$freq, min.freq = 1,
          max.words=200, random.order=FALSE, rot.per=0.35,
          colors=brewer.pal(8, "Dark2"))



