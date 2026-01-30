import pandas as pd
import webbrowser
import os
 
df=pd.read_csv('datos_ventas.csv')
 
total_importe=df['Importe'].sum()
total_unidades=df['Unidades'].sum()
 
print("El importe total de las ventas es:", total_importe)
print("El total de unidades vendidas es:", total_unidades)
 
num_registros = df["Importe"].count()
media_importe = df["Importe"].mean()
min_importe = df["Importe"].min()
max_importe = df["Importe"].max()
 
 
print("Número de registros en el DataFrame:", num_registros)
print("El importe medio de las ventas es:", media_importe)
print("El importe mínimo de las ventas es:", min_importe)
print("El importe máximo de las ventas es:", max_importe)
 
ventas_por_mes = df.groupby('Comercial')['Importe'].mean()
print("Ventas media por comercial:")
print(ventas_por_mes)
 
ranking_comerciales = df.groupby('Comercial')['Importe'].sum().sort_values(ascending=False)
print("Ranking de comerciales por importe total de ventas:")
print(ranking_comerciales)
 
unidades_Enero = df[df['Mes'] == 'Enero']['Unidades'].sum()
unidades_febrero = df[df['Mes'] == 'Febrero']['Unidades'].sum()
 
diferencia_unidades = unidades_Enero - unidades_febrero
 
print("Diferencia de unidades vendidas entre Enero y Febrero:", diferencia_unidades)
 
bloque_indicadores = f"""
<div style="display:flex; gap:12px; flex-wrap:wrap; margin: 15px 0;">
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; min-width:180px;">
<b>Total Importe</b><br>{total_importe:.2f}
</div>
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; min-width:180px;">
<b>Total Unidades</b><br>{total_unidades}
</div>
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; min-width:180px;">
<b>Media Importe</b><br>{media_importe:.2f}
</div>
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; min-width:180px;">
<b>Máx Importe</b><br>{max_importe:.2f}
</div>
<div style="border:1px solid #ddd; padding:12px; border-radius:8px; min-width:180px;">
<b>Mín Importe</b><br>{min_importe:.2f}
</div>
</div>
"""
 
# 8) Montamos HTML final
html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Informe 03 - Ordenación y Filtrado</title>
<style>
    body {{ font-family: Arial; margin: 30px; }}
    table {{ border-collapse: collapse; width: 100%; margin: 15px 0; }}
    th, td {{ border: 1px solid #ddd; padding: 8px; }}
    th {{ background: #f2f2f2; }}
    h1 {{ margin-bottom: 0; }}
    p {{ color: #555; margin-top: 5px; }}
</style>
</head>
<body>
<h1>Informe 03 - Ordenación y Filtrado</h1>
<p>Tablas generadas con Pandas (HTML local)</p>
 
  <h2>1) Tabla original</h2>
  {bloque_indicadores}
 
 </body>
</html>
"""
 
# 6) Guardar el HTML en un archivo
with open('informe_ventas.html', 'w', encoding='utf-8') as f:
    f.write(html)  
# 7) abrir el HTML en el navegador
 
webbrowser.open('file://' + os.path.realpath('informe_ventas.html'))
 