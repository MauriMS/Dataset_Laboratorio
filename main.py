from os import path
from Domain.dataset_excel import DataSetExcel
from Data.data_saver import DataSaver
from Domain.dataset_txt import DataSetTXT

excel_path = path.join(path.dirname(__file__),'files/productos.xlsx')
txt_path = path.join(path.dirname(__file__),'files/titanic.txt')

# txt = DataSetTXT(txt_path)
# txt.cargarDatos()

excel = DataSetExcel(excel_path)
excel.cargarDatos()

db = DataSaver()
db.guardaDataFrame(excel.datos,'productos_xlsx')
#db.guardaDataFrame(txt.datos,'titanic_txt')