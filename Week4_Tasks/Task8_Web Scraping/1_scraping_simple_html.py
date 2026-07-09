# BeautifulSoup parses the HTML file and creates a BeautifulSoup object that 
# represents the entire HTML document as a tree.

from bs4 import BeautifulSoup
import requests

with open('KF_training/Week4_Tasks/Task8_Web Scraping/simple.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')
    # print(type(soup))

# Returns the HTML with proper indentation and formatting
# print(soup.prettify())


# Returns title from the html_file
# print(soup.title)
# print(soup.title.text)


# Returns first div tag from the html_file
# print(soup.div)

# Returns the first <div> whose class is "article"
match = soup.find('div',class_="article")
# print(match)

# Returns the first <div> whose class is "footer"
match = soup.find('div',class_="footer")
# print(match)



# Accessing nested HTML elements using Tag objects

article = soup.find('div',class_='article')
# print(article)

title = article.h2.a.text
# print(title)

summary = article.p.text
# print(summary)

# Acessing all the class article instead of getting first article

for article in soup.find_all('div',class_='article'):
    title = article.h2.a.text
    print(title)

    summary = article.p.text
    print(summary)

    print()

