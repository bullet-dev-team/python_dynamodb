from package.MovieTable import create_movie_table
import json
import boto3
from boto3.dynamodb.conditions import Key


def application(environ, start_response):
  client = boto3.client('dynamodb')
  dynamodb = boto3.resource('dynamodb')
  tableName = 'Movies'
  table = dynamodb.Table(tableName)
  existing_tables = client.list_tables()['TableNames']
  if tableName not in existing_tables:
    table = create_movie_table(tableName)

  table.put_item(
      Item={
        'year': 2020,
        'title': 'new Movie',
        'info': {
          'plot': 'charpter 1',
          'rating': 10
        }
      }
  )

  item = table.query(
      KeyConditionExpression=Key('year').eq(2020)
  )

  response = {
    'tableStatus': table.table_status,
    'movie': str(item['Items'][0])
  }

  start_response("200 OK", [
    ("Content-Type", "application/json")
  ])

  return [json.dumps(response).encode('utf-8')]
