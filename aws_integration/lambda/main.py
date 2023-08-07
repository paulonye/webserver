import json  
import mysql.connector

host = 'student-management-system.crruakemgggf.us-east-1.rds.amazonaws.com'
port = 3306
user = 'admin'
password = 'password123$'
database = 'transactions'

#defining the connection
conn = mysql.connector.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

def get_orders(event, context):

	#parsing out query parameters
	no_of_rows = event['queryStringParameter']['rows']

	# construct body of response object
	cursor = conn.cursor()
	query = f"SELECT * FROM transactions LIMIT {no_of_rows}"
	cursor.execute(query)
	#this returns a list object
	data = cursor.fetchall()

	# construct http response object
	responseObject = {}
	responseObject['statusCode'] = 200
	responseObject['headers'] = {}
	responseObject['headers']['Content-Type'] = 'application/json'
	responseObject['body'] = json.dumps(data)

	# return the response Object
	return responseObject