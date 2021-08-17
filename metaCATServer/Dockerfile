FROM python:3.7

WORKDIR /app

RUN apt update
RUN apt install build-essential

RUN python -m pip install --upgrade pip
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 2100

CMD ["python", "meta_cat_server.py"]