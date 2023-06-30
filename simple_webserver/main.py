from fastapi import FastAPI, Query, Response
import csv
import json
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from fastapi.responses import StreamingResponse


app = FastAPI(title="Sample Real-Time Orders")

@app.get("/transactions")
def get_data(rows: int = Query(...)):
	final_result = {}
	with open('acc_records.csv', 'r') as file:
		data = csv.reader(file)
		header = next(data)
		count = 0
		for row in data:
			if count < rows:
				final_result[count] = row
			count = count + 1
	return final_result

@app.get("/orders")
def get_orders():
	engine = create_engine('postgresql://root:root@localhost:5432/root')
	df = pd.read_sql("SELECT * from public.transactions LIMIT 2", con = engine)
	response = df.to_dict()
	return response

@app.get("/download")
def download_data(rows: int = Query(...)):
    final_result = []
    with open('acc_records.csv', 'r') as file:
        data = csv.reader(file)
        header = next(data)
        count = 0
        for row in data:
            if count < rows:
                final_result.append(row)
                count += 1
    csv_data = "\n".join([",".join(row) for row in final_result])
    #return StreamingResponse(iter([csv_data]), media_type="text/csv")
    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="data.csv"'
    
    return response



if __name__ == '__main__':
	get_orders()
			
