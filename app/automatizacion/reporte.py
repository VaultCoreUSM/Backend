from app.automatizacion.init import *

def generar():
    datos = {
        "titulo": "Reporte de Productos",
        "fecha": datetime.datetime.now().strftime("%d/%m/%Y"),
        "items": [
            {"nombre": "Producto A", "precio": 150},
            {"nombre": "Producto B", "precio": 85},
            {"nombre": "Producto C", "precio": 220}
        ]
    }
    valor =crear_pdf(datos)
    print(valor)
    return valor

