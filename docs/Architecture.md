# Architecture

## Overview

The application is deployed on an AWS EC2 instance using Docker. Nginx acts as a reverse proxy and GitHub Actions automates deployment through SSH. Amazon CloudWatch monitors system metrics and application logs while Amazon SNS sends alarm notifications. Project backups are stored in Amazon S3.

## Architecture Flow

```
Developer
    │
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ▼
SSH Deployment
    │
    ▼
Amazon EC2
    ├── Docker
    │     └── Flask API
    ├── Nginx
    └── CloudWatch Agent
    │
    ▼
CloudWatch
    ├── Metrics
    ├── Logs
    └── Alarms
    │
    ▼
Amazon SNS
    │
    ▼
Email Notification

Project Backup
    │
    ▼
Amazon S3
```

## AWS Services Used

- Amazon EC2
- Amazon CloudWatch
- Amazon SNS
- Amazon S3
- IAM
- Security Groups

## Components

### EC2
Hosts the application.

### Docker
Runs the Flask API inside a container (image: `cloudhealth-api`).

### Nginx
Acts as a reverse proxy in front of the container, forwarding external traffic to the Flask API.

### GitHub Actions
Automatically builds and deploys the application to EC2 via SSH after every push to the main branch.

### CloudWatch
Collects system metrics (CPU, memory, disk) and application/Nginx logs.

### SNS
Sends email alerts when a CloudWatch alarm is triggered.

### S3
Stores project backups in a private bucket.