# Azure-Powered Real-Time Event Processing System

## Overview

This project is a cloud-native, microservices-based real-time event processing system built with Microsoft technologies. It processes and analyzes data streams in real-time, leveraging Azure services like Event Grid, Cosmos DB, and Stream Analytics. Designed for scalability, resilience, and real-time insights, it’s a perfect showcase of cloud-native architecture and advanced event-driven design.

## Features

- Event-Driven Microservices Architecture
- Real-Time Data Processing with Azure Stream Analytics
- Serverless Compute with Azure Functions
- Scalable Deployment with Azure Kubernetes Service (AKS)
- Machine Learning Integration for Real-Time Predictions
- Comprehensive Monitoring and Alerts

## Technologies Used

- **Microservices:** .NET Core, Docker, Kubernetes (AKS)
- **Event Processing:** Azure Event Grid, Azure Service Bus
- **Data Storage:** Azure Cosmos DB
- **Machine Learning:** Azure Machine Learning, Azure Synapse Analytics
- **Monitoring:** Azure Monitor, Application Insights
- **Security:** Azure Active Directory, Managed Identity

## Getting Started

### Prerequisites

- Azure Subscription
- .NET Core SDK
- Docker
- Helm

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/azure-event-processing-system.git
    ```

2. Deploy infrastructure using the provided script:
    ```bash
    cd infrastructure/aks-deployment
    ./aks_deploy.sh
    ```

3. Deploy microservices using Helm:
    ```bash
    helm install my-microservices ./helm-chart
    ```

### Usage

- Access the event processing dashboard on Azure Monitor.
- Manage and monitor microservices using AKS.
- Review real-time data processing results on Azure Data Explorer.

## Contributing

Contributions are welcome! Please submit pull requests to improve the system.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## ✅ Verified Quickstart (Local Simulator)

These commands run a local simulator that mirrors the ingestion → processing → results flow
without requiring Azure resources. This is useful for validating the repo in a clean environment.

```bash
./scripts/run_local.sh
```

To customize the number of events or payload base:

```bash
./scripts/run_local.sh --count 5 --payload demo-event
```

## ✅ Verified Smoke Test

```bash
./scripts/smoke_test.sh
```

## Troubleshooting

- **`./aks_deploy.sh: Permission denied`**

  Ensure the script is executable or run it via bash:

  ```bash
  chmod +x infrastructure/aks-deployment/aks_deploy.sh
  ./infrastructure/aks-deployment/aks_deploy.sh
  ```

- **`az: command not found` or Azure authentication errors**

  The AKS deployment requires the Azure CLI, Helm, and an authenticated Azure session. Install
  the Azure CLI and run `az login` before executing `aks_deploy.sh`.

- **No Azure resources available**

  Use the local simulator (`./scripts/run_local.sh`) to validate the pipeline logic without Azure.
