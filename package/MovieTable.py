import boto3

def create_movie_table(tableName):
  dynamodb = boto3.resource('dynamodb')

  table = dynamodb.create_table(
      TableName=tableName,
      KeySchema=[
        {
          'AttributeName': 'year',
          'KeyType': 'HASH'  # Partition key
        },
        {
          'AttributeName': 'title',
          'KeyType': 'RANGE'  # Sort key
        }
      ],
      AttributeDefinitions=[
        {
          'AttributeName': 'year',
          'AttributeType': 'N'
        },
        {
          'AttributeName': 'title',
          'AttributeType': 'S'
        },

      ],
      ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
      }
  )

  table.wait_until_exists()

  return table
