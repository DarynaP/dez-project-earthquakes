from prefect_gcp.cloud_run import CloudRunJob
from prefect_gcp import GcpCredentials

credentials = GcpCredentials.load("dez-gcp-creds")

block = CloudRunJob(
    credentials=credentials,
    project="dez-project-earthquakes",
    image="europe-southwest1-docker.pkg.dev/dez-project-earthquakes/prefect-flows-docker/ram-api-flow:earthquake-project",
    region="europe-southwest1"
)

block.save("cloud-run-infrastructure", overwrite=True)