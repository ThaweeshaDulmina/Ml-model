FROM python:3.9-slim

WORKDIR /app

COPY requriment.txt .
RUN pip install -r requriment.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]