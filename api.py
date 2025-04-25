from fastapi import FastAPI
from fastapi import UploadFile, File
import pandas as pd

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/scrape")
async def upload_csv(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        return {"error": "File must be a CSV"}
    
    contents = await file.read()
    data = pd.read_csv(pd.compat.StringIO(contents.decode('utf-8')))
    return {"columns": data.columns.tolist()}
