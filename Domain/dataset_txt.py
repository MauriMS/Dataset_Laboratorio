import pandas as pd
from Domain.dataset import DataSet

class DataSetTXT(DataSet):
    def __init__(self, archivo):
        super().__init__(archivo)
        
    def cargarDatos(self):
        try:
            df = pd.read_csv(self.archivo, sep=';')
            self.datos = df
            print('TXT cargado')
            if self.validarDatos():
                print('Datos validados')
            
            
        
        except Exception as e:
            print(f'Error al cargar el archivo .txt: {e}')