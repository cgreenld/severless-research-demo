# severless-research-demo
This is a repo designed to faciliate the testing of a lambda and the impact of SDK startup time on cold start

DynamoTables Used - Purpose
- cgreenSeverlessFlagStore - store flags to compare against homegrown
- cgreenSeverlessProxyFlagStore - store flags from proxy service
- cgreenSeverlessTestResults - store timing results from lambda runs so they can be compared at scale

EC2 Instances Used - Purpose
- testing-relay - ld proxy go app set up without a external data store for proxy into system
- testing-relay-db - ld proxy go app set up with dynamo DB data store set up for deamon mode

Notes From Sync 1
- play with failure modes, you can put a proxy between LD relay and LD, then shut off the network connection
- Maybe explore relay porxy and getting out of sync
- java or c sharp could be an option, node could be an option. Think extension vs iteration 1
- our serverless best practices doc and validating some of the best practices there







# Resources Used
- https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-dependencies
- https://lumigo.io/blog/canary-deployment-with-launchdarkly-and-aws-lambda/
- https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5


AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Description: >
  cgreen_svrls_db_run

  Sample SAM Template for cgreen_svrls_db_run

# More info about Globals: https://github.com/awslabs/serverless-application-model/blob/master/docs/globals.rst
Globals:
  Function:
    Timeout: 3

Resources:
  dbSvrlsRun:
    Type: AWS::Serverless::Function # More info about Function Resource: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction
    Properties:
      FunctionName: cgreen-dbSvrlsRun
      CodeUri: cgreen_svrls_db_run/
      Handler: app.lambda_handler
      Runtime: python3.9
      Architectures:
        - x86_64
      Events:
        HelloWorld:
          Type: Api # More info about API Event Source: https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#api
          Properties:
            Path: /hello
            Method: get

Outputs:
  # ServerlessRestApi is an implicit API created out of Events key under Serverless::Function
  # Find out more about other implicit resources you can reference within SAM
  # https://github.com/awslabs/serverless-application-model/blob/master/docs/internals/generated_resources.rst#api
  dbSvrlsRunApi:
    Description: "API Gateway endpoint URL for Prod stage for Hello World function"
    Value: !Sub "https://${ServerlessRestApi}.execute-api.${AWS::Region}.amazonaws.com/Prod/hello/"
  dbSvrlsRun:
    Description: "Hello World Lambda Function ARN"
    Value: !GetAtt dbSvrlsRun.Arn
  dbSvrlsRunIamRole:
    Description: "Implicit IAM Role created for Hello World function"
    Value: !GetAtt dbSvrlsRun.Arn
