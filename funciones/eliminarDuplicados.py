import pandas as pd


def eliminarDatosDuplicados(datos:pd.DataFrame) -> pd.DataFrame:
    if not isinstance(datos,pd.DataFrame):
        raise ValueError('Error el dato debe ser un DataFrame de pandas')
    return datos.drop_duplicates()