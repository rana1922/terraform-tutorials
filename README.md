# Food Delivery App - Docker + Terraform + AWS EC2

## Project Overview

This project demonstrates a full-stack application deployment using:

* Frontend: Node.js + Express + EJS
* Backend: Flask (Python)
* Containerization: Docker & Docker Compose
* Infrastructure as Code: Terraform
* Cloud Platform: AWS EC2

The application allows users to register with their name and email through a web interface. The data is stored in a JSON file and can be retrieved through a backend API.



---

## Project Structure

```text
food-delivery-app/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── server.js
│   ├── package.json
│   ├── Dockerfile
│   └── templates/
│       └── index.ejs
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── userdata.sh
│
├── docker-compose.yml
└── README.md
```

---

## Features

* User registration form
* Flask REST API
* Dockerized frontend and backend
* Docker Compose orchestration
* Automated AWS EC2 provisioning using Terraform
* Automated deployment using EC2 User Data


## Terraform Deployment

### Prerequisites

* AWS Account
* AWS CLI Configured
* Terraform Installed
* EC2 Key Pair Created

### Configure AWS Credentials

```bash
aws configure
```

### Initialize Terraform

```bash
cd terraform

terraform init
```

### Validate Configuration

```bash
terraform validate
```

### Deploy Infrastructure

```bash
terraform apply -var="key_name=<your-keypair-name>"
```

### Access Application

Frontend:

```text
http://<EC2_PUBLIC_IP>:3000
```

Backend:

```text
http://<EC2_PUBLIC_IP>:8000
```

---


---

## Useful Commands

### Check Running Containers

```bash
docker ps
```

### View Container Logs

```bash
docker logs frontend

docker logs backend
```

### Stop Containers

```bash
docker compose down
```

### Restart Containers

```bash
docker compose up -d --build
```

---


