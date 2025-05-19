import streamlit as st 
import pandas as pd 
import matplotlib.pyplot as plt 

# URLs de los archivos CSV (usuario: brilanag)
clientes_url = "https://raw.githubusercontent.com/brilanag/Dashboard-Chocolate-Export/main/clientes.csv"
mercados_url = "https://raw.githubusercontent.com/brilanag/Dashboard-Chocolate-Export/main/mercados.csv"
exportaciones_url = "https://raw.githubusercontent.com/brilanag/Dashboard-Chocolate-Export/main/exportaciones.csv"
barreras_url = "https://raw.githubusercontent.com/brilanag/Dashboard-Chocolate-Export/main/barreras.csv"

# Cargar datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Limpiar espacios en los nombres de columnas
clientes.columns = clientes.columns.str.strip()
mercados.columns = mercados.columns.str.strip()
exportaciones.columns = exportaciones.columns.str.strip()
barreras.columns = barreras.columns.str.strip()

# Título del Dashboard 
st.title("Dashboard Interactivo de Exportaciones de Chocolates") 

# Filtro de país 
paises = exportaciones["País"].unique() 
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises) 

# Mostrar datos de clientes 
st.subheader("Clientes") 
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado] 
st.dataframe(clientes_filtrados) 

# Mostrar datos de exportaciones 
st.subheader("Exportaciones de Chocolates") 
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado] 
fig, ax = plt.subplots() 
ax.bar(exportaciones_filtradas["Año"], exportaciones_filtradas["Exportaciones USD"], color='#2E86C1')
