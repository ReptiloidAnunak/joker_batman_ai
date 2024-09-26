from openai import OpenAI

from app.functions import get_character_for_answer
from settings import API_KEY


def test_1():
    client = OpenAI(api_key=API_KEY)
    user_question = 'How are you, my friend?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Batman'
    assert response is not None


def test_2():
    client = OpenAI(api_key=API_KEY)
    user_question = 'How to become strong like you?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Batman'
    assert response is not None


def test_3():
    client = OpenAI(api_key=API_KEY)
    user_question = 'You serve to the good'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Batman'
    assert response is not None


def test_4():
    client = OpenAI(api_key=API_KEY)
    user_question = 'Your save Gotham City and struggle for its security'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Batman'
    assert response is not None


def test_5():
    client = OpenAI(api_key=API_KEY)
    user_question = 'How can I help you?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Batman'
    assert response is not None


def test_6():
    client = OpenAI(api_key=API_KEY)
    user_question = 'Why are you so vile and so crazy?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Joker'
    assert response is not None


def test_7():
    client = OpenAI(api_key=API_KEY)
    user_question = 'Do you like to kill?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Joker'
    assert response is not None


def test_8():
    client = OpenAI(api_key=API_KEY)
    user_question = 'You are criminal'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Joker'
    assert response is not None


def test_9():
    client = OpenAI(api_key=API_KEY)
    user_question = 'How you rob a bank?'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Joker'
    assert response is not None


def test_10():
    client = OpenAI(api_key=API_KEY)
    user_question = 'You look like a drug addict'
    print('\nUSER: ', user_question)
    character = get_character_for_answer(client, user_question)
    response = character.answer_users_question(user_question)
    print(f"\n{character.name}:", response)
    assert character.name == 'Joker'
    assert response is not None