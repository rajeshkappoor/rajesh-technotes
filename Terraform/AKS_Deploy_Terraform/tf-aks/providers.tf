terraform {
  required_version = ">=1.0"

  required_providers {
    # azapi = {
    #   source  = "azure/azapi"
    #   version = "~>1.5"
    # }
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.37" # or latest stable version
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.0"
    }
    time = {
      source  = "hashicorp/time"
      version = "0.9.1"
    }
  }
}

provider "azurerm" {
  features {}
   subscription_id = "b380671e-07eb-4f0a-b256-f2e45b01b328"
}