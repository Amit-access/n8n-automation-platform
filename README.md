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
