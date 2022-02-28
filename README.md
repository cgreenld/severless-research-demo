# severless-research-demo
This is a repo designed to faciliate the testing of a lambda and the impact of SDK startup time on cold start

DynamoTables Used - Purpose
- cgreenSeverlessFlagStore - store flags to compare against homegrown
- cgreenSeverlessProxyFlagStore - store flags from proxy service
- cgreenSeverlessTestResults - store timing results from lambda runs so they can be compared at scale






# Resources Used
- https://docs.aws.amazon.com/lambda/latest/dg/python-package.html#python-package-dependencies
- https://lumigo.io/blog/canary-deployment-with-launchdarkly-and-aws-lambda/
