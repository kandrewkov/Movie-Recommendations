from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import json
import Creator from creator


movies = pd.read_csv('preproc_movies_nobudget.csv', index_col=0)
data = movies.drop(['Unnamed: 0.1', 'movie_duration','kp_rating', 'kp_rating_count', 'movie_year','imdb_rating', 'imdb_rating_count',  'movie_id', 'name_rus', 'name_eng', 'critics_rating'], axis=1)
short_data = pd.read_csv('short_data.csv', index_col=0)

c = Creator()
answer = c.get_answer()
neigh = NearestNeighbors()
neigh.fit(data)
indexs = neigh.kneighbors(answer.reshape(1, -1), 5, return_distance=False)
short_data.iloc[indexs[0]]['name_rus']
short_data.iloc[indexs[0]].to_json('prediction.json')

