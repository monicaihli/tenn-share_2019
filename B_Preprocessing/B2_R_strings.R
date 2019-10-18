# stringr is a popular r package for string manipulation

#install.packages("stringr")
library(stringr)

test_string <-"865-423-0000" #sometimes it's convenient to split strings up into smaller parts, like a phone number
str_split(test_string, "_")

# Concatenation can be done with str_c()
str_c("May", "the", "Fourth","be","with","you")
str_c("May", "the", "Fourth","be","with","you", sep = ' ')


# Number of characters with str length()
sentence = "one, two, three"
str_length(sentence)

words = c("one", "two", "three")
str_length(words)


# Substring with str sub()
test <- "Hello World"
str_sub(test, 1, 5) # asks for a substring of the first 5 characters
substring(test, 1, 5)


# replacing substrings
test = "Hello world."
str_sub(test, 1, 5) <- "Goodbye" # replace characters 1-5 with this other word
test

# padding says that you should fill in with whitepace till you get to that length of characters
str_pad("two", width = 7)
str_pad("four", width = 7)

test <- c('0', '0000', '0000000')
str_pad(test, width=7)

# trimming gets rid of whitespace
test = c("    It's late but that's what coffee is for.     ")
str_trim(test, side = "left")
str_trim(test, side = "right")
str_trim(test, side = "both")

