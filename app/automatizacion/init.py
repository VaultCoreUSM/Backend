# aqui estaran las funciones claves para lograr lo automatizacion,
import jinja2 
import pdfkit
import os 
import datetime

def crear_pdf(dato):
    try:
        windows = "/usr/bin/wkhtmltopdf"
        ruta_actual = os.getcwd()

        ruta_salida= ruta_actual.split("\\")[:-1]
        ruta_salida.append("reporte")
        ruta_salida=(os.path.join(*ruta_salida))

        ruta_base = os.getcwd()
        ruta_plantilla = os.path.join(ruta_base, "app", "automatizacion", "plantilla")
        ruta_salida = os.path.join(ruta_base, "app", "automatizacion","reporte","reporte.pdf")

        env=jinja2.Environment(loader=jinja2.FileSystemLoader(ruta_plantilla))
        print(env)
        template = env.get_template("/plantilla.html")
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


        pdfkit.from_string(html,ruta_salida,configuration=config)
        return [True,""]
    except  Exception as e:
        return [False,e]
        

#Fechas
