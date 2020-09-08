import pandas as pd
import numpy as np

from services.modules.matrixsim import MatrixSim

class PredictRating(MatrixSim):
    def __init__(self, df):
        MatrixSim.__init__(self, df)
        self.matrix_users = self.matrix_similarity()
        
    def rating_title(self, user, title):
        total_similarity = 0
        total_rating = 0
        for col in self.users:
            if user != col:
                if self.df[col][title] > 0:
                    total_rating = total_rating + self.matrix_users[user][col]*self.df[col][title]
                    total_similarity = total_similarity + self.matrix_users[user][col]

        return np.round(total_rating/total_similarity, 2)
    
    def watched_movies(self, user):
        dict_watched = self.df[self.df[user] != 0.0][user].to_dict()
        list_watched = []
        for title in list(dict_watched):
            list_watched.append({
                'title' : title,
                'rating': dict_watched[title]
            })
            
        return list_watched
        
    def predict_ratings(self, user):
        list_titles = list(self.df[self.df[user] == 0.0].index)
        list_ratings = []
        for title in list_titles:
            rating = self.rating_title(user, title)
            list_ratings.append(rating)

        df_ratings = pd.DataFrame({
            'predict_rating' : list_ratings
        }, index=list_titles)

        return df_ratings
    
    def recommended_movies(self, user, th):
        df_ratings = self.predict_ratings(user)
        df_filter = df_ratings[df_ratings['predict_rating'] >= th]
        list_movies = df_filter.sort_values(['predict_rating'], ascending=False)
        return list(list_movies.index)