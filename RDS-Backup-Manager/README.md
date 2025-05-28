# 🚀 AWS RDS Automation using Python (Boto3)

This project demonstrates how to automate common Amazon RDS tasks using Python and the Boto3 SDK.

---

## 📘 Python Automation for AWS RDS

🎯 **Objective**: To automate AWS RDS tasks using Python.

In this lab, you will:
* Create a new Amazon RDS instance.
* Create a manual backup (snapshot) of that instance.

---

## 🧠 What is AWS RDS?

Amazon RDS (Relational Database Service) is a managed service by AWS that helps you set up, operate, and scale relational databases in the cloud.

✅ **Key Features**:
* **Database Engines**: Supports MySQL, PostgreSQL, SQL Server, Oracle, and Amazon Aurora.
* **Managed Service**: AWS manages patches, backups, and scaling.
* **High Availability**: Multi-AZ deployment and automatic failover.
* **Security**: Offers encryption, IAM roles, and network isolation.
* **Scalability**: Easily increase instance size or use read replicas.
* **Backups**: Daily automatic backups and manual snapshots.
* **Monitoring**: Integrated with Amazon CloudWatch.

---

## 🧰 Prerequisites

Before starting:
* You must have an AWS account with admin access.
* AWS CLI and Python (preferably Python 3) should be installed.
* You must have completed previous labs.
* Install Boto3: Python SDK to interact with AWS:
    ```bash
    pip install boto3
    ```

---

## 🔧 PART 1: Creating an RDS Instance using Python (Boto3)

▶️ **File**: `create_rds_instance.py`

```python
import boto3  # AWS SDK for Python

# Step 1: Create an RDS client to talk to AWS RDS service
rds_client = boto3.client('rds')

# Step 2: Define your RDS database configuration
db_instance_name = 'myrdsinstance'              # Name for the RDS instance
db_instance_class = 'db.t2.micro'               # Type of instance (small & free-tier eligible)
engine = 'mysql'                                # Database engine
master_username = 'adminuser'                   # Master username for DB
master_password = 'SecurePassword123!'          # Master password for DB

# Step 3: Call AWS API to create the RDS instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier=db_instance_name,      # Unique name for RDS instance
    DBInstanceClass=db_instance_class,          # The size/type of the instance
    Engine=engine,                              # The database engine (e.g., mysql)
    MasterUsername=master_username,             # Admin username
    MasterUserPassword=master_password,         # Admin password
    AllocatedStorage=20,                        # Storage size in GB
    MultiAZ=False                               # High availability (False = single zone)
)

# Step 4: Print result
if 'DBInstance' in response:
    print(f"✅ RDS instance '{db_instance_name}' created successfully.")
else:
    print("❌ Error creating RDS instance:", response)

```
Markdown

# 🚀 AWS RDS Automation using Python (Boto3)

This project demonstrates how to automate common Amazon RDS tasks using Python and the Boto3 SDK.

---

## 📘 Lab 4: Python Automation for AWS RDS

🎯 **Objective**: To automate AWS RDS tasks using Python.

In this lab, you will:
* Create a new Amazon RDS instance.
* Create a manual backup (snapshot) of that instance.

---

## 🧠 What is AWS RDS?

Amazon RDS (Relational Database Service) is a managed service by AWS that helps you set up, operate, and scale relational databases in the cloud.

✅ **Key Features**:
* **Database Engines**: Supports MySQL, PostgreSQL, SQL Server, Oracle, and Amazon Aurora.
* **Managed Service**: AWS manages patches, backups, and scaling.
* **High Availability**: Multi-AZ deployment and automatic failover.
* **Security**: Offers encryption, IAM roles, and network isolation.
* **Scalability**: Easily increase instance size or use read replicas.
* **Backups**: Daily automatic backups and manual snapshots.
* **Monitoring**: Integrated with Amazon CloudWatch.

---

## 🧰 Prerequisites

Before starting:
* You must have an AWS account with admin access.
* AWS CLI and Python (preferably Python 3) should be installed.
* You must have completed previous labs.
* Install Boto3: Python SDK to interact with AWS:
    ```bash
    pip install boto3
    ```

---

## 🔧 PART 1: Creating an RDS Instance using Python (Boto3)

▶️ **File**: `create_rds_instance.py`

```python
import boto3  # AWS SDK for Python

# Step 1: Create an RDS client to talk to AWS RDS service
rds_client = boto3.client('rds')

# Step 2: Define your RDS database configuration
db_instance_name = 'myrdsinstance'              # Name for the RDS instance
db_instance_class = 'db.t2.micro'               # Type of instance (small & free-tier eligible)
engine = 'mysql'                                # Database engine
master_username = 'adminuser'                   # Master username for DB
master_password = 'SecurePassword123!'          # Master password for DB

# Step 3: Call AWS API to create the RDS instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier=db_instance_name,      # Unique name for RDS instance
    DBInstanceClass=db_instance_class,          # The size/type of the instance
    Engine=engine,                              # The database engine (e.g., mysql)
    MasterUsername=master_username,             # Admin username
    MasterUserPassword=master_password,         # Admin password
    AllocatedStorage=20,                        # Storage size in GB
    MultiAZ=False                               # High availability (False = single zone)
)

# Step 4: Print result
if 'DBInstance' in response:
    print(f"✅ RDS instance '{db_instance_name}' created successfully.")
else:
    print("❌ Error creating RDS instance:", response)

```
### 📝 Explanation of the Code:

- `import boto3`: Imports AWS SDK for Python to interact with AWS services.
- `boto3.client('rds')`: Creates a client to access RDS services.
- `DBInstanceIdentifier`: The unique name you want to give your RDS instance.
- `DBInstanceClass`: Type of compute and memory capacity (e.g., db.t2.micro).
- `Engine`: Database engine type (e.g., MySQL, PostgreSQL).
- `MasterUsername`: Admin login name to access the database.
- `MasterUserPassword`: Admin password. Use strong passwords!
- `AllocatedStorage`: How much disk space (in GB) to assign.
- `MultiAZ`: Choose True for high availability across zones; here, set to False for simplicity.
- `response`: The response from AWS, usually contains data about what was created.

---

## 🔄 PART 2: Triggering a Manual Backup (Snapshot) of the RDS Instance

### ▶️ File: `rds_backup.py`

```Python

import boto3  # AWS SDK for Python

# Step 1: Create RDS client
rds_client = boto3.client('rds')

# Step 2: Define backup snapshot name and DB instance to backup
backup_name = 'myrdsbackup'                  # Custom name for your backup snapshot
db_instance_name = 'myrdsinstance'           # The RDS instance you want to backup

# Step 3: Create manual backup
response = rds_client.create_db_snapshot(
    DBSnapshotIdentifier=backup_name,        # Snapshot name
    DBInstanceIdentifier=db_instance_name    # The DB to back up
)

# Step 4: Print result
if 'DBSnapshot' in response:
    print(f"✅ Manual backup '{backup_name}' created successfully.")
else:
    print("❌ Error creating manual backup:", response)
```

### 📝 Explanation of the Code:

- `create_db_snapshot()`: Creates a manual backup (snapshot) of your RDS instance.
- `DBSnapshotIdentifier`: Unique name for your backup.
- `DBInstanceIdentifier`: The name of the instance to back up.
- `if 'DBSnapshot' in response:`: Checks if the response includes a snapshot object, indicating success.


### ▶️ How to Run the Scripts

Save the Python files:

```
create_rds_instance.py
rds_backup.py
```
Make sure you have credentials set up using aws configure.

Run the script to create the RDS instance:
```Bash
python3 create_rds_instance.py
```
Wait a few minutes until the instance is fully available.

Run the backup script:
```Bash
python rds_backup.py
```

### ✅ Best Practices
- Always check the response to handle errors.
- Use try-except blocks to catch exceptions in production scripts.
- Avoid hardcoding sensitive credentials like usernames or passwords.
- Tag your RDS resources for better organization.
- Monitor snapshots and storage usage.

### 🔧 Features (Summary)
- Create a new RDS instance using Python
- Trigger manual backups (snapshots)
- Error checking and AWS response handling

### 📦 Requirements (Summary)
- Python 3+
- AWS CLI configured (aws configure)
- boto3 Python package
- Install Boto3:

```Bash
pip install boto3
```

### 🚀 Usage (Summary)

Create an RDS instance:
```Bash
python3 create_rds_instance.py
```
Trigger a manual backup (snapshot):

```Bash
python rds_backup.py
```

### 📁 Files
- `create_rds_instance.py`: Script to create a MySQL RDS instance.
- `rds_backup.py`: Script to create a manual snapshot of the instance.

---

## 🧑‍💻 Author

Abdullah bin Amin

[LinkedIn](https://www.linkedin.com/in/abdullahbinamin/)

[GitHub](https://github.com/AbdullahbinAmin)

---

## 📜 License

This project is open-sourced under the MIT License.

---