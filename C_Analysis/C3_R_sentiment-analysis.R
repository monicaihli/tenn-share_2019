library(dplyr)
library(tidytext)
library(ggplot2)

dir <- "/home/monica/PycharmProjects/tenn-share_2019/C_Analysis/"
setwd(dir)

# tidyverse and tidytext will do many of the same functions we used in python: stopword removal, tokenizing, etc
chat_data <- read.csv(file='chat_prepped.csv',header=TRUE,sep=',', stringsAsFactors = FALSE)
chat_data <- chat_data[-c(3)] # drop the Date, Answer column which is third column. A more sophisticated analysis might subset on date

tokenized <- chat_data %>%
  unnest_tokens(word, text_lemmatized)

coded <- tokenized %>%
  inner_join(get_sentiments("bing")) # by using a join, we're only keeping words that are in the lexicon. much  more useful than keeping junk words

# for one approach to analyzing the data, map sentiments to numeric values:
mapping <- c("positive" = 1, "negative" = -1)

coded$numeric <- mapping[coded$sentiment]

chat_experiences <- aggregate(coded$numeric, by=list(Category=coded$Id), FUN=sum) # aggregate the values to get the overall experience in each chat


# a plot to show the overall distribution of the chat experiences
ggplot(chat_experiences, aes(x=chat_experiences$x)) + geom_histogram(binwidth=1)
