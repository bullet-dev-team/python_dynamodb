from package.MovieTable import create_movie_table
import os
import json

def application(environ, start_response):
  table = create_movie_table()
  response = {
    'envVar': os.getenv('NAME'),
    'tableStatus': table.table_status
  }
  start_response("200 OK", [
    ("Content-Type", "application/json")
  ])
  return [json.dumps(response).encode('utf-8')]



