import pandas as pd
import streamlit as st
import pickle
import requests

# from bokeh.sampledata.movies_data import movie_path

def fetch_poster(movie_id):
        try:
            url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=39e160887458ed2247a4d4b68b2d2b70&language=en-US"
            response = requests.get(url)
            data = response.json()

            if "poster_path" in data and data["poster_path"] is not None:
                return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
            else:
                return "https://static.streamlit.io/examples/cat.jpg"

        except Exception as e:
            print("Error fetching poster:", e)
            return "https://static.streamlit.io/examples/cat.jpg"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies =[]
    recommended_movies_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # movie_id =i[0]

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,  recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'What are you looking for today',
    movies['title'].values
)

if st.button('Recommend'):
   names,posters = recommend(selected_movie_name)
   col1 , col2 , col3, col4, col5 = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])
   with col2:
       st.text(names[1])
       st.image(posters[1])
   with col3:
       st.text(names[2])
       st.image(posters[2])
   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])