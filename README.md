# 🚀 MLOps Spaceship Titanic Project

Welcome to the `mlops-spaceshiptitanic-project` — an end-to-end machine learning project built with MLOps best practices using the [Spaceship Titanic Kaggle dataset](https://www.kaggle.com/competitions/spaceship-titanic).

This repository demonstrates a modular, production-ready ML pipeline with components for ingestion, validation, transformation, training, evaluation, and deployment.

---

## 🧠 Problem Statement

The goal is to predict whether a passenger was **transported to an alternate dimension** during the Spaceship Titanic accident. Given structured data about passengers (e.g., age, cabin, home planet, expenditures), we will train a classification model to predict the `Transported` label.

---

## ⚙️ Tech Stack & Tools

- **Language:** Python (Object-Oriented Programming)
- **MLOps Framework:** GitHub Actions, Docker, AWS (EC2, ECR, S3)
- **IDE & Environment:** VS Code, Anaconda
- **Data & Monitoring:** MongoDB, Evidently AI

---

## 🚀 CI/CD Deployment Flow

1. 🏗️ **Build** Docker image from source code
2. 📦 **Push** Docker image to AWS ECR (`Spaceshiptitanicrepo`)
3. 🖥️ **Launch** EC2 Ubuntu instance
4. 📥 **Pull** image from ECR to EC2
5. 🧠 **Run** container to start ML inference service
6. 🤖 **Trigger** GitHub Actions for automated deployment

---

## 🏗️ Project Structure

```bash
mlops-spaceshiptitanic-project/
│
├── spaceship_titanic/
│   ├── components/               # Core ML pipeline steps
│   │   ├── data_ingestion.py
│   │   ├── data_validation.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   │   ├── model_evaluation.py
│   │   └── model_pusher.py
│   │
│   ├── configuration/           # Configuration management
│   ├── constants/               # Constant values and paths
│   ├── entity/                  # Config and artifact entities
│   ├── exception/               # Custom exception handling
│   ├── logger/                  # Logging module
│   ├── pipeline/                # Training & prediction pipelines
│   └── utils/                   # Utility functions
│
├── config/
│   ├── model.yaml               # Model training configurations
│   └── schema.yaml              # Input schema for validation
│
├── app.py                       # Optional API endpoint
├── demo.py                      # Manual script for testing
├── requirements.txt             # Project dependencies
├── setup.py                     # Installable package setup
├── Dockerfile                   # Container definition
├── .dockerignore
└── README.md                    

# Git Command
```bash
- git Clone URL 

- git add .

- git commit -m "comment here"

- git push origin main
```

# Create Environment using Conda
```bash
- conda create -n {environment name} python={version} -y
```

```bash
- conda init
```

```bash
- conda activate {environment name}
```

```bash
- pip install -r requirements.txt  #this is inside the environment
```

# Workflow
1. constants
2. entity
3. components
4. pipeline
5. Main file

# Export the environment variable using git bash
```bash

- export MONGODB_URL="mongodb+srv://<username>:<password>...."

- export AWS_ACCESS_KEY_ID = <AWS_ACCESS_KEY_ID>

- export AWS_SECRET_ACCESS_KEY = <AWS_SECRET_ACCESS_KEY>

```

# AWS-CICD-Deployment-with-Github-Actions
## 1. Login to AWS console.
## 2. Create IAM user for deployment
#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess
## 3. Create ECR repo to store/save docker image
```bash
- Save the URI: 699444791123.dkr.ecr.us-east-1.amazonaws.com/easyvisarepo
```
## 4. Create EC2 machine (Ubuntu)
## 5. Open EC2 and Install docker in EC2 Machine:

```bash
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

## 6. Configure EC2 as self-hosted runner:
```bash
setting>actions>runner>new self hosted runner> choose os> then run command one by one
```

## 7. Setup github secrets:
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- ECR_REPO
- MONGODB_URL