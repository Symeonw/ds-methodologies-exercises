import pandas as pd
import env


def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_zillow_data():
    query = '''
    select * from predictions_2016
        left join properties_2017 using(parcelid)
        where latitude IS not null AND longitude is not null;
    '''
    df = pd.DataFrame(pd.read_sql(query, get_connection('zillow')))
    return df

def get_iris_data():
    query = '''
    SELECT petal_length, petal_width, sepal_length, sepal_width, species_id, species_name
    FROM measurements m
    JOIN species s USING(species_id)
    '''
    return pd.read_sql(query, get_connection('iris_db'))

def get_mallcustomer_data():
    df = pd.read_sql('SELECT * FROM customers;', get_connection('mall_customers'))
    return df.set_index('customer_id')

