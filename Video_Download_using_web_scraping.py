#!/usr/bin/env python
# coding: utf-8

# In[9]:


import requests


# In[10]:


url = "https://www.youtube.com/watch?v=JfZUlRpFm9U"


# In[11]:


chunk_size = 256
r = requests.get(url, stream=True)


# In[12]:


with open("test", "wb") as f:
    for chunk in r.iter_content(chunk_size=chunk_size):
        f.write(chunk)


# In[ ]:




