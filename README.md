cloudmap-api
============

A simple demo app to show how AWS Cloud Map can be used for endpoint discovery. The SAM template deploys an API Gateway and Lambda function that return Cloud Map details about a service.


Installation
------------


You need to precreate a Cloud Map Namespace and Service before deployment. Next, you can deploy the app using the AWS SAM CLI ('sam deploy -g'). During this step, you will be asked to submit the name of the service and namespace.

Once deployment has finished, you can make a request to the API Gateway endpoint, which will return the service details in JSON. 



Contact
-------

In case of questions or bugs, please raise an issue or reach out to @marekq!
