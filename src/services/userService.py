import pandas as pd 

def readUser():
	df_user = pd.read_csv("./dataset/users.tsv", sep="\t", names=["users"])
	return list(df_user["users"])