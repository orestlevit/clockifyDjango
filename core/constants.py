import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("URL")
PATH_FOR_USER = os.getenv("URL") + "user"
API_KEY = os.getenv("CLOCKIFY_API")
WORKSPACE_ID = os.getenv("WORKSPACE_ID")
USER_ID = os.getenv("USER")
PATH_FOR_TIME_ENTRY = URL + f"workspaces/{WORKSPACE_ID}/user/{USER_ID}/time-entries"
REPORT_URL = os.getenv("REPORT_URL")
PATH_FOR_TOTAL_DURATIONS = REPORT_URL + f"workspaces/{WORKSPACE_ID}/reports/summary"
