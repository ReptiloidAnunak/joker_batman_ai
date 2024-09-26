from datetime import datetime

from functions import get_character_for_answer, save_answer_question, clear_terminal, show_chat_history


def answer_user_question(client):
    while True:
        show_chat_history()
        usr_char_msg_dict = {}
        #
        user_question = input('\n\n\nINPUT: ')
        character = get_character_for_answer(client, user_question)
        response = character.answer_users_question(user_question)

        response_str = f'{character.name}: {response}'

        print('User: ', user_question)
        print(response_str)
        time = datetime.now()
        time_str = time.strftime('%H:%M:%S  %d.%m.%Y')
        # print(time_str)

        usr_char_msg_dict[time_str] = tuple([user_question, response_str])
        # print(history_dict)
        save_answer_question(usr_char_msg_dict)
        clear_terminal()