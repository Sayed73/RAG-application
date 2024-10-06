from fastapi import FastAPI
# import uvicorn
from dotenv import load_dotenv
load_dotenv('.env')

from routes import base

app = FastAPI()

app.include_router(base.base_router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)