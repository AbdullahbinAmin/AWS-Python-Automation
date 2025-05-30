import boto3  # AWS SDK for Python
import datetime  # Used to define the time range

# Step 1: Connect to CloudWatch
cloudwatch_client = boto3.client('cloudwatch', region_name = 'eu-north-1')

# Step 2: Name of the load balancer you're monitoring
elb_name = 'FlaskELB'  # Replace this with your actual ELB name

# Step 3: Set the time range for monitoring (last 24 hours)
end_time = datetime.datetime.utcnow()  # Current time
start_time = end_time - datetime.timedelta(hours=1)  # 24 hours ago

# Step 4: Choose the metric to monitor
metric_name = 'RequestCount'  # How many requests passed through the ELB

# Step 5: Define the "dimensions" (metadata) for this metric
dimensions = [
    {
        'Name': 'LoadBalancerName',  # We're filtering data by Load Balancer name
        'Value': elb_name
    },
]

# Step 6: Request the metric data from CloudWatch
response = cloudwatch_client.get_metric_data(
    MetricDataQueries=[
        {
            'Id': 'm1',  # An identifier for this metric query
            'MetricStat': {
                'Metric': {
                    'Namespace': 'AWS/ELB',         # Metric group: ELB classic (not ALB)
                    'MetricName': metric_name,       # We're tracking RequestCount
                    'Dimensions': dimensions         # Which ELB to get data for
                },
                'Period': 300,  # Time in seconds: 300 = 5-minute intervals
                'Stat': 'Sum',  # We want the total number of requests per period
            },
            'ReturnData': True,  # We want the data returned
        },
    ],
    StartTime=start_time,  # Start of time range
    EndTime=end_time,      # End of time range
)

# Step 7: Print the raw metric data
print("Metric Data:", response['MetricDataResults'])

# OPTIONAL: Print each datapoint (time and request count)
# Note: CloudWatch's get_metric_data doesn't return 'Datapoints' key. This part may not work.
# Correct method would loop over 'MetricDataResults' values and timestamps.

for result in response['MetricDataResults']:
    for time, value in zip(result['Timestamps'], result['Values']):
        print(f"Time: {time}, Request Count: {value}")
