terraform {
  required_version = ">= 1.0"
  backend "local" {}  
  required_providers {
    google = {
      source  = "hashicorp/google"
    }
  }
}

provider "google" {
  project = var.project
  region = var.region
  credentials = file(var.credentials)
}

# Data Lake Bucket
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket
resource "google_storage_bucket" "data_bucket" {
  name          = "earthquake-data-dez"
  location      = var.region

  # Optional, but recommended settings:
  storage_class = var.storage_class
  uniform_bucket_level_access = true

  versioning {
    enabled     = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 120  // days
    }
  }

  force_destroy = true
}

# Data Warehouse
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "data-earthquake" {
  dataset_id = var.bq_dataset
  project    = var.project
  location   = var.region
}
#
resource "google_bigquery_table" "default" {
  dataset_id = google_bigquery_dataset.data-earthquake.dataset_id
  table_id   = "earthquake_info"

  time_partitioning {
    type = "DAY"
    field = "date"
  }

  clustering = ["continent", "week"]

  schema = file("/home/darynap/dez-project-earthquakes/terraform/earthquake_info_schema.json")

  deletion_protection=false
}
#
resource "google_bigquery_dataset" "dbt-earthquake" {
  dataset_id = var.dbt
  project    = var.project
  location   = var.region
}
