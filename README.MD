# "Smart Course Picker" -- background application

## Breif Introduction of the application
The background application serves as an AWS Lambda function and will run every 3 minutes triggered by the AWS Event bridge. The background application interacts with the AWS DynamoDB to access the data and do statistical analysis on the data and export the statistical result diagram to the S3 for the main application to display. In this way, we can reduce the computational cost for the statistical analysis since the program related to statistical analysis is moved to a background process and is not affected by how many users are using the application.


## Instructions
To run on the AWS Lambda Function, Open the AWS_LAMBDA_READY folder and follow the instructions below:
1) Upload the main program AWS_LAMBDA_READY_GRAPHER to the Lambda as the Lambda Function.
2) Use the AWSLambda-Python37-SciPy1x as the first layer.
3) Upload and use the dependency AWS_LAMBDA_READY_GRAPHER_LAYER as the second layer.
4) Configure and apply the appropriate IAM. 
5) (Optional) Configure the EventBridge for fix interval schedule
   i)  Choose the fix schedule interval
   ii) Choose the Lambda function

Developed by:
    Liren (Fred) Pan,
    Yixiao (Felix) Hong,
    Hongzheng  (Chris) Xu.
