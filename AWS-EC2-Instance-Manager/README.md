# 🚀 EC2 Instance Manager

This Python script automates EC2 instance management — including starting, stopping, and monitoring CPU utilization — using the AWS SDK (`boto3`).

---

## ✅ Features

- 🔄 Start an EC2 instance
- ⏹️ Stop an EC2 instance
- 📊 Monitor real-time CPU utilization using CloudWatch

---

## 🔧 Requirements

- Python 3.x
- `boto3` library
- AWS CLI (installed & configured)
- EC2 instance with monitoring enabled
- IAM user or role with the following permissions:
  - `AmazonEC2FullAccess`
  - `CloudWatchReadOnlyAccess`

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/aws-python-automation.git
cd aws-python-automation/ec2-instance-manager
```


### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS CLI

If you're using an IAM user:

```bash
aws configure
```

If using an EC2 instance with an IAM role, credentials will be loaded automatically.

#### 🚀 Run the Script

```bash
python3 ec2_control.py
```
You’ll be prompted:

```ubuntu
Enter 'start' to start the instance, 'stop' to stop it, 'monitor' to check CPU utilization, or 'exit' to quit:
```

---

## 🧠 How CPU Monitoring Works
The script fetches the average CPU utilization of your EC2 instance using AWS CloudWatch metrics over the last hour.

---

## 👨‍💻 Author

### Abdullah bin Amin

[LinkedIn](https://www.linkedin.com/in/abdullahbinamin/)

[GitHub](https://github.com/AbdullahbinAmin)

---

## 📜 License

This project is open-sourced under the MIT License.

---