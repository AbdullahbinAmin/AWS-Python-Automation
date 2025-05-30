# Importing Boto3, the AWS SDK for Python
import boto3

# Create a client to talk to the Elastic Load Balancing (ELBv2) service
client = boto3.client('elbv2', region_name='eu-north-1')

# Define a function that creates a load balancer
def create_application_load_balancer(name, subnets):
    # Call AWS to create the load balancer
    response = client.create_load_balancer(
        Name=name,            # Name of your load balancer
        Subnets=subnets,      # List of subnet IDs where ALB will be created
        Type='application'    # Specify that we are creating an Application Load Balancer (ALB)
    )

    # Return the response from AWS
    return response

# Provide your input values
lb_name = 'FlaskELB'  # Choose a name for your ALB
subnets_list = ['subnet-0edd12c58832ac119', 'subnet-0adb676ddf93ac234']  # Replace with real subnet IDs


# Call the function and store the response
response = create_application_load_balancer(lb_name, subnets_list)

# Print the Load Balancer's unique ARN (Amazon Resource Name)
print(response['LoadBalancers'][0]['LoadBalancerArn'])