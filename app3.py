import streamlit as st

# Function to display a row of movies
def display_row(title, movies):
    st.markdown(f"### {title}")
    cols = st.columns(len(movies))
    for col, movie in zip(cols, movies):
        with col:
            st.image(movie["image"], use_column_width=True)
            st.markdown(f"**{movie['title']}**")
            st.markdown(f"<span style='color:red;'>{movie['tag']}</span>", unsafe_allow_html=True)

# Movie data
your_next_watch = [
    {"title": "Love Yatri", "image": "https://via.placeholder.com/150", "tag": "Recently added"},
    {"title": "Notebook", "image": "https://via.placeholder.com/150", "tag": "Recently added"},
    {"title": "Rising Impact", "image": "https://via.placeholder.com/150", "tag": "Recently added"},
    {"title": "Laapataa Ladies", "image": "https://via.placeholder.com/150", "tag": "Recently added"},
    {"title": "When the Phone Rings", "image": "https://via.placeholder.com/150", "tag": "New Episode"},
    {"title": "Spy x Family", "image": "https://via.placeholder.com/150", "tag": "Weekly"},
]

filmfare_winners = [
    {"title": "Bajrangi Bhaijaan", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
    {"title": "Veere di Wedding", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
    {"title": "Aranyak", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
    {"title": "Bharat", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
    {"title": "Kathal", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
    {"title": "Mai: A Mother's Rage", "image": "https://via.placeholder.com/150", "tag": "Recently Added"},
]

# Display rows
display_row("Your Next Watch", your_next_watch)
display_row("Filmfare Award Winners & Nominees", filmfare_winners)
