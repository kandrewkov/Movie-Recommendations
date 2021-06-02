from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
import json
from creator import Creator


movies = pd.read_csv('preproc_data2.csv', index_col=0)
data = movies.drop(['Unnamed: 0.1', 'movie_id', 'name_rus', 'name_eng'], axis=1)
short_data = pd.read_csv('short_data.csv', index_col=0)

# КЛАСС ОБРАБОТЧИКА ОТВЕТОВ ПОЛЬЗОВАТЕЛЯ, КОТОРЫЙ СГЕНЕРИРУЕТ ВЕКТОР
c = Creator()
# ВЕКТОР ПОЛУЧЕННЫЙ КЛАССОМ ИЗ JSON (НЕ НАПИСАНО, КАК ОН ЕГО ИМЕННО ОБРАБАТЫВАЕТ)
vector = c.get_vector()
# СОЗДАЕМ И "ОБУЧАЕМ" МОДЕЛЬ
neigh = NearestNeighbors()
neigh.fit(data)
# ПОЛУЧАЕМ ИНДЕКСЫ ПОДХОДЯЩИХ ФИЛЬМОВ ИЗ DATA. Порядок фильмов в short data такой же.
indexs = neigh.kneighbors(vector.reshape(1, -1), 5, return_distance=False)
# Упаковываем краткую информацию с нужных фильмов
short_data.iloc[indexs[0]].to_json('prediction.json')

