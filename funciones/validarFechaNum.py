import pandas as pd
from funciones.eliminarNulos import eliminarDatosNulos


def validarFechaNum(datos:pd.DataFrame) -> pd.DataFrame:
    for column in datos.columns:
        if column.endswith('_date'):
            datos[column] = pd.to_datetime(datos[column], errors='coerce')
        elif column.endswith('_num'):
            datos[column] = pd.to_numeric(datos[column], errors='coerce') 
            
    if datos.isnull().sum().sum() > 0 :
            print('\n'+'Errores de formato'.center(80,'*'))
            print('Se Detectaron errores de formato en la Fecha y en los numeros')
            print('Se cambiaron datos erroneos por null')
            print('¿Desea eliminar las filas nulas?')
            Entrada = input('Ingrese SI o NO: ').lower()
            while Entrada not in ['si', 'no']:
                Entrada = input('Error por favor ingrese SI o NO: ').lower()
            if Entrada == 'si':
                #llamo a la funcion de eliminar datos
                dt = eliminarDatosNulos(datos)
                datos = dt
    
    return datos
            
            
            
            