########################################################################################################################
#
# This script demonstrates some common string operations in Python
#
########################################################################################################################

import re # used for regular expressions


########################################################################################################################
print('\n' + '*'*80 + '\n') # skip lines

# JOINING STRINGS

string1 = "Hello"
string2 = "world."

print(string1 + string2)

print('\n')

print(string1 + ' ' + string2)


print('\n' + '*'*80 + '\n') # skip lines
########################################################################################################################




# STRATEGIES TO REMOVE DIFFERENT EXAMPLES OF WHITESPACE

test_string = "\t\tHello\nworld.       Are \tyou out there?"
print("ORIGINAL TEXT:  " + test_string)

# .strip()
test_string = test_string.strip() # strip only affects whitespace at beginning or end of string
print('\n\n.STRIP():  ' + test_string)

# .replace()
test_string = test_string.replace("\t", " ") # substitute spaces for newlines and tabs
test_string = test_string.replace("\n", " ")
print('\n\n.REPLACE(): '+ test_string)


# regular expression
test_string = re.sub(r"\s{2,}", " ", test_string) # Regular expression looks for more than 2 spaces and replaces with single space
print('\n\nREGULAR EXPRESSION: ' + test_string)


print('\n' + '*'*80 + '\n') # skip lines
########################################################################################################################

# .FIND() - only some functionality is shown here. There are many more tricks shown in the documentation

test_string = "The cow jumped over the moon."
search_word = "cow"
find_result = test_string.find(search_word) # returns -1 if not found, or the position where the word starts if found
if find_result != -1:
  print("In the sentence: " + test_string)
  print("The word " + search_word + " is found at position " + str(find_result))

print('\n')

# .find() combined with .replace()
test_string = "The cow jumped over the moon."
search_word = "cow"
new_word = "ferret"
find_result = test_string.find(search_word) # returns -1 if not found, or the position where the word starts if found
if find_result != -1:
  test_string = test_string.replace(search_word,new_word)
  print("New sentence: " + test_string)


print('\n' + '*'*80 + '\n') # skip lines
########################################################################################################################

# CONVERTING CASE

test_string = "Some say a cat's motto is IF I FITS, I SITS. But I've noticed that not fitting doesn't stop them from trying."

print(test_string.upper())

print(test_string.lower())

