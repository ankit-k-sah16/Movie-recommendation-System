import streamlit as st
import pickle 
import pandas as pd 
import requests

movies_dict=pickle.load(open('movies_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movies_dict)

def fetch_poster(movie_id):
    response=requests.get("https://api.themoviedb.org/3/movie/{}?api_key=471d00bd6fdec5db1d376bde431e230b&language=en-US".format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies_names = []
    recommended_movies_poster = []
    for i in distances[1:6]:  # Skip the input movie itself
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_names, recommended_movies_poster




st.title('Movie Recommender System')
movie_list=movies['title'].values


selected_movie_name=st.selectbox('Type or select a movie from the dropdown ',movie_list)

if st.button(" Show Recommendation "):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

