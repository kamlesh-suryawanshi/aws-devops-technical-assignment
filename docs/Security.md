# Security

## Overview

The project follows basic cloud security best practices to protect the application and AWS resources.

## IAM

- IAM Role attached to the EC2 instance
- Least privilege principle followed
- CloudWatch Agent uses IAM Role permissions

## Security Groups

The EC2 Security Group allows only the required ports.

| Port | Purpose |
|------|---------|
| 22 | SSH |
| 80 | HTTP |

## Docker

- Application runs inside a Docker container
- Isolated execution environment

## Nginx

- Acts as a reverse proxy
- Internal application port is hidden from users

## Monitoring

Amazon CloudWatch continuously monitors system metrics and logs.

CloudWatch Alarm sends notifications using Amazon SNS.

## S3

Project backups are stored inside a private Amazon S3 bucket.

## Future Improvements

- HTTPS using Let's Encrypt
- AWS WAF
- Secrets Manager