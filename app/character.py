from openai import OpenAI


class Character:
    def __init__(self, client: OpenAI, name: str) -> str:
        self.name = name
        self.gpt_role_instruction = self._create_character_instruction_for_gpt()
        self.client = client

    def _create_character_instruction_for_gpt(self) -> str:
        instruction = f'You are {self.name} from Marvel. You answer to user and ask him something'
        return instruction

    def answer_users_question(self, user_question: str) -> str:
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": self.gpt_role_instruction},
                {
                    "role": "user",
                    "content": f'answer: {user_question}'
                }
            ]
        )
        response = f"{completion.choices[0].message.content}"
        return response
