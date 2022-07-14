FROM python:3.8

ENV PYTHONDOTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/wiki_citi_bot

RUN python3 -m venv /opt/venv

COPY ./requirements.txt /usr/src/requirements.txt
RUN /opt/venv/bin/python -m pip install --upgrade pip
RUN /opt/venv/bin/pip install wheel
RUN /opt/venv/bin/pip install psycopg2
RUN /opt/venv/bin/pip install -r /usr/src/requirements.txt

COPY . /usr/src/wiki_citi_bot

EXPOSE 8000
CMD ["/opt/venv/bin/python", "manage.py", "migrate"]
CMD ["/opt/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]