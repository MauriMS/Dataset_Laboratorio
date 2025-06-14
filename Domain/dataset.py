from abc import ABC, abstractmethod
from funciones.eliminarDuplicados import eliminarDatosDuplicados
from funciones.eliminarNulos import eliminarDatosNulos
from funciones.validarFechaNum import validarFechaNum

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
            print('Datos faltantes detectados')
            print('¿Desea eliminar las filas nulas?')
            Entrada = input('Ingrese SI o NO: ').lower()
            while Entrada not in ['si', 'no']:
                Entrada = input('Error por favor ingrese SI o NO: ').lower()
            if Entrada == 'si':
                #llamo a la funcion de eliminar datos
                dt = eliminarDatosNulos(self.datos)
                self.datos = dt
        
        #Verifico si hay filas Duplicadas y si las hay, pregunto si las quiere eliminar
        if self.datos.duplicated().sum() > 0:
            print('\nFilas duplicadas detectadas')
            print('¿Desea eliminar las filas duplicadas?')
            Entrada = input('Ingrese SI o NO: ').lower()
            while Entrada not in ['si', 'no']:
                Entrada = input('Error por favor ingrese SI o NO: ').lower()
            if Entrada == 'si':
                #llamo a la funcion de eliminar datos
                dt = eliminarDatosDuplicados(self.datos)
                self.datos = dt
                
        #Validar fecha y si es numerico
        dt = validarFechaNum(self.datos)
        self.datos = dt
        return True
