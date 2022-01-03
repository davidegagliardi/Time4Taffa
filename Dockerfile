FROM python:3

COPY . /app

RUN pip3 install -r /app/requirements.txt

RUN pip3 install auxlib conda

CMD [ "python", "./app/main.py" ]