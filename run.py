import json
import os
from datetime import datetime
from openai import OpenAI

from answer_user_question import answer_user_question
from settings import API_KEY, JOKER, BATMAN, DATA_BASE_JSON
from character import Character


def run_app():
    client = OpenAI(api_key=API_KEY)
    answer_user_question(client)



if __name__ == '__main__':
    run_app()