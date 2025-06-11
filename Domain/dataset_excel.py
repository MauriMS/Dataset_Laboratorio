import pandas as pd
from Domain.dataset import DataSet

class DataSetExcel(DataSet):
    def __init__(self, archivo):
        super().__init__(archivo)
        
    def cargarDatos(self):
        try:
            df = pd.read_excel(self.archivo)
            self.datos = df
            print('Excel Cargado')
            self.validarDatos()
            print('Datos validados')
            
        except Exception as e:
            print(f'Error al cargar los datos en excel: {e}')