FROM python:3.8.1-slim-buster as app
LABEL maintainer="ERICK GUBI <egubi@vmware.com>"

WORKDIR /main

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

COPY . .


EXPOSE 5000


# CMD ["gunicorn", "-c", "python:config.gunicorn", "main.app:create_app()"]

CMD ["python","main/app.py"]