import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv("movies_100.csv")


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]
def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]
def get_poster_from_index(index):
    return df[df.index == index]["poster"].values[0]
def get_genre_from_index(index):
    return df[df.index == index]["genres"].values[0]
def get_runtime_from_index(index):
    return df[df.index == index]["runtime"].values[0]
def get_cast_from_index(index):
    return df[df.index == index]["cast"].values[0]
def get_overview_from_index(index):
    return df[df.index == index]["overview"].values[0]
def get_director_from_index(index):
    return df[df.index == index]["director"].values[0]
def get_releasedate_from_index(index):
    return df[df.index == index]["release_date"].values[0]

def combine_features(row):
        return row["keywords"]+"" +row["cast"]+""+row["genres"]+""+row["director"]
def similar_movies(movie_input):
    features = ['keywords','cast','genres','director']
    
    for feature in features:
        df[feature] = df[feature].fillna("") #filling all NaNs with blank string
    df["combined_features"] = df.apply(combine_features,axis=1)
    cv = CountVectorizer() #creating new CountVectorizer() object
    count_matrix = cv.fit_transform(df["combined_features"]) 
    cosine_sim = cosine_similarity(count_matrix)
    movie_index = get_index_from_title(movie_input)
    similar_movies = list(enumerate(cosine_sim[movie_index])) 
    sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

    return sorted_similar_movies

