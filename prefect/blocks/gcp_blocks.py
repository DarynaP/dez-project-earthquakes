from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials

with open("path to your credentials .json file") as f:
    service_account = f.read() #credentials info

credentials_block = GcpCredentials(
    service_account_info = service_account 
)
credentials_block.save("dez-gcp-creds", overwrite=True)


bucket_block = GcsBucket(
    gcp_credentials=GcpCredentials.load("dez-gcp-creds"),
    bucket="earthquake-data-dez",  #GCS bucket name
)

bucket_block.save("dez-gcs", overwrite=True)