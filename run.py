
from openai import OpenAI
import subprocess
from app.answer_user_question import answer_user_question
from settings import API_KEY

def run_app():
    client = OpenAI(api_key=API_KEY)
    answer_user_question(client)



if __name__ == '__main__':
    run_app()