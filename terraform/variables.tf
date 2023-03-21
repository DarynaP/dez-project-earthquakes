variable "project" {
  description = "GCP Project ID"
  default = "dez-project-earthquakes"
  type = string

}

variable "region" {
  description = "Region for GCP resources"
  default = "europe-southwest1"
  type = string
}

variable "credentials" {
    description = "key for credentials acess"
    default = "/home/darynap/dez-project-earthquakes/dez-project-earthquakes-791c1355c759.json"

}

variable "storage_class" {
  description = "Storage class type for bucket"
  default = "STANDARD"
}

variable "bq_dataset" {
  description = "BigQuery Dataset that data will be written to"
  type = string
  default = "bq_earthquake_data"
}

