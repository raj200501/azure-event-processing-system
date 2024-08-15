#!/bin/bash

# Variables
RESOURCE_GROUP="myResourceGroup"
AKS_NAME="myAKSCluster"
ACR_NAME="myContainerRegistry"

# Create a resource group
az group create --name $RESOURCE_GROUP --location eastus

# Create an Azure Container Registry
az acr create --resource-group $RESOURCE_GROUP --name $ACR_NAME --sku Basic

# Create an AKS cluster
az aks create --resource-group $RESOURCE_GROUP --name $AKS_NAME --node-count 1 --enable-addons monitoring --generate-ssh-keys --attach-acr $ACR_NAME

# Get credentials for the cluster
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_NAME

# Deploy microservices using Helm
helm install my-microservices ./helm-chart
