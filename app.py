import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Mi Primera App ")

# Subtítulo e imagen 1
st.subheader("Primera Sección: Un Inicio Inspirador")
st.image("naruto.jpg", caption="Esta es la primera imagen", use_container_width=True)

# Subtítulo e imagen 2
st.subheader("Segunda Sección: Explorando Nuevos Horizontes")
st.image("broadway.jpg", caption="Aquí exploramos algo nuevo", use_container_width=True)


