FROM python:3.13

WORKDIR /app

COPY requriemes.txt .

RUN pip install -r requriemes.txt

COPY . .

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]