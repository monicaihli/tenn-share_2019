#########################################################################################################
#     Simple demonstration of rvest for webscraping. Goes beyond httr to give you sophisticated methods
#     for parsing HTML content that is received. This demonstration shows two ways of selecting html nodes
#     In one case, we see XPATH being used to navigate to a specific element. XPATH is a pretty common and
#     powerful tool for selecting nodes in HTML and XML. You'll encounter it across languages, libraries, and parsers
#     so it's worth spending a little time practicing with it.
#     The second selection technique simply shows selecting nodes by the type of tag, such as heading tags.
#
#     Documentation: https://cran.r-project.org/web/packages/rvest/rvest.pdf
#
#########################################################################################################

library(rvest)

url <- 'https://www.imdb.com/title/tt0126029/'  # Demo movie info page for SHREK (a personal favorite)
movie_page <- read_html(url) # read_html comes from the rvest package

node <-html_node(movie_page, xpath='//div[contains(@class, "title_wrapper")]') # see notes above about xpath
title <- html_nodes(node, "h1") # select an h1 node from within the first node
print(html_text(title))
