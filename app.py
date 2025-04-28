import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Mi Primera App ")

# Subtítulo e imagen 1
st.subheader("Primera Sección: Un Inicio Inspirador")
st.image("imagen1.png", caption="Esta es la primera imagen", use_column_width=True)

# Subtítulo e imagen 2
st.subheader("Segunda Sección: Explorando Nuevos Horizontes")
st.image("imagen2.png", caption="Aquí exploramos algo nuevo", use_column_width=True)

# Subtítulo e imagen 3
st.subheader("Tercera Sección: Reflexión Final")
st.image("imagen3.png", caption="Una reflexión para el final", use_column_width=True)
