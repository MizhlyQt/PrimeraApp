import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Mi Aplicación con Subtítulos e Imágenes")

# Primera sección con subtítulo e imagen
st.subheader("Primera Sección: Un Inicio Inspirador")
image1 = Image.open('naruto.jpg')  # Cambia 'imagen1.png' por el nombre de tu archivo
st.image(image1, caption="Esta es la primera imagen", width=600)

# Segunda sección con subtítulo e imagen
st.subheader("Segunda Sección: Explorando Nuevos Horizontes")
image2 = Image.open('broadway.jpg')  # Cambia 'imagen2.png' por el nombre de tu archivo
st.image(image2, caption="Aquí exploramos algo nuevo", width=600)



