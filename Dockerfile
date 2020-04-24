FROM python:3

MAINTAINER venkey "venkeymee@gmail.com"

RUN apt-get update && apt-get install -y python3 python3-dev python3-pip nginx

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 8443

ENTRYPOINT [ "python3" ]

CMD [ "app/app.py" ]
