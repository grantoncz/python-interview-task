
FROM python:3.9.6

WORKDIR /app

COPY requirements.txt ./

RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python ./text_classifier.py
