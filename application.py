import streamlit as st
import pickle
import pandas as pd
import requests

# Load data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Fetch movie poster using TMDB API
@st.cache_data
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=471d00bd6fdec5db1d376bde431e230b&language=en-US"
        )
        response.raise_for_status()
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data.get('poster_path', '')
    except:
        return "https://via.placeholder.com/500x750.png?text=No+Image"

# Recommend movies
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )
    
    recommended_movies_names = []
    recommended_movies_posters = []
    for i in distances[1:6]:  # Top 5 recommendations excluding the selected movie
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    
    return recommended_movies_names, recommended_movies_posters

# Streamlit UI
st.title('🎥 Movie Recommender System')
st.markdown("### Get recommendations based on your favorite movies 🎬")
st.write("")  # spacer

movie_list = movies['title'].values
selected_movie_name = st.selectbox('Type or select a movie from the dropdown:', movie_list)

if st.button("Show Recommendation"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    cols = st.columns(5)
    for idx in range(5):
        with cols[idx]:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
