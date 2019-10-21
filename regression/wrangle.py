import stats
from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
def clean_telco():
    df = pd.read_sql('''select customer_id, monthly_charges, tenure, total_charges from customers e
    join contract_types as c on e.contract_type_id = c.contract_type_id where contract_type = "Two year" and total_charges is not null
    group by customer_id;''' ,url)
    df = df[['customer_id', 'total_charges', "monthly_charges", "tenure"]]
    df.assign(total_charges = lambda x: x.total_charges.str.strip().replace('',np.nan).convert_objects(convert_numeric=True))
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors= "coerce").dropna()
    return df
def wrangle_telco():
    import pandas as pd
    df = clean_telco()
    return df
