from os import path
from Domain.dataset_excel import DataSetExcel
from Data.data_saver import DataSaver

excel_path = path.join(path.dirname(__file__),'files/productos.xlsx')


excel = DataSetExcel(excel_path)
excel.cargarDatos()

db = DataSaver()
db.guardaDataFrame(excel.datos,'productos_xlsx')