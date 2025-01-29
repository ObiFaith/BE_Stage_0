from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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
