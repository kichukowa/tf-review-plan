resource "google_storage_bucket" "example-bucket" {
  name     = "temp-example-storage-tf"
  location = "EU"
}