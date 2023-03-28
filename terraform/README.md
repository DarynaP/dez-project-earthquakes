## Terraform 
Terraform was used to build and manage GCP infrastructure. Here you can find the following files:
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
This file was used to set:
 - Data Lake:
        - Bucket named `earthquake-data-dez` (where are loaded parquet files from API)
 - Data Warehouse: 
        - BigQuery dataset `bq_earthquake_data`:
         - table `earthquake_info` (used to load data from the bucket `earthquake-data-dez`)
                - the schema for this table is specified in the [JSON file](terraform/earthquake_info_schema.json)
                - data loaded in this table is **partitioned** by day, and **clustered** by continent and week
        - BigQuery dataset `dbt_earthquake` (where will be located the tables with data transformed by dbt)

> For more information check [instructions](https://github.com/DarynaP/dez-project-earthquakes#terraform)
