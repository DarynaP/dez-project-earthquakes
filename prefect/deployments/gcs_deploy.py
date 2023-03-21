from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule
from prefect_gcp.cloud_run import CloudRunJob

from api_to_gcs import etl_api_to_gcs

cloud_run_block = CloudRunJob.load("cloud-run-infrastructure")

deployment = Deployment.build_from_flow(
    flow=etl_api_to_gcs,
    name="etl_api_to_gcs_deployment",
    work_queue_name="default",
    schedule=RRuleSchedule(rrule="RRULE:FREQ=WEEKLY;BYDAY=SA"),
    infrastructure=cloud_run_block
)


if __name__ == "__main__":
    deployment.apply()
