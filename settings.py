import json
import os
from dotenv import load_dotenv

load_dotenv()
ROOT_DIR = os.path.abspath(os.path.dirname(__file__))

API_KEY = os.environ.get('API_KEY')

JOKER = "Joker"
BATMAN = "Batman"

DATA_BASE_DIR = os.path.join(ROOT_DIR, 'data_base')
DATA_BASE_JSON = os.path.join(DATA_BASE_DIR, 'chat_history.json')

if not os.path.exists(DATA_BASE_DIR):
    os.mkdir(DATA_BASE_DIR)

if not os.path.exists(DATA_BASE_JSON):
    with open(DATA_BASE_JSON, 'w') as file:
        file.write(json.dumps([]))
