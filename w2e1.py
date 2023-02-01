#!/usr/bin/env python
# coding: utf-8

# In[38]:


import json
ratings = 0
movies = 0

with open("/Users/johnspurrier/Downloads/imdb_movies_1985to2022.json", "r") as f:
    for line in f:
        movie = json.loads(line)
        for actor in movie['actors']:
            if actor[1] == "Hugh Jackman":
                movies +=1
                ratings = ratings + movie['rating']['avg']
    print(ratings/movies)

