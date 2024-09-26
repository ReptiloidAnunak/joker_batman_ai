import json
import os

from openai import OpenAI

from character import Character
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