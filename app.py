import streamlit as st
import pickle
import pandas as pd
import requests
#st.run("app.py")
st.title('Movie Recommendation System')
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies_list = movies_dict['title'].values()
movies_data = pd.DataFrame(movies_dict)


def fetch_poster(movie_id):
    response = requests.get(
        "https://api.themoviedb.org/3/movie/{id}?api_key=c3010d30a61c3a1081401f17a74d5a90&language=en-US".format(
            id=movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies_data[movies_data['title'] == movie].index[0]
    recommended_object = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]

    recommended_indexes = [i[0] for i in recommended_object]
    movie_title = list(movies_data.loc[recommended_indexes, 'title'])
    movie_id = list(movies_data.loc[recommended_indexes, 'id'])
    list_of_tuples = list(zip(movie_id, movie_title))

    return list_of_tuples


selected_movie = st.selectbox(
    'Select your favourite movie',
    movies_list)

if st.button('Recommend'):
    recommended_movies = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5, gap="small")
    columns = [col1, col2, col3, col4, col5]
    i = 0
    for movie in recommended_movies:
        with columns[i]:
            st.text(movie[1])
            st.image(fetch_poster(movie[0]))
        i = i + 1

