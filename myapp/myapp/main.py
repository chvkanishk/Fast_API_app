from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json

app = FastAPI(title= "First app",description="returning a JSON file")

@app.get("/JSON_File")
async def get_data():
    with open('data.json') as df:
        data = json.load(df)
    return JSONResponse(content=data)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1",port=8000)