"""genera un archivo pdf editable / rellenable para formulario"""


from fpdf import FPDF

pdf = FPDF(format='A4')
pdf.add_page()
pdf.set_font("Helvetica", "B", 16)

# Título
pdf.cell(0, 10, "Formulario de Registro - Los Contactos de Mamá", ln=True, align="C")
pdf.ln(5)

# Sección Datos del negocio
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Datos del negocio", ln=True)
pdf.set_font("Helvetica", "", 11)

# Campos de texto
pdf.text_field(name="nombre_negocio", x=20, y=40, w=170, h=8, border=True, value="")
pdf.text(20, 38, "📌 Nombre del negocio:")

pdf.text_field(name="giro", x=20, y=55, w=170, h=8, border=True, value="")
pdf.text(20, 53, "🏷️ Giro / Categoría:")

pdf.text_field(name="direccion", x=20, y=70, w=170, h=8, border=True, value="")
pdf.text(20, 68, "📍 Dirección:")

pdf.text_field(name="telefono", x=20, y=85, w=170, h=8, border=True, value="")
pdf.text(20, 83, "📞 Teléfono:")

pdf.text_field(name="correo", x=20, y=100, w=170, h=8, border=True, value="")
pdf.text(20, 98, "📧 Correo electrónico:")

pdf.text_field(name="web_redes", x=20, y=115, w=170, h=8, border=True, value="")
pdf.text(20, 113, "🌐 Página web / Redes sociales:")

# Persona de contacto
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Persona de contacto", ln=True)
pdf.set_font("Helvetica", "", 11)

pdf.text_field(name="nombre_contacto", x=20, y=135, w=170, h=8, border=True, value="")
pdf.text(20, 133, "👤 Nombre:")

pdf.text_field(name="whatsapp_contacto", x=20, y=150, w=170, h=8, border=True, value="")
pdf.text(20, 148, "📲 WhatsApp:")

# Planes de publicación con checkbox
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Plan de publicación (selecciona uno)", ln=True)
pdf.set_font("Helvetica", "", 11)

plans = [
    ("Plan Beta Gratuito (1 mes)", 170),
    ("Plan Básico ($99/mes)", 160),
    ("Plan Destacado ($159/mes)", 150),
    ("Plan Premium ($249/mes)", 140),
]

y = 170
for plan, y_offset in plans:
    pdf.checkbox(name=plan.replace(" ", "_"), x=20, y=y, size=5)
    pdf.text(27, y+4, plan)
    y += 15

# Material para publicación
pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Material para publicación", ln=True)
pdf.set_font("Helvetica", "", 11)

materials = ["Logo (adjuntar)", "1 Foto del negocio/producto (adjuntar)", "Breve descripción (máx. 200 caracteres)"]

y = 240
for mat in materials:
    pdf.checkbox(name=mat.replace(" ", "_"), x=20, y=y, size=5)
    pdf.text(27, y+4, mat)
    y += 15

pdf.text_field(name="descripcion", x=20, y=y, w=170, h=15, border=True, value="")
y += 20

# Autorización
pdf.checkbox(name="autorizacion", x=20, y=y, size=5)
pdf.text(27, y+4, "Acepto que mi información sea publicada en la plataforma Los Contactos de Mamá y sus redes sociales.")
y += 15
pdf.text_field(name="firma_fecha", x=20, y=y, w=170, h=8, border=True, value="")
pdf.text(20, y-2, "Firma / Fecha:")

# Pie de contacto
pdf.set_font("Helvetica", "B", 12)
pdf.text(20, 290, "Contacto:")
pdf.set_font("Helvetica", "", 11)
pdf.text(20, 295, "📞 442-169-7170")
pdf.text(20, 300, "📧 info@loscontactosdemama.com.mx")

# Generar PDF
pdf.output("Formulario_Los_Contactos_de_Mama.pdf")
print("PDF rellenable generado con éxito")
