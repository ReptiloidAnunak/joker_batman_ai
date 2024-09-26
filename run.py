
from openai import OpenAI

from app.answer_user_question import answer_user_question
from app.functions import run_tests, print_app_title, print_start_chat_msg, choice_run_tests
from settings import API_KEY


def run_app():
    client = OpenAI(api_key=API_KEY)
    print_app_title()

    if choice_run_tests():
        run_tests()

    else:
        print_start_chat_msg()

    try:
        answer_user_question(client)
    except KeyboardInterrupt:
        if choice_run_tests():
            run_tests()


if __name__ == '__main__':
    run_app()