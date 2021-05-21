from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import json
from creator import Creator


movies = pd.read_csv('preproc_movies_nobudget.csv', index_col=0)
data = movies.drop(['Unnamed: 0.1', 'movie_duration','kp_rating', 'kp_rating_count', 'movie_year','imdb_rating', 'imdb_rating_count',  'movie_id', 'name_rus', 'name_eng', 'critics_rating'], axis=1)
short_data = pd.read_csv('short_data.csv', index_col=0)

c = Creator()
vector = c.get_vector()
neigh = NearestNeighbors()
neigh.fit(data)
indexs = neigh.kneighbors(vector.reshape(1, -1), 5, return_distance=False)
short_data.iloc[indexs[0]].to_json('prediction.json')

