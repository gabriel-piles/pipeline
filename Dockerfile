FROM python:3.7-alpine3.8
WORKDIR /code
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV GRAYLOG_IP circle_ci_change_value


RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

RUN apk update

RUN apk add --update --no-cache g++ gcc libxslt-dev musl-dev python3-dev linux-headers libffi-dev libressl-dev chromium chromium-chromedriver

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]