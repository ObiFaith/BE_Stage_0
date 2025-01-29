from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
  utc_data_time = datetime.now(timezone.utc)
  iso_utc_date_time = utc_data_time.isoformat()

  return {
    "email": "obifth@gmail.com",
    "current_datetime": iso_utc_date_time,
    "github_url": "https://github.com/ObiFaith/BE_Stage_0"
  }
