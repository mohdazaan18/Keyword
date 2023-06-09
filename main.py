import requests
import urllib
from bs4 import BeautifulSoup

url = input("Enter the link : ").strip()
# url = 'https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/'
website = requests.get(url)
website_text = website.text
soup = BeautifulSoup(website_text,"html.parser")
links=[]
for link in soup.find_all('a'):
  links.append(link.get('href'))

for link in links:
  if len(link)>1:
    print(link)
  
  