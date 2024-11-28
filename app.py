import pandas as pd
import streamlit as st
import plotly.express as px  # Nota: no es "plotly_express"

# Leer los datos
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir histograma')

# Al hacer clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
