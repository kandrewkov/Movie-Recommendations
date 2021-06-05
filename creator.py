import pandas as pd
import numpy as np
import json


class Creator:
    def __init__(self, a=1, b=2):
        """
        def get_answer(a,b)
            return np.array = a*mean(movies) + b*test
        """

        # self.a = a
        # self.b = b

        # Вот это написано вслепую
        with open('example.json', 'r') as myfile:
            jdata = myfile.read()
        self.obj = json.loads(jdata)  # parse file

        # подбор фильма не для себя
        # self.for_another = True  #bool(self.obj['for_another'])
        movies = pd.read_csv('preproc_data2.csv', index_col=0)
        data = movies.drop(['Unnamed: 0.1', 'movie_id', 'name_rus', 'name_eng'], axis=1)
        del movies
        # Слоаврь признаков (ключ - название, значение - индекс признака в векторе)
        self.enum_columns = {k: v for v, k in enumerate(data.columns)}
        self.vector = np.zeros_like(data.iloc[1])

        # if self.for_another:
        #     self.vector = np.zeros_like(data.iloc[1])
        #     self.visited_indexs = []
        #     self.rate_count = 0
        # else:
        #     user_id = int(self.obj['user_id'])
        #     #             Загружать из бд
        #     self.vector = None
        #     self.visited_indexs = None
        #     self.rate_count = 0

        # self.test_movies_id = self.obj['test_movies_id']
        # self.test_movies_rates = self.obj['test_movies_id']
        self.liked_countries = self.obj['liked_countries']
        self.disliked_countries = self.obj['disliked_countries']
        self.liked_genres = self.obj['liked_counties']
        self.disliked_genres = self.obj['disliked_counties']
        # self.movie_year = int(self.obj['movie_year'])

    def fill_by_test(self):
        """open json from user_test
        fill genres, country, and other binary features"""
        const = 10
        data_coefs = np.zeros_like(self.vector)
        result = np.zeros_like(self.vector)
        for genre in self.liked_genres:
            ind = self.enum_columns[genre]
            data_coefs[ind] = const
            result[ind] = const

        for genre in self.disliked_genres:
            ind = self.enum_columns[genre]
            data_coefs[ind] = const
            result[ind] = -const

        for country in self.liked_countries:
            ind = self.enum_columns[country]
            data_coefs[ind] = const
            result[ind] = const

        for country in self.disliked_countries:
            ind = self.enum_columns[country]
            data_coefs[ind] = const
            result[ind] = -const

        # if self.movie_year == -1:
        #     ind = self.enum_columns['movie_year']
        #     data_coefs[ind] = const
        #     result[ind] = self.movie_year
        return result, data_coefs
    #
    # def fill_by_movies(self):
    #     """open json with rated movies from user fill time, age, rating, """
    #     n = 0
    #     data = pd.read_csv('preproc_data2.csv')
    #     result = np.zeros_like(self.vector)
    #
    #     for id, rate in zip(self.test_movies_id, self.test_movies_rates):
    #         movie_vec = np.array(data.iloc[id])
    #         if rate > 3:
    #             result += (rate - 3) * movie_vec
    #             n += rate - 3
    #         else:
    #             result -= (3 - rate) * movie_vec
    #             n += 3 - rate
    #     return result / n

    def get_vector(self, full=False):
        """
        Get info from json by user
        return np.array = a*mean(movies) + b*test
        """
        if full:
            # self.vector += self.a * self.fill_by_movies()
            # self.vector += self.b * self.fill_by_test()
            # self.vector /= (self.a + self.b + self.rate_count)
            return self.vector
        else:
            return self.fill_by_test()
