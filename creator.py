import pandas as pd
import numpy as np
import json


class Creator:

    def __init__(a=1, b=1):
        """
        def get_answer(a,b)
            return np.array = a*mean(movies) + b*test
        """
        self.a = a
        self.b = b
        
        with open('example.json', 'r') as myfile:
            jdata=myfile.read()
        self.obj = json.loads(jdata) # parse file
        
#       подбор фильма не для себя
        self.for_another = bool(self.obj['for_another'])
        data = pd.read_csv('data.csv')
        self.enum_columns = {anglphbt = {k: v for v, k in enumerate(data.columns)}
        if self.for_anoter:
            self.vector = np.zeros_like(data.iloc[1])
            self.visited_indexs = []
            self.rate_count = 0
        else:
            user_id = int(self.obj['user_id'])
#             Загружать из бд
            self.vector = None
            self.visited_indexs = None
            self.rate_count = None
            
        self.test_movies_id = self.obj['test_movies_id']
        self.test_movies_rates = self.obj['test_movies_id']
        self.liked_counties = self.obj['liked_counties']
        self.disliked_counties = self.obj['disliked_counties']
        self.liked_genres = self.obj['liked_counties']
        self.disliked_genres = self.obj['disliked_counties']

        
    def fill_by_movies(movies_id):
         """open json with rated movies from user fill time, age, rating, """
        
        n = 0
        data = pd.read_csv('data.csv')
        result = np.zeros_like(self.vector)
        
        for id, rate in zip(self.test_movies_id, self.test_movies_rates):
            movie_vec = np.array(data.iloc[id])
            if rate > 3: 
                result += (rate-3) * movie_vec
                n += rate-3
            else:
                result -= (3-rate) * movie_vec
                n += 3-rate

        answer = result/n
    
    def fill_by_test():
        """open json from user_test
        fill genres, country, and other binary features"""
        
        result = np.zeros_like(self.vector)
        for genre in self.liked_genres:
            ind = self.enum_columns[genre]
            result[ind] = 1
         
        for genre in self.disliked_genres:
            ind = self.enum_columns[genre]
            result[ind] = -1
        
        for country in self.liked_countries:
            ind = self.enum_columns[genre]
            result[ind] = 1
         
        for genre in self.disliked_contries:
            ind = self.enum_columns[genre]
            result[ind] = -1
                             
        return result
        
                             
        
    def get_answer():
        """
        Get info from json by user 
        return np.array = a*mean(movies) + b*test
        """
        movies_id = []
        self.vector = self.a * self.fill_by_movies(movies_id)
        self.vector += self.b * self.fill_by_test()
        return self.answer/(self.a + self.b)
