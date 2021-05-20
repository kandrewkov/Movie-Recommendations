#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import json


def fill_by_movies(name):

def get_answer():
#   open json from user_test
#   fill genres, country, and other binary features

#   open json with rated movies from user
# fill time, age, rating, 

    answer = np.zeros(len(data))
    
    return answer

movies = pd.read_csv('preproc_movies_nobudget.csv', index_col=0)
data = movies.drop(['Unnamed: 0.1', 'movie_duration','kp_rating', 'kp_rating_count', 'movie_year','imdb_rating', 'imdb_rating_count',  'movie_id', 'name_rus', 'name_eng', 'critics_rating'], axis=1)
short_data = pd.read_csv('short_data.csv', index_col=0)

answer = get_answer()
# answer = np.array(data[movies['name_rus'] == '47 ронинов'])
neigh = NearestNeighbors()
neigh.fit(data)
indexs = neigh.kneighbors(answer.reshape(1, -1), 5, return_distance=False)
short_data.iloc[indexs[0]]['name_rus']

short_data.iloc[indexs[0]].to_json('prediction.json')

