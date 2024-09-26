import json
import os
import subprocess
import time
import typer

from colorama import Back, Fore, Style
from openai import OpenAI

from app.character import Character
from settings import JOKER, BATMAN, DATA_BASE_JSON


def get_character_for_answer(client: OpenAI, user_question) -> Character:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "you are psychologist"},
            {
                "role": "user",
                "content": f'analyze the text tone and return only "positive" or "negative": {user_question}'
            }
        ]
    )

    tone = f"{completion.choices[0].message.content}"
    print("Tone: ", tone)
    if tone.lower() == 'negative':
        character = Character(client, JOKER)
    elif tone.lower() == 'positive':
        character = Character(client, BATMAN)
    else:
        character = Character(client, BATMAN)
    return character


def save_answer_question(question_resp: dict):
    with open(DATA_BASE_JSON, 'r') as file:
        content_lst = json.loads(file.read())
        # print(content_lst)

    content_lst.append(question_resp)

    with open(DATA_BASE_JSON, 'w') as file:
        file.write(json.dumps(content_lst))


def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_chat_history():
    with open(DATA_BASE_JSON, 'r') as file:
        question_answer_dict = json.loads(file.read())
        for dic in question_answer_dict:
            for dt, pair in dic.items():
                print('\n')
                print('User: ', pair[0])
                print(pair[1])
                print('\n')
                print(dt)
                print('________')


def run_tests():
    print(Back.YELLOW + Fore.BLACK + Style.BRIGHT + 'RUN TESTS')
    print(Style.RESET_ALL)
    subprocess.run(['pytest', '-s'])
    input(Back.YELLOW + Fore.BLACK + Style.BRIGHT +  'Print enter to start' + Style.RESET_ALL)
    clear_terminal()

def create_test_n_style(text: str):
    print('\n')
    print(Back.LIGHTBLACK_EX + Fore.LIGHTYELLOW_EX + Style.BRIGHT + text)
    print(Style.RESET_ALL)

def print_app_title():
    print(Back.BLACK + Fore.LIGHTYELLOW_EX + Style.BRIGHT + 'Joker_Batman_AI app')
    print(Style.RESET_ALL)
    time.sleep(3)

def print_start_chat_msg():
    print(Back.BLACK + Fore.LIGHTMAGENTA_EX + Style.BRIGHT + 'Ask something yourself')
    print(Style.RESET_ALL)

def choice_run_tests():
    choice = typer.confirm("Do you want to run tests?")
    if choice:
        typer.echo("Вы выбрали 'Да'")
        return True
    else:
        typer.echo("Вы выбрали 'Нет'")
        return False