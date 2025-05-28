# Create a Manual Backup of the RDS Instance
import boto3

# Initialize the RDS Client
rds_client = boto3.client('rds')

backup_name = 'dbDbackup'
db_instance_name = "database"

backup_response = rds_client.create_db_snapshot(
    DBSnapshotIdentifier = backup_name,
    DBInstanceIdentifier = db_instance_name
)

# Check the response for errors
if 'DBSnapshot' in backup_response:
    print(f"Manaula Backup '{backup_name}' Created Successfully.")
else:
    print(f"Failed to Create Manual Backup: {backup_response}")
