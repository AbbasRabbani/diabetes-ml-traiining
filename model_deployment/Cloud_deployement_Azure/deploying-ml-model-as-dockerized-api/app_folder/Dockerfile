FROM python:3.11.9-slim

#Copy everything in Docker file directory

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
