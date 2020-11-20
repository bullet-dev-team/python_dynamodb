from package.MovieTable import create_movie_table, put_item
import boto3
from boto3.dynamodb.conditions import Key
from flask import Flask, request, render_template,jsonify

application = Flask(__name__)

@application.route('/')
def home():
  return render_template('home.html')

@application.route('/add', methods=['GET','POST'])
def add_movie():
  client = boto3.client('dynamodb')

  # crate table if not exists
  table_name = 'Movies'
  existing_tables = client.list_tables()['TableNames']
  if table_name not in existing_tables:
    create_movie_table(table_name)
  movie = request.form['movie']

  # put movie record
  put_item(table_name, movie)
  return 'succeed'

@application.route('/list_movies', methods=['GET'])
def list_movies():
  return render_template('movies.html')

@application.route('/list', methods=['GET','POST'])
def query():
  dynamodb = boto3.resource('dynamodb')
  table_name = 'Movies'
  table = dynamodb.Table(table_name)
  item = table.query(
      KeyConditionExpression=Key('year').eq(2020)
  )
  result = {
    "result": str(item['Items'])
  }
  result = {str(key): value for key, value in result.items()}
  return jsonify(result=result)

if __name__ == '__main__':
  application.run(debug=True)