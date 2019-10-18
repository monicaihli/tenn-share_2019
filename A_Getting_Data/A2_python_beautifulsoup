########################################################################################################################
#
#     Prints all the news story titles at wate.com
#
#     Demonstrates using Beautiful Soup library to parse HTML and XML. Builds upon what was learned
#     with requests. Note that this is not a standard library. You will have to install BS separately.
#     Documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
#     Start by inspecting the elements at the web page before testing the code!
#
########################################################################################################################




from bs4 import BeautifulSoup  # tells the script we want to use this library
import requests

# Here's stuff we've done before
url = 'https://www.wate.com'
headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}
response = requests.get(url, headers=headers)
content = response.content



soup = BeautifulSoup(content, 'html.parser') # there are other parser options like lxml for parsing XML

news_stories = soup.find_all("h3", class_="article-list__article-title")  # the parent element that contains every story title
for story in news_stories: # since find_all returns a list of tags, we can iterate over them
  link = story.find('a') # in this case, a link <a> is nested inside each h3 element
  if link is not None: # As long as we can successfully find the link
    link_text = link.text # take the text part of that link
    link_text = link_text.strip() # a function to strip away whitespace. These titles have a bunch of whitespace for some reason
    print(link_text)
