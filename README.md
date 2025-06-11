# Dataset_Laboratorio

# IMPORTANTE
1)Para descargar las dependencias:    pip install -r requirements.txt

2)En la carpeta Data Modificar el .env para poder conectarse a la base de datos.
 
3)Yo utilice PostgreSQL asi que hay que modificar la URL en data_saver.py    . Yo deje una linea para MYSQL comentada(No se si funciona), utilizar esa y comentar la de PostgreSQL.




# ACLARACIONES
Mi dataset esta configurado que si a una fila le falta algun valor elimina toda la fila. Y si hay valores duplicados tambien se puede eliminar pero le di libertad al usuario para elegir si quiere guardar con datos nulos y duplicados en la base de datos.

