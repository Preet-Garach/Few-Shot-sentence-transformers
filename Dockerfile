FROM python:3.8.10

RUN apt update -y && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install git+https://github.com/pmbaumgartner/setfit

RUN pip install requirements.txt

CMD ["python3","main.py"]