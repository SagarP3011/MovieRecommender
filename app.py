import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+ data['poster_path']

#movies_list= pickle.load(open('movies.pkl','rb')) # this gives error in loading pandas df from pkl file thus using dictionary one
movie_dict= pickle.load(open('movies_dict.pkl','rb'))
similarity= pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

def recommend(movie):
    movie_index= movies[movies['title']== movie].index[0] # Step 1
    distances = similarity[movie_index] # Step2
    movie_list = sorted(list(enumerate(distances)),reverse=True , key=lambda x:x[1])[1:6] #Step 3 and 4
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id    
        recommended_movies.append(movies.iloc[i[0]].title) # to get names of movie recommended
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters

selected_movie_name = st.selectbox(
    'Movie Liked',
    movies['title'].values
)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5 = st.columns(5)

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