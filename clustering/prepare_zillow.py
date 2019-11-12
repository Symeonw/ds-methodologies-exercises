from sum import nulls_by_col

def handle_missing_values(df, prop_required_column = .5, prop_required_row = .60):
    threshold = int(round(prop_required_column*len(df.index),0))
    df.dropna(axis=1, thresh=threshold, inplace=True)
    threshold = int(round(prop_required_row*len(df.columns),0))
    df.dropna(axis=0, thresh=threshold, inplace=True)
    return df

def zillow_single_unit(df):
    criteria_1=df.propertylandusedesc=='Single Family Residential'
    criteria_2=df.calculatedfinishedsquarefeet>500
    df=df[(criteria_1) & (criteria_2)]
    return df
