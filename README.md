
# 🤖 ScenarioCase Scribe – AI Test Scenario Generator

### 🚀 AI-powered test scenario generator for QA automation teams

ScenarioCase Scribe is an **AI-powered test scenario generation platform** designed for QA automation teams.  
It converts plain-text software requirements into **structured Gherkin scenarios** — including **positive, negative, edge, sanity, smoke, and regression cases** — and automatically generates **detailed test cases**.

With one click, ScenarioCase Scribe can:

- Convert natural-language requirements into structured BDD (Gherkin) scenarios

- Generate detailed, automation-ready test cases with preconditions, steps, and expected results

- Accept CSV uploads and generate downloadable .feature and .csv artifacts

- Run as a containerized service — easy to integrate into CI/CD pipelines or automation frameworks

---

⚙️ Quick Start (Local Development)

1. Clone the repository

git clone https://github.com/Amit-access/n8n-automation-platform.git
cd n8n-automation-platform


Create your environment file

cp .env.example .env


Then open .env and update the following:

N8N_BASIC_AUTH_USER and N8N_BASIC_AUTH_PASSWORD

OPENAI_API_KEY with your own key

Adjust WEBHOOK_BASE_URL if deploying elsewhere

Run using Docker Compose

docker-compose up -d


Access the UI

🌐 Web App: https://scribe.qaiagentslab.cloud

⚙️ n8n Editor: http://<your-server-ip>:5678

Stop the services

docker-compose down

2. Try the Hosted Version (No Setup Needed)

Visit the live platform: https://scribe.qaiagentslab.cloud

- Paste plain-text requirements OR

- Upload a .csv file with requirements

- Download generated .feature (Gherkin Scenarios) and .csv (Test Cases)

🔄 3. Automate in Your Pipeline

Integrate it into your CI/CD workflows by running the container in your test stage:

- name: Run ScenarioCase Scribe
  run: docker run -p 3000:3000 dockerhead12/n8n-platform:latest
  
---

🌐 Live Platform

Try it now: https://scribe.qaiagentslab.cloud

✅ Supports both Text Mode and CSV Mode
✅ Generates downloadable .feature and .csv artifacts instantly

---

## Features

- 🔁 Converts text requirements into **structured Gherkin scenarios**  
- 📁 Upload CSV requirements and generate test cases in bulk  
- 📥 Download generated **.feature** and **.csv** files for use in your automation framework  
- 🤖 Built-in **ScenarioCase Agent** runs automatically inside the container — no manual setup required
- 🔐 Security-first design – isolated agent execution, sandboxed container, and no persistent data storage
- 🐳 Fully containerized with automated CI/CD and Docker Hub deployment  

---

## Architecture Overview

The platform is designed as a containerized microservice built with **Node.js and n8n**, with the AI-powered agent (`ScenarioCase Scribe.json`) automatically configured and executed at runtime.

The repository includes:
- `Dockerfile` – Build instructions for the container image  
- `docker-compose.yml` – Compose setup for local development  
- `.github/workflows/docker-build.yml` – CI/CD pipeline to build and push images  
- `ScenarioCase Scribe.json` – AI agent configuration (automatically used in container)  
- `public/Scenario-Scribe.html` – Frontend HTML UI for scenario input and execution

---

## 📁 Project Structure

```
.
├── .github/workflows/docker-build.yml     # GitHub Actions CI/CD workflow
├── Dockerfile                             # Docker image build configuration
├── docker-compose.yml                     # Docker Compose setup for local dev
├── ScenarioCase Scribe.json               # AI agent configuration (auto-used)
├── public/
│   └── Scenario-Scribe.html               # Frontend web UI
├── README.md                              # Project documentation
```

---

## 🐳 Docker Setup & Usage

The Docker image is built and published automatically to Docker Hub using GitHub Actions.

### 📦 Pull the image (from Docker Hub)

```bash
docker pull dockerhead12/n8n-platform:latest
```

### ▶️ Run the container

Using Docker Compose (recommended for local development):

```bash
docker-compose up
```

Or run it directly with Docker:

```bash
docker run -p 3000:3000 dockerhead12/n8n-platform:latest
```

Once the container starts, the service will be available at:  
👉 `http://localhost:3000`

---

## 🔄 CI/CD Pipeline – GitHub Actions

This repository includes a CI/CD workflow defined in `.github/workflows/docker-build.yml`.

Every time a new commit is pushed to the `main` branch:

1. 🏗️ The Docker image is automatically built  
2. 📤 The image is pushed to Docker Hub (`dockerhead12/n8n-platform:latest`)  
3. ✅ A build and sanity check are run to verify the container  

This ensures the container is always up-to-date with the latest code changes without manual intervention.

---

## 📊 Example Use Cases

- Transform business requirements into automation-ready Gherkin test scenarios  
- Automatically generate regression, smoke, and sanity test suites  
- Upload CSV-based requirements and instantly generate `.feature` + `.csv` artifacts  
- Integrate with CI/CD pipelines to generate scenarios before automated test runs  

---

## 🔮 Future Roadmap

- 🧠 **Version Tagging:** Automated release tagging with semantic versioning  
- ⚙️ **Cloud Deployment:** Deploy on VPS/Hostinger for remote usage and team collaboration  
- 🌐 **Public Agent Access:** Enable live testing & feedback from community users  
- 📊 **Enhanced Analytics:** Track and visualize generated scenario coverage  
- 🤖 **Multi-Agent Support:** Add specialized agents for API testing, performance testing, and regression generation  

---

## 🤝 How to Contribute

We welcome contributions from the community! Here's how you can help:

1. **Fork** this repository  
2. **Create a feature branch** (`git checkout -b feature-name`)  
3. **Commit your changes** (`git commit -m 'Add new feature'`)  
4. **Push** to your branch (`git push origin feature-name`)  
5. **Open a Pull Request** 🎉  

---

## 📦 Useful Links

- 🔗 GitHub Repository: [ScenarioCase Scribe](https://github.com/Amit-access/n8n-automation-platform/)  
- 🐳 Docker Hub: [dockerhead12/n8n-platform](https://hub.docker.com/u/dockerhead12)
- 🌐 Live Demo: scribe.qaiagentslab.cloud

---

## 🧪 Summary

ScenarioCase Scribe is your intelligent QA co-pilot — converting natural language requirements into ready-to-automate Gherkin scenarios and structured test cases.  
It drastically reduces manual effort, accelerates automation, and delivers test artifacts your team can use immediately — all from a single, containerized solution.

📦 Docker Hub: `dockerhead12/n8n-platform`  
🧠 Maintainer: **Amit Tupe**
