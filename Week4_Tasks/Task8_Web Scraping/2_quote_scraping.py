import requests
import json
import csv
from bs4 import BeautifulSoup



# practicing with only one first quote 

# url = f"https://quotes.toscrape.com"
# source = requests.get(url).text
# soup = BeautifulSoup(source,'lxml')
# # print(soup.prettify())

# quote_class= soup.find('div',class_="quote")
# quote = quote_class.span.text
# author = quote_class.find('small',class_='author').text
# tag_class = quote_class.find('div',class_='tags')
# tag = tag_class.find('a',class_='tag').text
# tags = [tag.text for tag in tag_class.find_all('a',class_='tag')] 

# link = quote_class.a['href']

# about_link = url + link
# source = requests.get(about_link).text
# soup = BeautifulSoup(source,'lxml')

# born = soup.find('div',class_="author-details")
# born_date = born.find('span',class_="author-born-date")
# print(born_date.text)

# print(quote)
# print(author)
# print(tag)
# print(tags)
# print(quote_class.prettify())


#---------------------- Actual webscraping code starts here ---------------------------

csv_file = open("KF_training/Week4_Tasks/Task8_Web Scraping/2_quote_scraping.csv",'w') 
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['quote','author','tags'])

lst =[]
# i=1 # Method-1

url = f"https://quotes.toscrape.com" # Method-2
while True:

# Method - 1 [pagination] -> by incrementing url page number

    # url = f"https://quotes.toscrape.com/page/{i}/"

    # source = requests.get(url).text
    # soup = BeautifulSoup(source,'lxml')

    # quote_classes = soup.find_all('div', class_='quote')

    # if not quote_classes:
    #     break


# Method - 2 [pagination] -> by observing whether next button is there or not 

    if url is None:
        break
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')

    next_button =  soup.find('li', class_='next')
    if next_button :
        next_page =  next_button.a['href']
        url = "https://quotes.toscrape.com" + next_page
    else:
        url = None


    for quote_class in soup.find_all('div',class_="quote"):
        quote = quote_class.span.text
        author = quote_class.find('small',class_='author').text
        tags = [tag.text for tag in quote_class.find_all('a',class_='tag')] 
        data = {
            "quote": quote,
            "author": author,
            "tags": tags
        }
        lst.append(data)
        csv_writer.writerow([quote,author,tags])

    # i+=1

with open("KF_training/Week4_Tasks/Task8_Web Scraping/2_quote_scraping.json",'w') as f:
    json.dump(lst,f,indent=2,ensure_ascii=False)
csv_file.close()
   
