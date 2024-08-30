import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('ANUNCIOS DE COCHES A LA VENTA')
hist_button = st.button('Construir histograma')
if hist_button:
    st.write('Histograma de venta de coches por kilometraje')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    
    st.write('Grafico de dispersion por model_año')
    
    
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="model_year")
    
    st.plotly_chart(fig_scatter, use_container_width=True)