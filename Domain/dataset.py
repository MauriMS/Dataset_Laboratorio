from abc import ABC, abstractmethod
from funciones.eliminarDuplicados import eliminarDatosDuplicados
from funciones.eliminarNulos import eliminarDatosNulos

class DataSet(ABC):
    def __init__(self,archivo):
        self.__archivo = archivo
        self.__datos = None
        
    @property
    def archivo(self):
        return self.__archivo
    
    @archivo.setter
    def archivo(sefl,archivo):
        sefl.__archivo = archivo
        
    @property
    def datos(self):
        return self.__datos
    
    @datos.setter
    def datos(self,datos):
        self.__datos = datos
    
    @abstractmethod
    def cargarDatos(self):
        pass
    
    def validarDatos(self):
        #Verifico si los datos estan cargados
        if self.__datos is None:
            raise ValueError('Datos no cargados')
        
        #Verifico si los datos son nulos y si lo son, pregunto si los quiere eliminar
        if self.datos.isnull().sum().sum() > 0 :
            print('Datos faltantes detectados\n')
            print('¿Desea eliminar las filas nulas?')
            Entrada = input('Ingrese SI o NO :').lower()
            while Entrada not in ['si', 'no']:
                Entrada = input('Error por favor ingrese SI o NO: ').lower()
            if Entrada == 'si':
                #llamo a la funcion de eliminar datos
                eliminarDatosNulos(self.datos)
        
        #Verifico si hay filas Duplicadas y si las hay, pregunto si las quiere eliminar
        if self.datos.duplicated().sum() > 0:
            print('Filas duplicadas detectadas')
            print('¿Desea eliminar las filas duplicadas?')
            Entrada = input('Ingrese SI o NO :').lower()
            while Entrada not in ['si', 'no']:
                Entrada = input('Error por favor ingrese SI o NO: ').lower()
            if Entrada == 'si':
                #llamo a la funcion de eliminar datos
                eliminarDatosDuplicados(self.datos)
                
        # Validar fecha y si es numerico
        # for column in self.datos.columns:
        #     if column.endswith('_date'):
        #         self.datos[column] = pd.to_datetime(self.datos[column], errors='coerce')
        #     elif column.endswith('_num'):
        #         self.datos[column] = pd.to_numeric(self.datos[column], errors='coerce') 
        #return True
    
    
    def transformarDatos(self):
        pass