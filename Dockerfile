FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["sh", "-c", "python api_work/manage.py migrate && python api_work/manage.py runserver 0.0.0.0:8000"]