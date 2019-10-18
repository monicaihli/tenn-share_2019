#########################################################################################################
#     Simple demonstration of httr to request content programmatically using R instead of a browser
#     Documentation: https://cran.r-project.org/web/packages/httr/vignettes/quickstart.html
#
#########################################################################################################


library(httr)

url<-'https://api.elsevier.com/content/affiliation/affiliation_id/60024266/'
response <- GET(url)  # make the request and save to a variable
print(   headers(response)  )  # display headers from the server's response
print(   headers(response)$'content-type'   )  # Access the contents of one of the headers
print(   status_code(response))  # print the status code of the response, such as 200
headers(response)$date # Access contents of another header
print(  (content(response))  )


raw_content <- content(response, "raw") # assign the raw content to a variable
writeBin(raw_content, "response.txt") # write the bytes to file
