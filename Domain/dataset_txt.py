import pandas as pd
from Domain.dataset import DataSet

class DataSetTXT(DataSet):
    def __init__(self, archivo):
        super().__init__(archivo)
        
    def cargarDatos(self):
        try:
            df = pd.read_csv(self.archivo, sep=';')
            self.datos = df
            print('\n'+'TXT cargado'.center(80,'-')+'\n')
            if self.validarDatos():
                print('Datos validados\n')
            
            
        
        except Exception as e:
            print(f'Error al cargar el archivo .txt: {e}')