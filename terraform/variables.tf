variable "project" {
  description = "GCP Project ID"
  default = "dez-project-earthquakes" #change to your project ID
  type = string

}

variable "region" {
  description = "Region for GCP resources"
  default = "europe-southwest1" #change to your zone
  type = string
}

variable "credentials" {
    description = "key for credentials acess"
    default = "/home/darynap/dez-project-earthquakes/dez-project-earthquakes-791c1355c759.json" #change to path for your key file

}

variable "storage_class" {
  description = "Storage class type for bucket"
  default = "STANDARD"
}

variable "bq_dataset" {
  description = "BigQuery Dataset that data will be written to"
  type = string
  default = "bq_earthquake_data" #change to your BigQuery name
}


