# **Joker_Batman_AI**
https://github.com
### **Описание**

GPT-чат, определяющий тональность сообщения пользователя.<br>
Если пользователь отправляет позитивное или нейтральное сообщение, ему отвечает Бэтман, если негативное - Джокер.<br>
В конце сообщения ИИ задает пользователю вопрос в контексте его сообщения.
Каждый раз история чата сохраняется и обновляется на экране терминала.

Вам будет предложено запустить тесты при запуске приложения и при выходе из чата с ботом.
Для выхода из чата с ботом и приложения нажмите CTRL+C или закройте терминал.


## Запуск

**Стандартный запуск**
<br>
1. Запустите команду установки виртуального окружения `python3 -m venv .venv`<br>
2. Актвируйте виртуальное окружение 
Linux/Mac: `source .venv/bin/activate`<br>
Windows (Command Prompt): `.venv\Scripts\activate`<br>
Windows (PowerShell): `.venv\Scripts\Activate.ps1`<br>
<br>
3. Установите необходимые библиотеки
`pip install -r requirements.txt`<br>
4. Запустите код `python run.py`
<br><br>

**Запуск с помощью Docker**

Если на вашем компьютере не установлен Docker, скачайте его по инструкции на [официальном сайте](https://www.docker.com/get-started/)

1. Убедитесь, что вы находитесь в корневой директории, где расположен [Dockerfile](Dockerfile)<br>Запустите команду сбора докер-контейнера `docker build -t joker_batman_ai .`
2. Запустите докер-контейнер<br>`docker run --restart unless-stopped -d --name joker_batman_ai_container joker_batman_ai && docker logs -f joker_batman_ai_container`