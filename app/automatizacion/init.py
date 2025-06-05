# aqui estaran las funciones claves para lograr lo automatizacion,
import jinja2 
import pdfkit
import os 
from datetime import datetime, date, time, timedelta 
from datetime import datetime, timedelta

#pdf
def crear_pdf(dato, entrada="reporte"):
    try:
        windows = "/usr/bin/wkhtmltopdf"
        ruta_actual = os.getcwd()

        ruta_salida= ruta_actual.split("\\")[:-1]
        ruta_salida.append("reporte")
        ruta_salida=(os.path.join(*ruta_salida))

        ruta_base = os.getcwd()
        ruta_plantilla = os.path.join(ruta_base, "app", "automatizacion", "plantilla")
        ruta_salida = os.path.join(ruta_base, "app", "automatizacion","reporte",f"{entrada}.pdf")

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
        return [True,ruta_salida]
    except  Exception as e:
        return [False,e]
        

#Fechas
def fecha_meses_atras(cantidad):
    try:
        fecha_actual = datetime.now()
        # Aproximación simple (no exacta para meses)
        fecha_pasada = fecha_actual - timedelta(days=30*cantidad)
        
        return (
            fecha_pasada.day,
            fecha_pasada.month,
            fecha_pasada.strftime("%B"),
            fecha_pasada.year
        )
    except Exception as e:
        print(f"Error: {e}")
        return None, None, None, None
    
def fecha_creacion(dia,mes,anio):
    creacion= date(anio, mes, dia)
    return creacion


def fecha_masdias(fecha,dias): # fecha es una variable date, si no se tiene enviar a una funcion auxiliar
    fecha_nueva= fecha +timedelta(days=dias)
    return fecha_nueva

def fecha_tupla(fecha,modo=0):
    print(fecha)
    fecha=str(fecha)
    fecha=fecha.split(" ")
    partes = fecha[0].strip().split("-")
    print(partes)
    print(not(modo))
    if not(modo):
        return (partes[2],partes[1],partes[0])
    else:
        hora=fecha[1].split(":")
        print(hora)
        return (partes[2],partes[1],partes[0],hora[0],hora[1],hora[2] )




#Archivos
#se suguiere usar usar la variable archivador para manejar los archivis

# archivo_crear_carpeta(ruta, nombre)
def archivo_crear_carpeta(ruta, nombre):
    nueva_ruta = os.path.join(ruta, nombre)
    try:
        os.makedirs(nueva_ruta, exist_ok=True)
        return True
    except Exception as e:
        return False

# archivo_borrar_archivo()
import os

def archivo_borrar_archivo(ruta):
    try:
        if os.path.isfile(ruta):
            os.remove(ruta)
            return True
        else:
            print("No es un archivo o no existe.")
    except Exception as e:
        return False

# archivo_buscar()

def archivo_buscar(ruta):
    return os.path.exists(ruta)
#+






#