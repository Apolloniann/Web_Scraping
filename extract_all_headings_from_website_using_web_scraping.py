#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
type(res)
res.text

soup=bs4.BeautifulSoup(res.text,'lxml')
type(soup)

hi = soup.select('.mw-headline')
hi

for i in soup.select('.mw-headline'):
    print(i.text)





