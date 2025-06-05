from datetime import datetime, date, time, timedelta 

from datetime import datetime, timedelta

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



fecha=fecha_creacion(5,6,2025)



print(fecha_masdias(fecha,7))
hoy = datetime.now()
print(hoy)
print(fecha_tupla(hoy,1))
