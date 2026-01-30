import pandas as pd
import webbrowser
import os   

df = pd.read_csv('datos_ventas.csv')

total_importe = df['Importe'].sum()
print(f'Total Importe: {total_importe}')

total_unidades = df['Unidades'].sum()
print(f'Total Unidades: {total_unidades}')

num_registros = len(df)
print(f'Número de registros: {num_registros}')

filtrar_por_mes = df.groupby('Mes')['Importe'].sum()
print('Importe total por mes:')
print(filtrar_por_mes) 

media_importe = df['Importe'].mean()
print(f'Media Importe: {media_importe}')

max_importe = df['Importe'].max()
print(f'Máx Importe: {max_importe}')

min_importe = df['Importe'].min()
print(f'Mín Importe: {min_importe}')

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

# 6) Guardar el HTML en un archivo
with open('informe_ventas.html', 'w', encoding='utf-8') as f:
    f.write(bloque_indicadores)  
# 7) abrir el HTML en el navegador
 
webbrowser.open('file://' + os.path.realpath('informe_ventas.html'))