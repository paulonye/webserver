import requests
import json
from time import sleep

def load_data():
	data = requests.get('http://127.0.0.1:8000/transactions?rows=2').json()
	print(data)

def load_data_db():
	data = requests.get("http://localhost:8080/orders").json()
	print(data)

if __name__ == '__main__':
	load_data_db()