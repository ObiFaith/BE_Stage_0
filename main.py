from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=["*"],  # Limit to necessary HTTP methods
  allow_headers=["Authorization", "Content-Type"],
  allow_credentials=True,
)

class ApiResponse(BaseModel):
  email: str
  current_datetime: str
  github_url: str

@app.get('/', response_model=ApiResponse)
def index():
  utc_data_time = datetime.now(timezone.utc)
  iso_utc_date_time = utc_data_time.isoformat()

  return ApiResponse(
    email="obifth@gmail.com",
    current_datetime=iso_utc_date_time,
    github_url="https://github.com/ObiFaith/BE_Stage_0"
  )
