# aqui estaran las funciones claves para lograr lo automatizacion,
import jinja2 
import pdfkit
import os 
import datetime

def crear_pdf(dato):
    windows = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    ruta_actual = os.getcwd()

    ruta_salida= ruta_actual.split("\\")[:-1]
    ruta_salida.append("reporte")
    ruta_salida=(os.path.join(*ruta_salida))
    ruta_actual= ruta_actual +"\\plantilla"

    env=jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_actual))
    print(env)
    template = env.get_template("plantilla.html")
    html= template.render(dato)
    print(html)
    options = {
    'page-size': 'Letter',
    'margin-top': '0.05in',
    'margin-right': '0.05in',
    'margin-bottom': '0.05in',
    'margin-left': '0.05in',
    'encoding': 'UTF-8',
    }

    config = pdfkit.configuration(wkhtmltopdf=windows)

    salida_pdf = "reporte.pdf"
    print(salida_pdf)
    pdfkit.from_string(html,salida_pdf,configuration=config)
    #ruta_salida

