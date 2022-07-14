# Wiki Citi Bot

Tests django-project.

## Start service with Docker

Start Service in docker container:

0. Copy `.env.dev` file to `.env` and correct variables

0. Start Service container:

    ```
    $ docker-compose -f docker-compose.yml up -d
    ```

## Postgres Docker

Start PostgresDB in docker container:

0. Copy `.env.local` file to `.env` and correct variables if not yet

0. Start Postgres container:

    ```
    $ docker-compose up -d wiki-citi-bot-pg
    ```

## Virtual Environment

0. Create Virtual Environment

    ```
    $ sudo apt install python3-pip python3-venv
    $ python3 -m venv .venv
    ```

0. Activate Virtual Environment

    ```
    source .venv/bin/activate
    ```

0. Install requirements

    ```
    (.venv)$ pip install -r requirements.txt
    ```

0. Copy `.env.example` file to `.env` and correct variables if not yet

## Run

Before running the app upgrade a DB:

```
(.venv) $ python manage.py migrate
```

Run the app with:

```
(.venv) $ python manage.py runserver
```