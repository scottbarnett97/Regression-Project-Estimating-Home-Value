import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import env
import os
 

####################### Imports ############################

def check_file_exists(fn, query, url):
    '''
    this function checks to see if the .csv file already exists. If yes it reads it
    '''
    if os.path.isfile(fn):
        print('csv file found and loaded\n')
        return pd.read_csv(fn, index_col=0)
    else: 
        print('creating df and exporting csv\n')
        df = pd.read_sql(query, url)
        df.to_csv(fn)
        return df 
    
def get_zillow_data():
    '''
    This function brings in the Zillow DF using mySQL from the Codeup server
    It uses the env.py file for access
    '''
    url = env.get_db_url('zillow')
    filename = 'zillow.csv'
    query = '''select 
                taxvaluedollarcnt
                , bedroomcnt
                , bathroomcnt
                , calculatedfinishedsquarefeet
                , fips
            from properties_2017
                join propertylandusetype
                    using (propertylandusetypeid)
            where propertylandusetypeid in (261, 279)
            '''
    df = check_file_exists(filename, query, url)
    return df 

    
    
    
    
""" This Function pulls in ght Telco_churn dataframe"""




def get_telco_data():
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename)
    else:
        # read the SQL query into a dataframe
        df = pd.read_sql('select * from customers join contract_types using (contract_type_id) join internet_service_types using (internet_service_type_id) join payment_types using (payment_type_id)', env.get_db_url('telco_churn'))

        # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

        # Return the dataframe to the calling code
        return df 