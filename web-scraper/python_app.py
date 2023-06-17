import requests
from bs4 import BeautifulSoup


url = 'https://www.codewithtomi.ml/'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content, 'lxml')
title = soup.find_all('h2', {'class':'post-title'})
print(title)

title_one = title[0].getText()
print(title_one)

# In a for loop
for t in title:
    print(t.getText())
