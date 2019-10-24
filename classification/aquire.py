import pandas as pd
from env import host, user, password 
def get_titanic_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/titanic_db'
    df = pd.read_sql('''select * from passengers''' ,url)
    return df
def get_iris_data():
    url = f'mysql+pymysql://{user}:{password}@{host}/iris_db'
    df = pd.read_sql('''select species.species_id, species_name, sepal_length, sepal_width, petal_length, petal_width from species join measurements as m on m.species_id = species.species_id;''' ,url)
    df = df[["species_id", "species_name", "sepal_length", "sepal_width", "petal_length", "petal_width"]]
    return df
