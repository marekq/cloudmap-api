import boto3, json, os

# setup session with sessiondiscovery (cloudmap)
cd      = boto3.client('servicediscovery')

# import service and endpoint name from env variables
nasp_name  =  os.environ['NamespaceName']
serv_name  =  os.environ['ServiceName']

# start main lambda handler
def handler(event, context):

    resp = []

    print(event)
    print(type(event))
    
    # get the url path
    path    = str(event['rawPath']).strip('/')
    print("received " + path)

    # discover available instances in the namespace
    inst = cd.discover_instances(
            NamespaceName   = nasp_name,
            ServiceName     = serv_name
        ) 

    # return only the dns name if /dns is the path
    if path == "dns":
        resp = json.dumps(inst['Instances'][0]['Attributes']["AWS_INSTANCE_CNAME"])

    # return all properties for all other paths
    else:
        resp = json.dumps(inst['Instances'])

    # return a JSON with the contents
    x = {
        "statusCode": 200,
        "body": resp,
        "headers": {"Content-Type": "application/json"}
    }

    print(x)
    return x
