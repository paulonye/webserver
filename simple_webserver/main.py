from fastapi import FastAPI, Query, Response
import csv
import json
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from fastapi.responses import StreamingResponse


app = FastAPI()

@app.get("/transactions")
def get_data(rows: int = Query(...)):
	with open('acc_records.csv', 'r') as file:
		data = csv.reader(file)
		header = next(data)
		response = [row for count, row in enumerate(data) if count < rows]

	return response

@app.get("/orders")
def get_orders():
	engine = create_engine('postgresql://root:root@localhost:5432/root')
	df = pd.read_sql("SELECT * from public.transactions LIMIT 2", con = engine)
	response = df.to_dict()

	return response

@app.get("/transactions/download_data")
def download_data(rows: int = Query(...)):
    final_result = get_data(rows)
    csv_data = "\n".join([",".join(row) for row in final_result])
    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="data.csv"'
    
    return response



if __name__ == '__main__':
	get_data(2)
			
