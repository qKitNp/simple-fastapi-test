import os

from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

INDEX_HTML = Path(__file__).parent / "index.html"

@app.get("/")
def read_root():
    return FileResponse(INDEX_HTML)

if __name__ == "__main__":                                                                                               
       import uvicorn                                                                                                       
       port = int(os.environ.get("PORT", 8000))  # ← use $PORT                                                              
       uvicorn.run(app, host="0.0.0.0", port=port)