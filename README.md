# DATA ENGINEERING ZOOMCAMP – Final Project
## Overview
This capstone project was developed as a part of the [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp) 
course held by [DataTalks.Club](https://datatalks.club/). 
The goal of this project was to build an end-to-end data pipeline, with a focus on: 
* Creating a data pipeline to aid with batch data processing (on a weekly basis);
* Producing an analytical dashboard that will allow to easily discover trends and assimilate insights.

> **Disclaimer** The dataset used for this project was collected between January and April 2023, which makes it a relatively small dataset (25,626 observations). The main idea of this project wasn't to deal with a big dataset at this point, but rater build a pipeline that can fetch, organize and transform present data on a weekly basis. However, it is possible to obtain a bigger dataset if you maintain this pipeline to fetch data for longer time, but for me that wasn't possible due to course deadlines.

## Table of Contents
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
    <li><a href="#dataset-used">Dataset used</a></li>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#project-architecture">Project architecture</a></li>
    <li><a href="#dashboard">Dashboard</a>
    <li><a href="#conclusions">Conclusions</a>
    <li><a href="#reproducibility">Reproducibility</a>
  </ol>
</details>

## About the Project
The planet Earth is constantly changing 🌍. Seismic activity is produced when tectonic plates shift or when other events take place below the surface. While some earthquakes are sizable and do a lot of damage, other earthquakes are so little that they can hardly be felt without sensitive technology. 

Earthquake data is a valuable resource for public safety, and this project aims to look to this information at weekly basis. With the power of this data, we can answer a series of questions:
 - How many earthquakes happened worldwide per day? 
 - Which geographical areas had the earthquake epicenter during the specified time frame?
 - How many earthquakes happened in each continent, monthly?
 


### Dataset used
The data was collected using [EveryEarthquake API](https://rapidapi.com/dbarkman/api/everyearthquake/), additionally the data obtained between January and April 2023 can be found in the folder [`earthquake-data`](earthquake-data) as parquet files (per week).
To use this API you need to have a **X-RapidAPI-Key**, to obtain your key you first need to create an account, more information can be obtained [here](https://docs.rapidapi.com/docs/keys).

The complete information about the dataset can be found at [ANSS Comprehensive Earthquake Catalog](https://earthquake.usgs.gov/data/comcat).

The final dataset loaded to BigQuery contain the following information:

- **id (str)**: unique ID value that identifies the seismic event 
- **magnitude (float)**: event registered magnitude
- **felt (int)**: total number of felt reports submitted
- **depth (float)**: the depth where the earthquake begins to rupture (in km)
- **latitude (float)**: decimal degrees latitude (negative values for southern latitudes) [-90.0, 90.0] - coordinates of the epicenter in units of latitude (the number of degrees north (N) or south (S) of the equator and varies from 0 at the equator to 90 at the poles)
- **longitude (float)**: decimal degrees longitude (negative values for western longitudes) [-180.0, 180.0] - coordinates of the epicenter in units of longitude (longitude is the number of degrees east (E) or west (W) of the prime meridian which runs through Greenwich, England)
- **distanceKM (float)**: distance to populated places that are in close proximity to the seismic event (in km)
- **date (datetime)**: date when the seismic event ocurred
- **year (int)**: year when the event ocurred
- **week (int)**: week of the year when the event ocurred
- **country (str)**: continent of seismic event (`None` if the event occurred in the ocean)
- **city (str)**: city of seismic event (`None` if the event occurred in the ocean)
- **locality (str)**: locality of seismic event (`None` if the event occurred in the ocean)
- **continent (str)**: continent of seismic event (`None` if the event occurred in the ocean)


<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

### Technologies
For this project the following technologies were used:
<br>
- Google Cloud Platform (GCP)
    - Data Lake: [*Google Cloud Storage*](https://cloud.google.com/storage)
    - Data Warehouse: [*BigQuery*](https://cloud.google.com/bigquery)
    - Serverless execution environment: [*Artifact Registry*](https://cloud.google.com/artifact-registry), [*Compute Engine*](https://cloud.google.com/compute) and [*Cloud Run*](https://cloud.google.com/run/docs/overview/what-is-cloud-run)
- Infrastructure as code (IaC): [*Terraform*](https://www.terraform.io/)
- Containerization: [*Docker*](https://www.docker.com/)
- Workflow orchestration: [*Prefect Cloud*](https://www.prefect.io/cloud/)
- Transforming data: [*dbt*](https://www.getdbt.com/)
- Data Visualization: [*Power BI*](https://powerbi.microsoft.com/pt-pt/desktop/)

<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

### Project architecture

The end-to-end data pipeline includes the following steps:
- Fetch, select and upload the initial dataset to a Data Lake (Bucket);
- Get, pre-process and upload the data from the Data Lake to a Data Warehouse;
- Transform the data in the Data Warehouse to prepare it for the dashboard;
- Create the final dashboard.

The diagram below contains detailed information:
![](images/project_architecture.png)


<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

## Dashboard

The final dashboard was created using Power BI, for a more interactive view of the dashboard you can access using this [link](https://app.powerbi.com/links/dPVMgplCPK?ctid=3ed61ac7-7658-4220-8a6a-75bf5a7fe255&pbi_source=linkShare) (you will need a Power BI account).

![](images/final_dashboard.png)

## Conclusions

When we talk about earthquakes, it is important to note that they are a natural occurrence that happens all around the world. 
<br>

While the number of earthquakes per day may seem high, the data showed that **between 200 and 300 earthquakes** occur every day, it is important to note that most of these earthquakes are small and go unnoticed by people (low magnitude - alert green).
<br>

Regarding the localization of the earthquakes, it wasn't surprising since the **majority of them occurred close to the limits of the tectonic plates**. The tectonic plates are constantly moving, sliding past each other or colliding, and sometimes this movement results in an earthquake.
Some of the most active known lines in the world include the San Andreas Fault in California, the Ring of Fire in the Pacific Ocean, the Himalayan Front in Asia,and Cascadia Subduction Zone along the West Coast of North America, which can be observed in the map. 
<br>

When we look at the distribution of earthquakes around the world, it is not surprising to learn that **around 50% of earthquakes occur in the ocean**. This is because a large portion of the Earth's surface is covered by oceans, and many of the world's most active fault lines are located beneath the ocean floor. After the ocean, North America is the continent that experiences the most seismic activity, and that can be explained by the  major fault lines located in that region (already mentioned above).


## Reproducibility 
This project pipeline can be replicated by following the steps in this tutorial.

### Google Cloud Platform
GCP account is required. If you don't have one yet, you can create and use a free trial. After creating an account:
  1. Setup new project and give it an unique Project ID.
  2. Configure service account to get access to this project. 
Go to IAM & Admin > Service Accounts > Click on + CREATE SERVICE ACCOUNT > Give a name and an service account ID > Grant this service account access to project, namely as:
  - Viewer
  - Storage Admin
  - Storage Object Admin
  - BigQuery Admin

After the service account is created go to Actions > Manage Keys > ADD KEY > Create new key > Save it as JSON file
<br>
  3. For the local setup of GCP download [SDK](https://cloud.google.com/sdk)
<br>
  4. Set environment variable to your downloaded GCP key:
```bash
export GOOGLE_APPLICATION_CREDENTIALS="<path/to/your/service-account-authkeys>.json"
gcloud auth activate-service-account --key-file $GOOGLE_APPLICATION_CREDENTIALS
```
<br>
  5. Enable the following options under the APIs and services section:

  - [Identity and Access Management (IAM) API](https://console.cloud.google.com/apis/library/iam.googleapis.com) 
  - [IAM service account credentials API](https://console.cloud.google.com/apis/library/iamcredentials.googleapis.com)
  - [Compute Engine API](https://console.developers.google.com/apis/api/compute.googleapis.com)
  - [Cloud Run Admin API](https://console.cloud.google.com/apis/library/run.googleapis.com)
  - [Artifact Registry API](https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com)

  
For more information follow this [tutorial](https://www.youtube.com/watch?v=18jIzE41fJ4&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=3&ab_channel=DataTalksClub%E2%AC%9B)

  6. You can start by cloning this repository

### Terraform 
Terraform was used to build and manage GCP infrastructure. Terraform configuration files are located in the [terraform folder](terraform), there can be found the detailed information about the files:
- [variables.tf](terraform/variables.tf) - contains variables to make your configuration more reproducible;
- [main.tf](terraform/main.tf) - is a key configuration file consisting of several sections;
- [table1_schema.json](terraform/table1_schema.json) - contain the JSON schema for the Data Warehouse table.

> **Important** if you want to change the names of *project, bucket, dataset ...*, don't forget to replace them in the files!


The steps below can be used to generate resources inside the GCP:
1. Move to the [terraform folder](terraform) using bash command `cd`.
2. Run `terraform init` command to initialize the configuration.
3. Use `terraform plan` to match previews local changes against a remote state.  
4. Apply changes to the cloud with `terraform apply` command, you will need to write `yes` to confirm that you want to proceed with this task.

> To remove stack from the Cloud, use the `terraform destroy` command.

### Prefect
Prefect cloud was used for workflow orchestration. In order to run the created flow in a serverless  way  Google Compute Engine was set as the agent for the run and an execution environment was created using Google Cloud Run.

For more details you can check this amazing [tutorial](https://medium.com/@danilo.drobac/7-a-complete-google-cloud-deployment-of-prefect-2-0-32b8e3c2febe).

1. Login to your Prefect Cloud `prefect cloud login`
2. Create the needed blocks `python prefect/blocks/gcp_blocks.py`
3. Configure VM for Agent
```bash
gcloud compute instances create prefect-agent \
    --image=ubuntu-2004-focal-v20230104 \
    --image-project=ubuntu-os-cloud \
    --machine-type=e2-micro \
    --zone=<YOUR ZONE> \
    --service-account=prefect@PROJECT_ID.iam.gserviceaccount.com
```
4. SSH into the VM using `gcloud compute ssh prefect-agent`
5. Create a new file called install_script.sh by typing: `nano install_script.sh`
6. Copy in the following contents, replacing <INSERT_PREFECT_API_KEY> with the Prefect API key
```bash
#!/bin/bash
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    software-properties-common \
    python3-dateutil
sudo ln -s /usr/bin/python3 /usr/bin/python
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
PATH="$HOME/.local/bin:$PATH"
export PATH
pip3 install prefect prefect-gcp
prefect cloud login -k <INSERT_PREFECT_API_KEY>
```
7. Make the file executable (+x) by running: `sudo chmod +x install_script.sh`
8. Execute the file and run all of our commands within: `./install_script.sh`

9. The last thing we need to do is start the agent for the main queue
```bash
tmux
prefect agent start -q main
```
press Ctrl/Cmd + b + d to exit the session
9. Create Artifact Registry
```bash
gcloud artifacts repositories create prefect-flows-docker \
  --repository-format=docker \
  --location= <YOUR ZONE> \
  --description="Docker repository for Prefect Flows"
```
10. Build the Docker Image
<br>

`docker build -t <INSERT_REGISTRY_ADDRESS>/ram-api-flow:2.7.7-python3.8 . `
<br>

`gcloud auth configure-docker <YOUR ZONE>-docker.pkg.dev` 
<br>

`docker push <INSERT_REGISTRY_ADDRESS>/ram-api-flow:2.7.7-python3.8`

11. Create Cloud Run Block 
`python prefect/blocks/cloudrun_block.py`
12. Create two deployments using Cloud Run Infrastructure
<br>

`python prefect/deployments/bq_deploy.py`
<br>

`python prefect/deployments/gcs_deploy.py`


This will create two deployments, the first one runs every sunday to get the data from API and load to GCP Bucket, the second runs every sunday and gest the data from the bucket, transforms it and then load to BigQuery table. 

![](images/prefect_deploy.png)


### dbt
[dbt](https://www.getdbt.com/) was used for data transformation in DWH for further analytics dashboard development.

First you will need to create a dbt Cloud account (if you don't already have one) using [this link](https://www.getdbt.com/signup/) 
and connect to your BigQuery by following [these instructions](https://docs.getdbt.com/docs/dbt-cloud/cloud-configuring-dbt-cloud/cloud-setting-up-bigquery-oauth).
You can find more detailed instructions [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/dbt_cloud_setup.md).

Note that:
* you can fork or copy an existing dbt project located in the [separate folder](dbt) and use a link to the forked/copied version if necessary; 
* you need to check that BigQuery already has areas (datasets) for staging and production dbt models


<p align="right">(<a href="#table-of-contents">back to table of contents</a>)</p>

