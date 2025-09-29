import pandas as pd
import urllib.parse

# Configuración
codigo_pais = "52"  # México
mensaje = """¡Hola! 👋
Soy Gilberto Morelos de Los Contactos de Mamá 🏡.

📢 Durante nuestro periodo de lanzamiento, las escuelas pueden aparecer GRATIS
en nuestro directorio de Querétaro y San Juan del Río, mándanos tus datos.
Es un placer para nosotros contar contigo.

🔗 Más info: www.loscontactosdemama.com.mx
"""

# Cargar lista de números
df = pd.read_csv("numeros.csv")  # columna "telefono"

# Generar enlaces para WhatsApp Web
enlaces = []
for numero in df['telefono']:
    texto_codificado = urllib.parse.quote(mensaje)
    enlace = f"https://web.whatsapp.com/send?phone={codigo_pais}{numero}&text={texto_codificado}"
    enlaces.append(enlace)

# Guardar enlaces en CSV
df['enlace_whatsapp_web'] = enlaces
df.to_csv("enlaces_whatsapp_web.csv", index=False)

print("Enlaces generados y guardados en 'enlaces_whatsapp_web.csv'.")

