import boto3

# Initialize the RDS Client
rds_client = boto3.client("rds")

# Define the Parameters for your RDS Instance
db_instance_name = "database"
db_instance_class = "db.t3.micro"
engine = "mysql"
master_username = "Abdullah"
master_password = ""  # NEVER push real passwords to GitHub!

# Create the RDS Instance
response = rds_client.create_db_instance(
    DBInstanceIdentifier=db_instance_name,
    DBInstanceClass=db_instance_class,
    Engine=engine,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    AllocatedStorage=20,  # Specify the Storage Size in GB
    MultiAZ=False  # Corrected parameter spelling
)

# Check the response for Errors
if 'DBInstance' in response:
    print(f"RDS Instance {db_instance_name} Created Successfully.")
else:
    print(f"Failed to Create RDS Instance: {response}")