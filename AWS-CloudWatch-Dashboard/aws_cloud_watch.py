# Import Required Libraries
import boto3
import datetime
import json

# Connect to CloudWatch
cloudwatch = boto3.client('cloudwatch', region_name='eu-north-1')

# Set metric details
metric_name = 'CPUUtilization'
namespace = 'AWS/EC2'
instance_id = "i-04ed4786f71568dea"

# Set time range (last 1 hour)
end_time = datetime.datetime.utcnow()
start_time = end_time - datetime.timedelta(hours=1)

# Fetch Metric Data
response = cloudwatch.get_metric_data(
    MetricDataQueries = [
        {
            'Id': 'm1',
            'MetricStat': {
                'Metric': {
                    'Namespace': namespace,
                    'MetricName': metric_name,
                    'Dimensions': [
                        {
                            'Name': 'InstanceId',
                            'Value': instance_id
                        },
                    ]
                },
                'Period': 300,
                'Stat': 'Average',
            },
            'ReturnData': True,
        },
    ],
    StartTime=start_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
    EndTime=end_time.strftime('%Y-%m-%dT%H:%M:%SZ'),
)

# Extract the Metric Values
metric_data = response['MetricDataResults'][0]['Values']

# Print the Values
print("Metric Data Values:")
for value in metric_data:
    print(value)


# Create a dashboard
dashboard_name = 'MyDashboard'
widgets = [
    {
        'type': 'metric',
        'x': 0,
        'y': 0,
        'width': 12,
        'height': 6,
        'properties': {
            'metrics': [
                [namespace, metric_name, 'InstanceId', instance_id],
            ],
            'period': 300,
            'stat': 'Average',
            'region': 'eu-north-1',
        },
    },
]

# Create the Dashboard
cloudwatch.put_dashboard(
    DashboardName=dashboard_name,
    DashboardBody=json.dumps({'widgets': widgets}),
)

