import streamlit as st
from PIL import Image

# Título de la aplicación
st.title("Mi Primera Aplicacion con las cosas que me gustan")
st.write("Solo para poner de ejemplo de muchas de las cosas que me gusto hice esta aplicacion")

# Primera sección con subtítulo e imagen
st.subheader("Primera Sección: El anime")
image1 = Image.open('naruto.jpg')  
st.image(image1, caption="Aqui puse una imagen de uno de mis animes favoritos", width=600)

page_style = """
<style>
/* Fondo principal */
[data-testid="stAppViewContainer"] {
    background-color: #000b3c;
}

/* Color de todos los textos */
[data-testid="stMarkdownContainer"] {
    color: #edeff7;
}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

# Segunda sección con subtítulo e imagen
st.subheader("Segunda Sección: Los musicales")
image2 = Image.open('broadway.jpg')  
st.image(image2, caption="Amo los musicales especialmente los de broadway", width=600)



