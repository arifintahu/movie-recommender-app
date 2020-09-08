from services.modules.predictrating import PredictRating
import pandas as pd 

def readFeature():
	df_features = pd.read_csv("./dataset/features.tsv", sep="\t", index_col="title")
	return df_features

def recommendMovies(user):
	df_features = readFeature()
	predict = PredictRating(df_features)
	return({
		"recommended" : list(predict.recommended_movies(user, 4.0)),
		"watched" : predict.watched_movies(user)
		})