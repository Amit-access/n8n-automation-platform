# 🤖 ScenarioCase Scribe – AI Test Scenario Generator

### 🚀 AI-powered test scenario generator for QA automation teams

ScenarioCase Scribe is an **AI-powered test scenario generation platform** designed for QA automation teams.  
It converts plain-text software requirements into **structured Gherkin scenarios** — including **positive, negative, edge, sanity, smoke, and regression cases** — and automatically generates **detailed test cases**.

The tool can also process **CSV requirement uploads** to generate:
- 📜 Gherkin scenarios downloadable as `.feature` files  
- 🧪 Test cases downloadable as `.csv` files

---

## 🧠 Features

- 🔁 Converts text requirements into **structured Gherkin scenarios**  
- 📁 Upload CSV requirements and generate test cases in bulk  
- 📥 Download generated **.feature** and **.csv** files for use in your automation framework  
- 🤖 Built-in **ScenarioCase Agent** runs automatically inside the container — no manual setup required  
- 🐳 Fully containerized with automated CI/CD and Docker Hub deployment

---

## 🧰 Architecture Overview

The platform is designed as a containerized microservice built with **Node.js and n8n**, with the AI-powered agent (`ScenarioCase Scribe.json`) automatically configured and executed at runtime.

The repository includes:
- `Dockerfile` – Build instructions for the container image  
- `docker-compose.yml` – Compose setup for local development  
- `.github/workflows/docker-build.yml` – CI/CD pipeline to build and push images  
- `ScenarioCase Scribe.json` – AI agent configuration (automatically used in container)  

---

## 🐳 Docker Setup & Usage

The Docker image is built and published automatically to Docker Hub using GitHub Actions.

### 📦 Pull the image (from Docker Hub)

```bash
docker pull dockerhead12/n8n-platform:latest
### ▶️ Run the container

Using Docker Compose (recommended for local development):

```bash
docker-compose up
Or run it directly with Docker:
docker run -p 3000:3000 dockerhead12/n8n-platform:latest
Once the container starts, the service will be available at:👉 http://localhost:3000

---

## 🔄 CI/CD Pipeline – GitHub Actions

This repository includes a CI/CD workflow defined in:

Every time a new commit is pushed to the `main` branch:

1. 🏗️ The Docker image is automatically built  
2. 📤 The image is pushed to Docker Hub (`dockerhead12/n8n-platform:latest`)  
3. ✅ A build and sanity check are run to verify the container

This ensures the container is always up-to-date with the latest code changes without manual intervention.

---

## 📁 Repository Structure
.
├── .github/workflows/docker-build.yml # GitHub Actions CI/CD workflow
├── Dockerfile # Docker image build configuration
├── docker-compose.yml # Docker Compose setup for local dev
├── ScenarioCase Scribe.json # AI agent configuration (auto-used)
├── README.md # Project documentation

---

## 📊 Example Use Cases

- Transform business requirements into automation-ready Gherkin test scenarios  
- Automatically generate regression, smoke, and sanity test suites  
- Upload CSV-based requirements and instantly generate `.feature` + `.csv` artifacts  
- Integrate with CI/CD pipelines to generate scenarios before automated test runs

---

## 🔮 Future Roadmap

- 🧠 Add version tagging and automated release generation 
- 📊 Integrate reporting for generated test cases 

🧪 Summary

ScenarioCase Scribe is your intelligent QA co-pilot — converting natural language requirements into ready-to-automate Gherkin scenarios and structured test cases.
It drastically reduces manual effort, accelerates automation, and delivers test artifacts your team can use immediately — all from a single, containerized solution.

📦 Docker Hub: dockerhead12/n8n-platform

🧠 Maintainer: Amit Tupe
