########################################################################################################################
#
#  This script prints a list of database titles from a library's A-Z list.
#
#  Demonstrates using Selenium to manipulate a driver that can control your browser (Chrome).
#  Selenium documentation: https://selenium-python.readthedocs.io/
#
#  Chromedriver documentation: https://chromedriver.chromium.org/
#
########################################################################################################################


from selenium import webdriver
from bs4 import BeautifulSoup
import time # a utility that will help us add time delays where appropriate


url = 'https://libguides.utk.edu/az.php'

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get(url) # instead of using requests to get the page, we are using a browser controlled by the driver
time.sleep(4) # pause for a few seconds, give the page time to fully load
soup = BeautifulSoup(driver.page_source, 'lxml')
results = soup.find(id="s-lg-az-result-count")  # In this web page, there's an html tag that reports how many databases
print(results.text)
print('/n') # print a blank line
if soup.find(id="s-lg-az-content"):
  results_panel = soup.find(id="s-lg-az-content")
  for result in results_panel.find_all("div", "s-lg-az-result"):  # FOR EVERY RESULT ON PAGE:
      if result.find('a'):  # TITLE ELEMENT
        link = result.find('a')
        if link.find('span'):
          link.find('span').replace_with('')  # remove "This link opens in a new window" span if found
        print(link.text)