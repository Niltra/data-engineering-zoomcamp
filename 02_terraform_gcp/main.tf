terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  credentials = file("./keys/my-creds.json")
  project     = "de-zoomcamp-2026-500215"
  region      = "europe-west1"
}

# 1. El Data Lake (Google Cloud Storage)
resource "google_storage_bucket" "demo-bucket" {
  name          = "de-zoomcamp-2026-500215-terra-bucket" # El nombre debe ser único en todo el mundo
  location      = "EU"
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# 2. El Data Warehouse (Google BigQuery)
resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = "demo_dataset"
  location   = "EU"
}