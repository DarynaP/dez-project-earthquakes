#libraries
import pandas as pd
from prefect import flow, task
from prefect_gcp import GcpCredentials
from datetime import date
import requests



@task(retries=3)
def fetch_data(url: str) -> dict:
    '''
    Get the data from the api and return it as dict format
    
    headers = {"X-RapidAPI-Key": "6d15e169famsh14ec07b2b3145d2p1f0eddjsnf6010e34a528",
    "X-RapidAPI-Host": "everyearthquake.p.rapidapi.com"} #personal identification 
    response_dict = requests.get(url, headers=headers).json()
    '''
    headers = {"X-RapidAPI-Key": "6d15e169famsh14ec07b2b3145d2p1f0eddjsnf6010e34a528",
    "X-RapidAPI-Host": "everyearthquake.p.rapidapi.com"}

    response_dict = requests.get(url, headers=headers).json()
    
    return response_dict

@task()
def data_to_df(response_dict: dict) -> pd.DataFrame:
    '''
    Selects from the dict values of key 'data' (is were the information of each earthquake is stored) and 
    stores as list of dicts
    Selects just the importants columns (in this case keys)
    Transform and append each dict as row in dataframe
    '''

    list_dicts_data = response_dict['data']
    keys_list = ['id', 'magnitude', 'type', 'title', 'date', 'time', 'updated', 
    'felt', 'cdi', 'mmi', 'alert', 'status', 'tsunami', 'sig', 'net', 'code', 
    'ids', 'sources', 'nst', 'dmin', 'rms', 'gap', 'magType', 'geometryType', 
    'depth', 'latitude', 'longitude', 'place', 'distanceKM', 'placeOnly', 
    'location', 'continent', 'country', 'subnational', 'city', 'locality', 
    'postcode', 'what3words', 'timezone']

    df =  pd.DataFrame()
    for earthquake in list_dicts_data:
        earthquake_dict = {key: earthquake[key] for key in keys_list}
        earthquake_df = pd.DataFrame(earthquake_dict, index=[0]).set_index('id')
        df = pd.concat([df, earthquake_df], axis=0)
    return df

@task()
def write_gcs(df: pd.DataFrame) -> None:
    '''
    Writes the dataframe into GCS Bucket as parquet file
    The name of the file changes every week

    '''
    today = date.today()
    year = today.isocalendar().year
    week = today.isocalendar().week
    file_name = f'earthquake_{year}week{week}'
    
    gcp_credentials = GcpCredentials.load("dez-gcp-creds")
    credentials = gcp_credentials.get_credentials_from_service_account()
    
    df.to_parquet(f'gs://earthquake-data-dez/{file_name}.parquet', 
    storage_options={'token': credentials})
    return

    


@flow()
def etl_api_to_gcs()-> None:
    '''Main flow to fetch data, transform to datafarme and ingest into GCS bucket'''
    
    url = "https://everyearthquake.p.rapidapi.com/all_week.json"

    response_dict = fetch_data(url)
    df = data_to_df(response_dict)
    write_gcs(df)



if __name__ == "__main__":
    etl_api_to_gcs()



