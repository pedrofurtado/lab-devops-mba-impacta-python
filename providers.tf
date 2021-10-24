terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "3.89.0"
    }
  }
}
provider "google" {
  project = "mythic-tenure-45826"
  region = "us-west1"
  zone = "us-west1-b"
}
