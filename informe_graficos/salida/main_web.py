import pandas as pd
import webbrowser
from pathlib import Path

# 1) URL de la web (Wikipedia: sencillos más vendidos)
URL = "https://www.basketball-reference.com/leagues/NBA_2024.html"

# 2) Leer TODAS las tablas HTML de la web
tablas = pd.read_html(URL)

print(f" Tablas encontradas: {len(tablas)}")

# 3) Elegir la tabla 0 (la primera)
df = tablas[0]

# 4) Mostrar por consola (para comprobar)
print("=== PRIMERAS FILAS DE LA TABLA ===")
print(df.head(10))

# 5) Generar HTML SOLO con 10 filas
html = df.head(10).to_html(index=False)

#Ordenar por la columna de Loses (derrotas)
df_sorted = df.sort_values(by='L', ascending=False)
html += "\n<h2>Tabla ordenada por Derrotas (Loses)</h2>\n"
html += df_sorted.head(10).to_html(index=False)

#Filtrar filas que contengan una palabra en “Bulls"
df_filtered = df[df['Eastern Conference'].str.contains('Bulls', na=False)]
html += "\n<h2>Filtrado de equipos que contienen 'Bulls'</h2>"
html += df_filtered.to_html(index=False)

#Guardar también el CSV local
csv_salida = Path("nba_2024_teams.csv")
df.to_csv(csv_salida, index=False)

#Comprobar si hay valores nulos
nulos = df.isnull().sum().sum()
html += f"\n<h2>Número total de valores nulos en la tabla: {nulos}</h2>\n"

# 6) Guardar informe HTML
salida = Path("informe_web.html")
salida.write_text(html, encoding="utf-8")
print(f"\n Informe guardado en: {salida.resolve()}")

# 7) Abrir en navegador
webbrowser.open(salida.resolve().as_uri())
