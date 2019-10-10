import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from env import host, user, password
url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
df = pd.read_sql('''select customer_id, monthly_charges, tenure, total_charges from customers e
join contract_types as c on e.contract_type_id = c.contract_type_id where contract_type = "Two year" and total_charges is not null
group by customer_id;''' ,url)
df.describe()

def clean_telco(df):
    df = df[['customer_id', 'total_charges', "monthly_charges", "tenure"]]
    df.total_charges = df.total_charges.str.strip().replace('', np.nan).astype(float)
    df = df.dropna()
    return  df
def wrangle_telco():
    import pandas as pd
    from env import host, user, password
    df = pd.read_sql('''select customer_id, monthly_charges, tenure, total_charges from customers e
    join contract_types as c on e.contract_type_id = c.contract_type_id where contract_type = "Two year" and total_charges is not null
    group by customer_id;''' ,url)
    df = clean_telco(df)
    return df

wrangle_telco()