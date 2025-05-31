from aws_cdk import core
from aws_cdk import aws_s3 as s3
from aws_cdk import aws_lambda as _lambda

class AwsCdkIaCStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self,
            "MyFirstBucket",
            versioned=True,
            removal_policy=core.RemovalPolicy.DESTROY
        )

        # Create a Lambda function
        lambda_function = _lambda.Function(self, "PythonAutomationLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="index.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        # Grant Lambda read/write access to the S3 bucket
        bucket.grant_read_write(lambda_function)
