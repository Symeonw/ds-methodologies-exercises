def get_mall():
    import pandas as pd 
    from env import user, password, host
    url = f'mysql+pymysql://{user}:{password}@{host}/mall_customers'
    return pd.read_sql("""select * from customers""",url)

