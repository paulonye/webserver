
import json
from typing import Union
import mysql.connector
from sqlalchemy import create_engine
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, Query, Response, File, UploadFile


app = FastAPI()

@app.get("/transactions")
def get_data(rows: Union[int, None] = 5):
	if rows:
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
def download_data(rows: int = 10):
    final_result = get_data(rows)
    csv_data = "\n".join([",".join(row) for row in final_result])
    response = Response(content=csv_data, media_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="data.csv"'
    
    return response

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    """Uploads a file to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket("quidax_test")
    blob = bucket.blob(file.filename)
    path = Path(file.filename)
    blob.upload_from_filename(path)

    print("Uploaded to bucket")
	
if __name__ == '__main__':
	upload_file("acc_records.csv")
			



