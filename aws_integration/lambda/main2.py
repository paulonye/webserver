from os import getenv
import json  
import mysql.connector
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

load_dotenv()

host = getenv('db_HOST')
port = 3306
user = getenv('db_USER')
password = getenv('PASSWORD')
database = getenv('DATABASE')

conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

@app.get("/orders")
def get_orders():

	cursor = conn.cursor()

	# SQL query to retrieve data
	query = "SELECT * FROM transactions LIMIT 3"

	# Execute the query
	cursor.execute(query)

	data = cursor.fetchall()

	# construct body of response object

	# construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = data

	# return the response Object
	print(responseObject)
	return responseObject



if __name__ == '__main__':
	get_orders(2,3)

			



