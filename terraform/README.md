## Terraform 
We will use Terraform to build and manage GCP infrastructure. Here you can find the following files:
- [variables.tf](terraform/variables.tf) - contains variables to make your configuration more reproducible;
- [main.tf](terraform/main.tf) - is a key configuration file consisting of several sections;
- [table1_schema.json](terraform/table1_schema.json) - contain the JSON schema for the Data Warehouse table.


### `variables.tf`
This file was used to define some of the variables: 

 - project: project ID `dez-project-earthquakes`
 - region: location zone `europe-southwest1`
 - credentials: path to were JSON credential file is located 
 - bq_dataset: BigQuery dataset to load raw data `bq_earthquake_data`
 - bdt: BigQuery dataset for dbt transformations `dbt_earthquake`

> If you use different names, make sure that you change them as well in the file.

### `main.tf`

