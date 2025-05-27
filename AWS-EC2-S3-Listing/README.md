# EC2-S3 Listing Automation

This Python automation script connects to AWS using `boto3` and lists all available S3 buckets in your account. It's designed to run inside an EC2 instance with the appropriate IAM role or user credentials.

---

## ✅ Features
- Connects to AWS using Python's `boto3`
- Lists all S3 buckets in your account
- Displays output directly in the terminal
- Lightweight and easy to customize

---

## 🔧 Prerequisites
- Python 3.x installed
- AWS CLI installed and configured
- EC2 instance (Amazon Linux or Ubuntu preferred)
- IAM user or instance role with:
  - **AmazonS3FullAccess**
  - **AmazonEC2FullAccess**

---

## 🛠️ AWS CLI Setup (Before Running the Script)

1. **Install AWS CLI (if not already installed):**

   **Amazon Linux / Ubuntu:**
    ```bash
    sudo apt update
    sudo apt install awscli -y
    ```

2. **Configure AWS CLI:**

    If using IAM user credentials:

    ```bash
    aws configure
    ```

You will be prompted to enter:

- AWS Access Key ID
- AWS Secret Access Key
- Region (e.g., us-east-1)
- Output format (e.g., json)

If using IAM role on EC2, skip this step — AWS CLI and boto3 will auto-detect permissions.


---

## 📦 Installation

1. **SSH into your EC2 Instance** (e.g., via MobaXterm):
   ```bash
   ssh -i your-key.pem ec2-user@your-ec2-ip
   ```

2. **Install Python & pip** (if not installed):

    ```bash
    sudo apt update && sudo apt install python3 python3-pip -y
    ```

3. **Install Dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```
    
4. **Run the Script:**

    ```bash
    python3 s3_list_script.py
    ```
---

## 📁 Output Example

S3 Buckets:

- → item-bucket-1
- → item-bucket-2

---

## 🧑‍💻 Author

Abdullah bin Amin

[LinkedIn](https://www.linkedin.com/in/abdullahbinamin/)

[GitHub](https://github.com/AbdullahbinAmin)

---

## 📜 License

This project is open-sourced under the MIT License.

---