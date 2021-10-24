resource "google_compute_instance" "firstvm" {
  name         = "helloworld"
  machine_type = "n1-standard-1"
  zone         = "us-central1-c"
  boot_disk {
    initialize_params {
      image = "ubuntu-2004-focal-v20210927"
    }
  }
  network_interface {
    network = "default"
    access_config {
    }
  }
}
