from scipy import spatial
import pandas as pd
import numpy as np

class MatrixSim:
    def __init__(self, df):
        self.df = df
        self.users = list(df.columns)
    
    def similarity(self, a, b):
        cosine = spatial.distance.cosine(self.df[a], self.df[b])
        result = 1 - cosine
        return result

    def list_similarity(self, user):
        result = []
        for col in self.users:
            sim = self.similarity(user, col)
            result.append(np.round(sim, 2))

        return result

    def matrix_similarity(self):
        result = {}
        for col in self.users:
            list_sim = self.list_similarity(col)
            result[col] = list_sim
        df_matrix = pd.DataFrame(result, index=self.users)

        return df_matrix