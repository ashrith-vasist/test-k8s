FROM python:3.9-slim

WORKDIR /K8s

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py", "runserver"]