FROM python:3.9.20-slim

WORKDIR /home/app

COPY bot bot
COPY main.py .
COPY req.txt .

RUN pip install -r req.txt


CMD [ "python", "main.py" ]