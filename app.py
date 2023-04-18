import requests
import streamlit as st
import pickle
import pandas as pd
import time


# def fetch_poster(movie_id):
#     response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
#     data= response.json()
#
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend(book):
    book_index = books[books['b_title'] == book].index[0]
    distances = similarity[book_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:21]

    recommended_book = []
    # book_author=[]
    # recommended_movies_poster=[]

    for i in movies_list:
        ISBN = books.iloc[i[0]].ISBN
        recommended_book.append(books.iloc[i[0]].b_info)
        # book_author.append(books.iloc[i[0]].b_author)
        # fetch poster from api
        # recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_book


books_dict = pickle.load(open('book_dictsss.pkl', 'rb'))
books = pd.DataFrame(books_dict)

similarity = pickle.load(open('booksss_similarity.pkl', 'rb'))

st.title('Book Recommender📖')
st.snow()
selected_book_name = st.selectbox(
    'Enter the name of the book',
    books['b_title'].values)

if st.button('Recommend'):
    with st.spinner('Wait for it...'):
        time.sleep(2)
    st.success('Done!')

    names = recommend(selected_book_name)
    # author = recommend(selected_book_name)

    for i in range(10):
        st.header(names[i])
        # st.markdown(author[i])

