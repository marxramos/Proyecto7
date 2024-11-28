import pandas as pd
import streamlit as st
import plotly.express as px  # Nota: no es "plotly_express"

# Leer los datos
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir histograma')
dist_button = st.button('construir una dispersion')

#Encabezado
st.header('Grafico de Automovil')

# Al hacer clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dist_button:
    st.write('crecion de un grafico de dispersion para el conjunto de datos de anuncions de venta de coches')

    fig = px.scatter(car_data, x ='model_year', y ='price')
    st.plotly_chart(fig, use_container_width=True)
