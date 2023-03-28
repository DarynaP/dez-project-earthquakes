from pathlib import Path
import pandas as pd
import pandas_gbq
from datetime import date, datetime
from prefect import flow, task
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials



@task(retries=3)
def extract_from_gcs(year: int, week: int) -> Path:
    """Download earthquake data from GCS"""
    gcs_path = f"earthquake_{year}week{week}.parquet"
    gcs_block = GcsBucket.load("dez-gcs")
    gcs_block.get_directory(from_path=gcs_path)
    return Path(gcs_path)


@task()
def transform(path: Path) -> pd.DataFrame:
    """read the data into pandas and do some important transformations"""
    df = pd.read_parquet(path)
    _df = df.copy()
    #reset the index
    _df = _df.reset_index()
    #select just the columns of interest 
    final_columns = ['id', 'magnitude', 'type', 'date','felt', 'cdi', 'mmi', 'alert', 'status', 
    'tsunami', 'sig', 'ids','gap', 'depth', 'latitude', 'longitude', 'distanceKM', 'location', 
    'continent', 'country', 'subnational', 'city', 'locality']
    _df = _df.loc[:, final_columns]
    #date converted to datetime 
    _df['date']= pd.to_datetime(_df['date'])
    #deal with null values that are stores as ''
    _df = _df.replace('', None)
    #now let's separete the colum date into date and time 
    _df.rename(columns = {'date':'date_time'}, inplace = True)
    _df['date'] = pd.to_datetime(_df['date_time']).dt.date
    _df.drop('date_time', inplace=True, axis=1)
    #transform date type again
    _df['date'] = pd.to_datetime(_df['date'])
    #create new columns for year and week
    _df['year'] = pd.to_datetime(_df['date']).dt.isocalendar().year
    _df['week'] = pd.to_datetime(_df['date']).dt.isocalendar().week
    #transform the data types of the table
    convert_dict = {'magnitude': float, 'type': str,'felt': int, 'cdi': float, 'mmi': float, 
    'alert': str, 'status': str, 'tsunami': int, 'sig': int, 'ids': str,'gap': float, 'depth': float, 
    'latitude': float, 'longitude': float, 'distanceKM': float, 'location': str, 'continent': str, 
    'country': str, 'subnational': str, 'city': str, 'locality': str, 'year': int, 'week': int}
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

    path = extract_from_gcs(year, week)
    df = transform(path)
    write_bq(df)



if __name__ == "__main__":
    el_gcs_to_bq()