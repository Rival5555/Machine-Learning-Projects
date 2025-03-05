import pickle
import pandas as pd
import streamlit as st
import requests
import base64

# Function to fetch movie poster
def fetch_poster(movie_id):
    """Fetches movie poster URL from TMDb API."""
    try:
        response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=eec231d6776852b54536943b6ea5e23a&language=en-US")
        response.raise_for_status()
        data = response.json()
        poster_path = data['poster_path']
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except (requests.exceptions.RequestException, KeyError) as e:
        st.error(f"Error fetching poster for movie ID {movie_id}: {e}")
        return None

# Function to recommend movies
def recommend(movie):
    """Recommends similar movies."""
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_posters = []
        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            poster_url = fetch_poster(movie_id)
            if poster_url:
                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(poster_url)
        return recommended_movies, recommended_movies_posters
    except IndexError:
        st.error(f"Movie '{movie}' not found.")
        return [], []

# Function to display a row of movies
def display_row(title, movies):
    st.markdown(f"### {title}")
    cols = st.columns(len(movies))
    for col, movie in zip(cols, movies):
        with col:
            st.image(movie["image"], use_column_width=True)
            st.markdown(f"**{movie['title']}**")
            st.markdown(f"<span style='color:red;'>{movie['tag']}</span>", unsafe_allow_html=True)

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Set Streamlit page configuration
st.set_page_config(layout="wide", page_title="Movie-Recommender-System", page_icon="🎬", initial_sidebar_state="expanded")

# Background image
with open("sonika-agarwal-gs9dNWHfnm8-unsplash.jpg", "rb") as f:
    img_bytes = f.read()
encoded_image = base64.b64encode(img_bytes).decode()

st.markdown(
    f"""
    <style>
    body {{
        background-image: url("data:image/jpeg;base64,{encoded_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("""<h1 style="color: red;">Movie Recommendation System</h1>""", unsafe_allow_html=True)

# Movie selection
selected_movie_name = st.selectbox('Choose a movie', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(len(names))
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)

# Display genres
genres = [
    "Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama",
    "Fiction", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller",
    "War", "Western", "Zombie", "Slasher", "Musical", "Historical", "Biography",
    "Sports", "Teen", "Family", "Classic", "Adult", "Dark", "Hollywood",
    "Bollywood", "Dystopian", "Cyber-punk", "Disaster", "Spy", "Heist",
    "Detective", "Time Travel"
]

st.markdown(
    """
    <style>
        .genre-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 150px;
            height: 100px;
            background-color: #450606; 
            border-radius: 10px;
            margin: 10px; 
            transition: transform 0.4s ease-in-out; 
        }

        .genre-container:hover {
            background-color: #330404;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

num_cols = 5
all_cols = st.columns(num_cols)

for i, genre in enumerate(genres):
    col = all_cols[i % num_cols]
    with col:
        st.markdown(
            f"""
            <div class="genre-container"> 
                <h6 style="color: white;">{genre}</h6>
            </div>
            """,
            unsafe_allow_html=True,
        )


import requests

# TMDb API key
# api_key = "eec231d6776852b54536943b6ea5e23a"
#
# # Movie IDs (replace with actual movie IDs)
# movie_ids = [1156666, 1156666, 1156666]  # Example, replace with real movie IDs
#
# # Fetch movie details and construct poster URLs
# movies_with_posters = []
# base_poster_url = "https://image.tmdb.org/t/p/w500"
#
# for movie_id in movie_ids:
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         poster_path = data.get("poster_path", "")
#         title = data.get("title", "Unknown Title")
#         if poster_path:
#             poster_url = f"{base_poster_url}{poster_path}"
#             movies_with_posters.append({"title": title, "image": poster_url})
#
# # Display the movies with poster URLs
# print(movies_with_posters)



# Example movie rows for categories
example_movies = [
    {"title": "Your Fault", "movie_id": 49529, "tag": "Recently Added"},
    {"title": "Notebook", "movie_id": 49026, "tag": "Recently Added"},
    {"title": "Spy x Family", "movie_id": 49529, "tag": "Weekly"}
]

display_row("Popular Now", example_movies)
