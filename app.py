import pandas as pd
import streamlit as st
import plotly.express as px  # Nota: no es "plotly_express"

# Leer los datos
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir un gráfico histograma')
dist_button = st.button('construir un gráfico dispersión')

#Encabezado
st.header('Graficos a prueba: Automovil')

# Al hacer clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if dist_button:
    st.write('Crecion de un gráfico de dispersión para el conjunto de datos de venta de coches')

    fig = px.scatter(car_data, x ='model_year', y ='price')
    st.plotly_chart(fig, use_container_width=True)
