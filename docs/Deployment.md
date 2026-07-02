# Deployment Guide

## 1. Launch EC2

- Ubuntu Server (Free Tier `t2.micro`)
- Configure Security Groups (see [Security.md](Security.md) for allowed ports)
- Connect using SSH

## 2. Install Docker

```bash
sudo apt update
sudo apt install docker.io -y
sudo usermod -aG docker $USER
```

## 3. Clone Repository

```bash
git clone <repository-url>
cd aws-devops-technical-assignment
```

## 4. Build Docker Image

```bash
docker build -t cloudhealth-api .
```

## 5. Run Container

```bash
docker run -d \
  --name cloudhealth-api \
  --restart unless-stopped \
  -p 5000:5000 \
  cloudhealth-api
```

The `--restart unless-stopped` flag ensures the container automatically restarts if it crashes or the EC2 instance reboots.

## 6. Configure Nginx

Install Nginx on the EC2 host and configure it as a reverse proxy in front of the Flask container (listening on port 80, forwarding to `localhost:5000`). The Nginx config file is version-controlled in the repository and copied to `/etc/nginx/sites-available/` during deployment.

## 7. Configure GitHub Actions

- Generate an SSH key pair for deployment access
- Add the following as GitHub Actions Secrets: `EC2_HOST`, `EC2_USER`, `EC2_SSH_KEY`
- Configure `.github/workflows/deploy.yml` to build the Docker image, push it (or transfer it), and SSH into EC2 to redeploy the container on every push to `main`

## 8. Configure CloudWatch

- Install the CloudWatch Agent on the EC2 instance
- Configure metrics collection (CPU, memory, disk)
- Configure log collection (application logs, Nginx access/error logs)
- Configure a CloudWatch alarm on CPU utilization, linked to an SNS topic

## 9. Backup

Upload project artifacts (code, configs, docs) to a private Amazon S3 bucket.

## 10. Load Testing

Run k6 load tests against the deployed endpoint. See [LoadTesting.md](LoadTesting.md) for configuration and results.