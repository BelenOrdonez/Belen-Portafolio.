import streamlit as st

st.set_page_config(page_title="Portafolio de Belén Ordónez")

st.title("Belén Ordónez Tumi")

imagen = Image.open("foto.jpg") 
st.image(imagen, caption="Belén Ordónez Tumi", width=300)

st.markdown("""
<p class="presentacion">
Hola! Mi nombre es <strong>Belén Ordónez Tumi</strong> y tengo 19 años. <br>
Soy estudiante de <strong>Comunicación para el Desarrollo</strong> en la 
<strong>Pontificia Universidad Católica del Perú</strong>. <br>
Actualmente me encuentro en <strong>5to ciclo</strong> de mi carrera.
</p>
""", unsafe_allow_html=True)

st.markdown("""
<p>
Además de estudiar a tiempo completo, tengo un trabajo de medio tiempo en el 
<strong>Centro de Idiomas de la Universidad del Pacífico</strong> como supervisora 
de exámenes de inglés internacionales.
</p>
""", unsafe_allow_html=True)

st.header("Habilidades")
st.write("- C1 en Inglés - Examen Aptis")

st.header("Voluntariado")
st.write('- "Hermano menor" en la ONG CESAL')

st.header("Contacto")
st.write("📱 Número: 75699653")
st.write("📧 Correo: a20230427@pucp.edu.pe")

