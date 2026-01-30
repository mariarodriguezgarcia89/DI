# ============================================================================
# SCRIPT: CREAR GRÁFICOS DE VENTAS
# Este script lee datos de ventas de un archivo CSV y genera gráficos
# ============================================================================
 
# PASO 1: IMPORTAR LIBRERÍAS
# ============================================================================
import pandas as pd  # pandas: librería para trabajar con datos tabulares
import matplotlib.pyplot as plt  # matplotlib: librería para crear gráficos
import os  # os: librería del sistema operativo (no se usa en este script)
 
 
# PASO 2: LEER EL ARCHIVO CSV
# ============================================================================
# pd.read_csv(): lee un archivo CSV (valores separados por comas)
# 'datos_ventas.csv': nombre del archivo que queremos leer
# df: variable que almacena los datos (DataFrame = tabla de datos)
df = pd.read_csv('datos_ventas.csv')
 
# DEFINE EL ORDEN DE LOS MESES
# ============================================================================
# Lista que especifica en qué orden deben aparecer los meses en el gráfico
# IMPORTANTE: Los nombres deben coincidir EXACTAMENTE con los del CSV
# En el CSV están: 'Enero', 'febrero', 'marzo' (con estas mayúsculas exactas)
orden_meses = ['Enero', 'febrero', 'marzo']
 
 
# PASO 3: CONVERTIR LA COLUMNA MES A TIPO CATEGÓRICO
# ============================================================================
# pd.Categorical(): convierte un campo a categoría (tipo especial en pandas)
# df['Mes']: accede a la columna 'Mes' del DataFrame
# categories=orden_meses: define las categorías posibles en el orden especificado
# ordered=True: indica que el orden importa (no es aleatorio)
# Resultado: La columna 'Mes' ahora respeta el orden definido en los gráficos
df['Mes'] = pd.Categorical(df['Mes'], categories=orden_meses, ordered=True)
 
 
# PASO 4: AGRUPAR DATOS POR MES Y SUMAR
# ============================================================================
# df.groupby('Mes'): agrupa los datos por la columna 'Mes'
#   - Si hay 3 filas de "Enero", las agrupa en una sola
# [["Unidades", "Importe"]]: selecciona SOLO estas 2 columnas para agrupar
#   - Ignora la columna 'Comercial'
# .sum(): suma todos los valores de cada grupo
#   - Ej: Si hay 3 "Enero" con 12, 7 y 20 unidades, suma = 39
# observed=True: solo muestra meses que tienen datos en el CSV
#   - Evita categorías vacías
# ventas_por_mes: guarda el resultado (una tabla pequeña con 3 meses)
ventas_por_mes = df.groupby('Mes', observed=True)[["Unidades", "Importe"]].sum()
 
 
# PASO 5: MOSTRAR LOS DATOS EN PANTALLA
# ============================================================================
# print(): muestra texto en la pantalla/consola
print("Ventas totales por mes:")
# Muestra la tabla con los totales agrupados
print(ventas_por_mes)
 
 
# PASO 6: CREAR EL GRÁFICO DE LÍNEAS
# ============================================================================
# ventas_por_mes.plot(): crea un gráfico a partir de los datos
# y='Unidades': gráfica SOLO la columna 'Unidades' (no incluye 'Importe')
# kind='line': tipo de gráfico = líneas (no barras, no pastel, etc.)
# marker='o': añade un punto circular ('o') en cada valor del gráfico
# title='...' : pone un título arriba del gráfico
# ax: variable que almacena el gráfico para poder modificarlo
ax = ventas_por_mes.plot(y='Unidades', kind='line', marker='o',
                         title='Unidades vendidas por mes')
 
 
# PASO 7: ETIQUETAR LOS EJES
# ============================================================================
# ax.set_xlabel(): define el texto del eje X (horizontal)
# 'Mes': nombre que aparecerá debajo del gráfico
ax.set_xlabel('Mes')
 
# ax.set_ylabel(): define el texto del eje Y (vertical)
# 'Unidades Vendidas': nombre que aparecerá a la izquierda del gráfico
ax.set_ylabel('Unidades Vendidas')
 
 
# PASO 8: GUARDAR EL GRÁFICO COMO IMAGEN
# ============================================================================
# Define dónde se guardará el archivo de imagen
ruta_lineas = "grafico_unidades_lineas.png"
 
# plt.savefig(): guarda el gráfico como archivo de imagen
# ruta_lineas: ruta y nombre del archivo donde se guarda
plt.savefig(ruta_lineas)
 
# plt.close(): cierra el gráfico en memoria (libera recursos)
# Importante: sin esto, el gráfico se quedaría en memoria
plt.close()
 
 
# PASO 9: CONFIRMAR QUE SE GUARDÓ EXITOSAMENTE
# ============================================================================
# print(): muestra un mensaje en pantalla
# f"...": formato de string con variable (f-string)
# {ruta_lineas}: inserta el contenido de la variable en el texto
print(f"Gráfico de líneas guardado en: {ruta_lineas}")