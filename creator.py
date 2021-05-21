import pandas as pd
import numpy as np
import json


class Creator:

    def __init__(answer=None, a=1, b=1):
        """
        def get_answer(a,b)
            return np.array = a*mean(movies) + b*test
        """
        if answer is None:
            self.answer = np.array(len(data))
        else:
            self.answer = answer
            
        self.a = a
        self.b = b
        # read file
        with open('example.json', 'r') as myfile:
            data=myfile.read()
        # parse file
        self.obj = json.loads(data)
        
    def fill_by_movies(movies_id):
         """open json with rated movies from user fill time, age, rating, """
        data = pd.read_csv('data.csv')
        result = np.zeros(len(data.shape))
        count = 0
        data.iloc[id]
        for id in movies_id:
            movie_vec = np.array(data.iloc[id])
            n += rate
            rate = obj['rate']
            
            if rate > 3: 
                result += rate * movie_vec
            else:
                result -= rate * movie_vec

        answer = result/count
    
    def fill_by_test():
        """open json from user_test
        fill genres, country, and other binary features"""
        
    def get_answer():
        """
        Get info from json by user 
        return np.array = a*mean(movies) + b*test
        """
        movies_id = []
        self.answer = self.a * self.fill_by_movies(movies_id)
        self.answer += self.b * self.fill_by_test()
        return self.answer/(self.a + self.b)
