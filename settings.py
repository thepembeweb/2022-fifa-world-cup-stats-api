import os
from dotenv import load_dotenv

load_dotenv()

ALGORITHMS = os.getenv('ALGORITHMS')
API_AUDIENCE = os.getenv('API_AUDIENCE')
AUTH0_DOMAIN = os.getenv('AUTH0_DOMAIN')
CAPTURER_TOKEN = os.getenv('CAPTURER_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_TEST_URL = os.getenv('DATABASE_TEST_URL')
REVIEWER_TOKEN = os.getenv('REVIEWER_TOKEN')
SUPERVISOR_TOKEN = os.getenv('SUPERVISOR_TOKEN')
