import stats
import string
t = str.maketrans(dict.fromkeys(string.punctuation))

def clean_data(df):
    df = df.translate(t)

def convert_data(df_column, convert_type, convert_nans):
    

