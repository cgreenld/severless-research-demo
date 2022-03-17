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

