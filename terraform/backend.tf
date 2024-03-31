terraform {
  backend "gcs" {
    bucket = "state-tf-review-plan"
    prefix = "terraform/state"
  }
}