#for prefect
from pathlib import Path
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from utils import location, country_to_continent
#for the transformations
import pandas as pd
import pandas_gbq
from datetime import date, datetime


@task(retries=3)
def extract_from_gcs(year: int, week: int) -> Path:
    """Download earthquake data from GCS"""
    gcs_path = f"earthquake_{year}week{week}.parquet"
    gcs_block = GcsBucket.load("dez-gcs")
    gcs_block.get_directory(from_path=gcs_path)
    return Path(gcs_path)


@task(retries=3)
def transform(path: Path) -> pd.DataFrame:
    """read the data into pandas and do some important transformations"""
    df = pd.read_parquet(path)
    _df = df.copy()
    #reset the index
    _df = _df.reset_index()
    #select just the columns of interest 
    final_columns = ['id', 'magnitude', 'date','felt', 'depth', 
    'latitude', 'longitude', 'distanceKM']
    _df = _df.loc[:, final_columns]
    #date converted to datetime 
    _df['date']= pd.to_datetime(_df['date'])
    #create new columns for year and week
    _df['year'] = pd.to_datetime(_df['date']).dt.isocalendar().year
    _df['week'] = pd.to_datetime(_df['date']).dt.isocalendar().week
    #now let's separate the colum date to keep just the date (there is no need to keep the hour)
    _df.rename(columns = {'date':'date_time'}, inplace = True)
    _df['date'] = pd.to_datetime(_df['date_time']).dt.date
    _df.drop('date_time', inplace=True, axis=1)
    #transform to datetime type again with specified format
    _df['date']= pd.to_datetime(_df['date'], format = "%Y/%m/%d")
    #use latitude and longitude to get country, city and locality
    _df['country'] = _df.apply(lambda row: location(row['latitude'], row['longitude'])[0], axis=1)
    _df['city'] = _df.apply(lambda row: location(row['latitude'], row['longitude'])[1], axis=1)
    _df['locality'] = _df.apply(lambda row: location(row['latitude'], row['longitude'])[2], axis=1)
    #some of country names were misspelled
    _df = _df.replace('Türkiye', 'Turkey')
    _df = _df.replace('Índia', 'India')
    #create continent column, using country name gets the continent
    _df['continent'] = _df.apply(lambda row: country_to_continent(row['country']), axis=1)
    #transform the data types of the table
    convert_dict = {'id': str,'magnitude': float, 'felt': int, 'depth': float, 'latitude': float, 
    'longitude': float, 'distanceKM': float,'year': int, 'week': int,
    'country': str, 'city': str, 'locality': str, 'continent': str}
    _df = _df.astype(convert_dict)
    
    return _df


@task()
def write_bq(df: pd.DataFrame) -> int:
    """Write DataFrame to BiqQuery"""

    gcp_credentials_block = GcpCredentials.load("dez-gcp-creds")

    df.to_gbq(
        destination_table="dez-project-earthquakes.bq_earthquake_data.earthquake_info",
        project_id="dez-project-earthquakes",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=5000,
        if_exists="append"
    )
    return len(df)


@flow()
def el_gcs_to_bq() -> None:
    """Main ETL flow to load data into Big Query"""
    today = date.today()
    year = today.isocalendar().year
    week = today.isocalendar().week

    path = extract_from_gcs(year, 13)
    df = transform(path)
    write_bq(df)



if __name__ == "__main__":
    el_gcs_to_bq()