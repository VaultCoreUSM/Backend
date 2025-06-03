from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import datetime

# Configurar Jinja2
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('plantilla\plantilla.html')
print(template)

# Datos dinámicos para la plantilla
datos = {
    "titulo": "Reporte de Productos",
    "fecha": datetime.datetime.now().strftime("%d/%m/%Y"),
    "items": [
        {"nombre": "Producto A", "precio": 150},
        {"nombre": "Producto B", "precio": 85},
        {"nombre": "Producto C", "precio": 220}
    ]
}

"""
# Renderizar HTML
html_renderizado = template.render(datos)

# Generar PDF
HTML(string=html_renderizado).write_pdf("reporte.pdf")"""