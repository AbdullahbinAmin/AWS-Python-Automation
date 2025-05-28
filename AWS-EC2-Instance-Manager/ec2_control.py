import boto3
import datetime

# Initialize the EC2 and CloudWatch Clients
ec2 = boto3.client('ec2')
cw = boto3.client('cloudwatch')

# Define the instance ID of the EC2 Instance to manage
instance_id = "i-04ed4786f71568dea"

# Function to start the EC2 Instance
def start_instance():
    ec2.start_instances(InstanceIds=[instance_id])
    print(f"Starting EC2 Instance with ID: {instance_id}")

# Function to stop the EC2 Instance
def stop_instance():
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"Stopping EC2 Instance with ID: {instance_id}")

# Function to Get CPU Utilization of the EC2 Instance
def get_cpu_utilization():
    metric_name = "CPUUtilization"
    namespace = "AWS/EC2"
    period = 300  # in seconds, e.g., 5 minutes

    # Dimensions must be a list of dictionaries
    dimensions = [
        {
            'Name': 'InstanceId',  
            'Value': instance_id
        }
    ]

    # AWS requires datetime objects for StartTime and EndTime
    end_time = datetime.datetime.utcnow()
    start_time = end_time - datetime.timedelta(hours=1)  # 1 hour ago

    response = cw.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': namespace,      
                        'MetricName': metric_name,   
                        'Dimensions': dimensions     
                    },
                    'Period': period,                
                    'Stat': 'Average'
                },
                'ReturnData': True
            }
        ],
        StartTime=start_time,
        EndTime=end_time,
        ScanBy='TimestampDescending'
    )

    if 'MetricDataResults' in response:
        datapoints = response['MetricDataResults'][0]['Values']
        if datapoints:
            print(f"Average CPU Utilization: {datapoints[-1]}%")
        else:
            print("No CPU Utilization Data Available.")
    else:
        print("Unable to fetch CPU Utilization Data.")

# Main Function
def main():
    while True:
        action = input("Enter the Action that you want: \n"
                       "1. 'start'   ---> To Start the Instance\n"
                       "2. 'stop'    ---> To Stop the Instance\n"
                       "3. 'monitor' ---> To Check the CPU Utilization\n"
                       "4. 'exit'    ---> To Quit:\n\n"
                       "Please Enter: ")

        if action == 'start':
            start_instance()
        elif action == 'stop':
            stop_instance()
        elif action == 'monitor':
            get_cpu_utilization()
        elif action == 'exit':
            print("Exiting the script. Goodbye!")
            break
        else:
            print("Invalid Action! Please Enter 'start', 'stop', 'monitor', or 'exit'.")

# Entry point
if __name__ == "__main__":
    main()