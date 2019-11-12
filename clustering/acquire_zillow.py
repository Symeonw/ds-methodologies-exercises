def get_zillow():
    import pandas as pd
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/zillow'
    return pd.read_sql('''select * from predictions_2017
    left join properties_2016 using(`parcelid`)
    left join airconditioningtype using (`airconditioningtypeid`)
    left join architecturalstyletype using (`architecturalstyletypeid`)
    left join heatingorsystemtype using (`heatingorsystemtypeid`)
    left join propertylandusetype using (`propertylandusetypeid`) 
    left join storytype using (`storytypeid`)
    left join typeconstructiontype using (`typeconstructiontypeid`)
    where (`latitude` is not null) and (`longitude` is not null);''',url)


def zillow_to_csv():
    return df.to_csv("zillow_data.csv")

