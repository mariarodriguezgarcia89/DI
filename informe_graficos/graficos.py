import pandas as pd  # pandas: librería para trabajar con datos tabulares
import matplotlib.pyplot as plt  # matplotlib: librería para crear gráficos
import os
import webbrowser


'''
TAREA 1 — Carga y análisis de datos (Pandas)
'''

#leer datos desde un archivo CSV
df = pd.read_csv('datos_ventas.csv')

#mostrar por consola las primeras filas y columnas
print(df.head())

'''
TAREA 2 — Tabla resumen de datos
Debe generar:
Una tabla HTML a partir del DataFrame completo
Guardarla como:
salida/tabla_datos.html
'''

#crear tabla HTML
tabla = df.to_html()

# 5) Montar un HTML completo (con título + estilo básico)
html_completo = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>GRUPO DAM</title>
<style>
    body {{
      font-family: Arial, sans-serif;
      margin: 30px;
    }}
    h1 {{
      margin-bottom: 5px;
    }}
    p {{
      color: #555;
      margin-top: 0;
    }}
    table {{
      border-collapse: collapse;
      width: 100%;
      margin-top: 15px;
    }}
    th, td {{
      border: 1px solid #ddd;
      padding: 10px;
      text-align: left;
    }}
    th {{
      background: #f2f2f2;
    }}
    tr:nth-child(even) {{
      background: #fafafa;
    }}
</style>
</head>
<body>
<h1>Grupo DAM</h1>
<p>Generado con Pandas (sin Datapane)</p>
 
  <h2>Tabla de datos</h2>
  {tabla}
</body>
</html>
"""

# Asegurarse de que el directorio de salida existe
os.makedirs('salida', exist_ok=True)


with open('salida/tabla_datos.html', 'w', encoding='utf-8') as f:
    f.write(html_completo)      
print("Tabla HTML guardada en salida/tabla_datos.html")


'''
TAREA 3 — Cálculo de valores agregados
Debe calcular con Pandas:
Total de unidades vendidas
Total de importe
Media de unidades por venta
Comercial con mayor importe total
 NO se acepta cálculo manual
 Se evalúa:
Uso de groupby, sum, mean, sort_values
'''

total_unidades = df['Unidades'].sum()
print(f"Total de unidades vendidas: {total_unidades}")

total_importe = df['Importe'].sum()
print(f"Total de importe: {total_importe}")

media_unidades = df['Unidades'].mean()
print(f"Media de unidades por venta: {media_unidades}")

comercial_mayor_importe = df.groupby('Nombre')['Importe'].sum().sort_values(ascending=False).idxmax()
print(f"Comercial con mayor importe total: {comercial_mayor_importe}")


'''TAREA 4 — Gráficos obligatorios (Matplotlib)

Debe generar y guardar 3 gráficos:
Gráfico 1 — Líneas
Evolución de unidades vendidas por mes
Guardar como:
grafico_lineas_unidades.png
'''

# 1. Agrupa por 'Mes' y suma las Unidades e Importe
ventas_por_mes = df.groupby('Mes', observed=True)[["Unidades", "Importe"]].sum()

# 2. Crea el lienzo (tamaño 10x6 pulgadas)
plt.figure(figsize=(10, 6))

# 3. Dibuja la línea: eje X (Meses), eje Y (Unidades)
# marker='o' pone puntos en los meses, linestyle='-' une con línea continua
plt.plot(ventas_por_mes.index, ventas_por_mes['Unidades'], marker='o', linestyle='-', color='b')

# 4. Configuración estética
plt.title('Evolución de Unidades Vendidas por Mes')
plt.xlabel('Mes')
plt.ylabel('Unidades Vendidas')
plt.grid() # Añade una rejilla de fondo para facilitar la lectura

# 5. Guarda la imagen y cierra el gráfico para liberar memoria
plt.savefig('grafico_lineas_unidades.png')
plt.close()

'''
Gráfico 2 — Barras
Importe total por comercial
Guardar como:
grafico_barras_importe.png
'''

# 1. Agrupa por 'Nombre', suma el 'Importe' y ORDENA de mayor a menor
importe_por_comercial = df.groupby('Nombre')['Importe'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

# 2. Usa el método plot integrado de Pandas con kind='bar'
importe_por_comercial.plot(kind='bar', color='orange')

plt.title('Importe Total por Comercial')
plt.xlabel('Comercial')
plt.ylabel('Importe Total')
plt.grid(axis='y') # La rejilla solo aparece de forma horizontal

plt.savefig('grafico_barras_importe.png')
plt.close()

'''
Gráfico 3 — Sector
Reparto de unidades por comercial
Guardar como:
grafico_sector_unidades.png
'''

# 1. Agrupa y suma unidades por vendedor
unidades_por_comercial = df.groupby('Nombre')['Unidades'].sum()

plt.figure(figsize=(8, 8)) # Un lienzo cuadrado es mejor para círculos

# 2. kind='pie' crea el gráfico de tarta
# autopct='%1.1f%%': Calcula y muestra el porcentaje con un decimal automáticamente
# startangle=140: Gira el gráfico para una mejor perspectiva visual
unidades_por_comercial.plot(kind='pie', autopct='%1.1f%%', startangle=140)

plt.title('Reparto de Unidades por Comercial')
plt.ylabel('') # Elimina la etiqueta 'Nombre' en el eje Y que pone Pandas por defecto

plt.savefig('grafico_sector_unidades.png')
plt.close()

'''TAREA 5 — Informe final en HTML (CLAVE)
Debe crear un informe HTML final que incluya:
Título del informe
Breve texto explicativo
Los 3 gráficos
Estilo mínimo (ordenado y legible)
Archivo obligatorio:
salida/informe_final.html'''

# Crear el contenido HTML del informe final
informe_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="utf-8">  
    <title>Informe de Ventas - Grupo DAM</title>
    <style>
        :root {{
            --primary: #2c3e50;
            --secondary: #34495e;
            --accent: #3498db;
            --bg: #f4f7f6;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg);
            color: var(--primary);
            margin: 0;
            padding: 40px;
            display: flex;
            justify-content: center;
        }}

        .container {{
            max-width: 900px;
            background: white;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }}

        header {{
            border-bottom: 3px solid var(--accent);
            margin-bottom: 30px;
            padding-bottom: 10px;
        }}

        h1 {{
            margin: 0;
            color: var(--primary);
            font-size: 2.2em;
        }}

        .description {{
            color: #666;
            line-height: 1.6;
            font-size: 1.1em;
        }}

        .grafico {{
            margin: 40px 0;
            padding: 20px;
            border: 1px solid #eee;
            border-radius: 8px;
            text-align: center;
            transition: transform 0.2s;
        }}

        .grafico:hover {{
            transform: scale(1.01);
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
        }}

        h2 {{
            color: var(--secondary);
            font-size: 1.4em;
            margin-bottom: 20px;
            text-align: left;
            border-left: 5px solid var(--accent);
            padding-left: 15px;
        }}

        img {{
            max-width: 100%;
            height: auto;
            border-radius: 4px;
        }}

        footer {{
            margin-top: 50px;
            text-align: center;
            font-size: 0.9em;
            color: #999;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Informe de Ventas - Grupo DAM</h1>
            <p class="description">Análisis visual del rendimiento comercial y evolución mensual de ingresos.</p>
        </header>

        <section class="grafico">
            <h2>Evolución de Unidades Vendidas por Mes</h2>
            <img src="../grafico_lineas_unidades.png" alt="Evolución mensual">
        </section>

        <section class="grafico">
            <h2>Importe Total por Comercial</h2>
            <img src="../grafico_barras_importe.png" alt="Ranking por comercial">
        </section>

        <section class="grafico">
            <h2>Reparto de Unidades por Comercial</h2>
            <img src="../grafico_sector_unidades.png" alt="Distribución de ventas">
        </section>

        <footer>
            Generado automáticamente por el Sistema de Análisis de Datos - 2024
        </footer>
    </div>
</body> 
</html>
"""
# Guardar el informe final en un archivo HTML
with open('salida/informe_final.html', 'w', encoding='utf-8') as f:
    f.write(informe_html)
print("Informe final guardado en salida/informe_final.html")

webbrowser.open('salida/informe_final.html')


