import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

table = dynamodb.create_table(
    TableName='bitstamp',
    KeySchema=[
        {'AttributeName': 'symbol', 'KeyType': 'HASH'},
        {'AttributeName': 'time', 'KeyType': 'RANGE'}
    ],
    AttributeDefinitions=[
        {'AttributeName': 'symbol', 'AttributeType': 'S'},
        {'AttributeName': 'time', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
print("Table status:", table.table_status)
