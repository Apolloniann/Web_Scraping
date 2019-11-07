#!/usr/bin/env python
# coding: utf-8

# In[1]:


import m3u8
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm_notebook as tqdm
import subprocess


# In[2]:


sess = requests.Session()


# In[3]:


r = sess.get("https://www.iplt20.com/video/144829/final-csk-vs-srh-fbb-stylish-player-of-the-match-lungi-ngidi")


# In[4]:


soup = BeautifulSoup(r.content, 'html5lib')


# In[5]:


video_id = soup.find('video', attrs={'id': 'playlistPlayer'})['data-video-id']
account_id = soup.find('video', attrs={'id': 'playlistPlayer'})['data-account']


# In[6]:


url = "https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8"

params = {
    'videoId': video_id,
    'pubId': account_id,
    'secure': True
}

r = sess.get(url, params=params)


# In[7]:


m3u8_master = m3u8.loads(r.text)
m3u8_playlist_uris = [playlist['uri'] for playlist in m3u8_master.data['playlists']]


# In[8]:


m3u8_master.data


# In[9]:


playlist_uri = m3u8_playlist_uris[0]


# In[10]:


r = sess.get(playlist_uri)
playlist = m3u8.loads(r.text)
m3u8_segment_uris = [segment['uri'] for segment in playlist.data['segments']]


# In[11]:


with open("video.ts", 'wb') as f:
    for segment_uri in tqdm(m3u8_segment_uris):
        r = sess.get(segment_uri)
        f.write(r.content)


# In[12]:


subprocess.run(['ffmpeg', '-i', 'video.ts', 'video.mp4'])

