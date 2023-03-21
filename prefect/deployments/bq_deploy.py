from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import RRuleSchedule
from prefect_gcp.cloud_run import CloudRunJob

from gcs_to_bq import el_gcs_to_bq

cloud_run_block = CloudRunJob.load("cloud-run-infrastructure")

deployment = Deployment.build_from_flow(
    flow=el_gcs_to_bq,
    name="etl_gcs_to_bq_deployment",
    work_queue_name="default",
    schedule=RRuleSchedule(rrule="RRULE:FREQ=WEEKLY;BYDAY=SU"),
    infrastructure=cloud_run_block
)


if __name__ == "__main__":
    deployment.apply()
