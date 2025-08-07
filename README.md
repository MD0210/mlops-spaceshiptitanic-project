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
2. 📦 **Push** Docker image to AWS ECR (`Spashiptitanicrepo`)
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

