""" scrip´t para cargar archivo json que es la base de datos"""
#se abre el archivo que hay que modificar
#se sobre escibe el archivo html con la carga de datos json
#se genera un nuevo archivo html listo para insertar en github
#se protege la base de datos de anunciantes
#la base de datos siempre en mi computadora



import json
from datetime import datetime

# Archivos
plantilla_html = "escuelas.html"         # tu HTML actual (vacío de anunciantes)
json_anunciantes = "anunciantes.json"    # JSON con los anunciantes

# Nombre de salida con fecha y hora
fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
html_salida = f"escuelas_{fecha_hora}.html"

# Leer JSON
with open(json_anunciantes, "r", encoding="utf-8") as f:
    data = json.load(f)

# Leer plantilla HTML
with open(plantilla_html, "r", encoding="utf-8") as f:
    html = f.read()

# Generar contenido de anuncios
contenido = ""

# Sección Prioridad (flip cards)
contenido += '<div class="anuncio-grid anuncio-prioridad">\n'
for a in data:
    if a["categoria"] == "prioridad":
        contenido += f'''
<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <img src="{a["imagen"]}" alt="{a["nombre"]}">
      <h4>{a["nombre"]}</h4>
    </div>
    <div class="flip-card-back">
      <h4>{a["nombre"]}</h4>
      <p>{a["descripcion"]}</p>
      <p>Contacto: {a["contacto"]}</p>
      <a href="{a["enlace"]}" class="btn prioridad">Más Información</a>
    </div>
  </div>
</div>
'''
contenido += '</div>\n'

# Sección Intermedio
contenido += '<div class="anuncio-grid anuncio-intermedio">\n'
for a in data:
    if a["categoria"] == "intermedio":
        contenido += f'''
<div class="card-intermedio">
  <img src="{a["imagen"]}" alt="{a["nombre"]}">
  <div class="info">
    <h4>{a["nombre"]}</h4>
    <p>{a["descripcion"]}</p>
    <p>Contacto: {a["contacto"]}</p>
    <a href="{a["enlace"]}" class="btn intermedio">Más Información</a>
  </div>
</div>
'''
contenido += '</div>\n'

# Sección Básico
contenido += '<div class="anuncio-grid anuncio-basico">\n'
for a in data:
    if a["categoria"] == "basico":
        contenido += f'''
<div class="card-basico">
  <h4>{a["nombre"]}</h4>
  <p>{a["descripcion"]}</p>
  <p>Contacto: {a["contacto"]}</p>
  <a href="{a["enlace"]}" class="btn basico">Más Información</a>
</div>
'''
contenido += '</div>\n'

# Reemplazar contenedor vacío
html = html.replace(
    '<div class="central-section" id="anuncios-container">\n    <!-- Las cards se cargarán dinámicamente desde JSON -->\n  </div>',
    f'<div class="central-section" id="anuncios-container">\n{contenido}\n  </div>'
)

# Guardar HTML final
with open(html_salida, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Archivo generado: {html_salida}")
