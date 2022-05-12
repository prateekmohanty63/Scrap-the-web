import requests
from bs4 import BeautifulSoup

url ="https://www.codewithharry.com"






# Step 1: Get the HTML
r =requests.get(url)
htmlContent=r.content
#print(htmlContent)

# Step 2: Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
#print(soup.prettify)


# Step 3 : HTML Tree traversal
title=soup.title
# print(title)
# print(type(title))


# Get all the paragraphs from the page
paras=soup.find_all('p')
#print(paras)


# Get all the anchor tags from the page
anchors=soup.find_all('a')
#print(anchors)


# find first paragraph
para=soup.find('p')
#print(para)

# find class of first para
#print(soup.find('p')['class'])


# find all the elements with class lead
print(soup.find_all("p",class_="lead"))