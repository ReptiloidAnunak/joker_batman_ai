FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN pytest

CMD ["python", "run.py"]