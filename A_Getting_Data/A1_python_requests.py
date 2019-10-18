########################################################################################################################
#
#  Demonstrates different ways of using requests library to make an HTTP request and grab content from a web page
#  This is just like using your browser, only we can use Python instead!
#  To watch what's happening, try stepping through using PyCharm's debug feature. :D
#  Requests documentation: https://requests.kennethreitz.org/en/master/
#
########################################################################################################################

import requests # tells the script to use the requests library


# SUPER SIMPLE EXAMPLE
response = requests.get("https://google.com") # Get this URL and save it to a variable
print(response.content) # display the contents of the page (in this case, the source code for the page)
print(response.headers) # the headers of a response object are stored as a python dictionary
print(response.headers['date']) # So we can access the individual elements in the headers as such

print('\n' + '*'*80 + '\n') # overengineered way of skipping a line in the output


########################################################################################################################

# EXAMPLE TESTING FOR A SUCCESSFUL CONNECTION
good_url = "https://lib.utk.edu" # This time, we'll store the url in a variable.
response = requests.get(good_url) # Get this URL and save it
if response.status_code == 200:   # Test if the response's status code is a good one
  print("Success!")

print('\n' + '*'*80 + '\n') # skip a line

bad_url = "https://lib.utk.edu/oops-doesnt-exist"
response = requests.get(bad_url)
if response.status_code == 200:
  print("Success!")
elif response.status_code == 404:
  print("Whoops, page not found!")
else:
  print("I have no idea what just happened.")

print('\n' + '*'*80 + '\n') # skip a line

########################################################################################################################


# PubMed OAI-PMH Web services example that uses parameters

# We could just build a string variable containing the complete request
url = "https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi?verb=ListRecords&from=2019-02-01&until=2019-10-01&set=bmcbioc&metadataPrefix=oai_dc"
response = requests.get(url=url)
print("RESPONSE WHEN WE PASS THE COMPLETE URL:")
print(response.content)

print('\n')

base_url = 'https://www.ncbi.nlm.nih.gov/pmc/oai/oai.cgi'
parameters = {
  'verb': 'ListRecords',
  'from': '2019-02-01',
  'until': '2019-10-01',
  'set': 'bmcbioc',
  'metadataPrefix': 'oai_dc'
}
response = requests.get(url=base_url, params=parameters)
print('SAME RESPONSE WHEN WE BUILD REQUEST FROM BASE URL AND PARAMETERS:')
print(response.content)

print('\n' + '*'*80 + '\n') # skip a line


########################################################################################################################

# Example using headers to tell the server what kind of format we'd like our response in

base_url = "https://api.elsevier.com/content/affiliation/affiliation_id/"
affiliation_id = "60024266"
url = base_url + affiliation_id
headers = {"Accept": "application/xml"}  #
response = requests.get(url, headers=headers)
print('RESPONSE WHEN WE USE HEADERS TO ASK THE SERVER FOR XML')
print(response.content)

print('\n')

base_url = "https://api.elsevier.com/content/affiliation/affiliation_id/"
affiliation_id = "60024266"
url = base_url + affiliation_id  # we can concatenate variables with text together to form something new.
headers = {"Accept": "application/json"}  #
response = requests.get(url, headers=headers)
print('DIFFERENT RESPONSE WHEN WE USE HEADERS TO ASK THE SERVER FOR JSON')
print(response.content)

########################################################################################################################