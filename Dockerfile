FROM python:alpine

WORKDIR /number_guess

COPY . .

CMD ["python", "main.py"]