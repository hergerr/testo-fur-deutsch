# App for learning german vocabulary and grammar

### Main requirements

1. Checking for duplicate when adding new question
2. Two categories: *Rektion des Verbs* and *Vokabular*
3. Mobile and web app
4. Implementing amenities like combo boxes for choosing *Fallen* and *Artikeln*

### Side features

1. Smart measuring level of mastery of each question set, and asking least mastered questions more frequently



### Dockerized app (current state)

```bash
# if you want to delete volumes
docker-compose down -v

docker-compose up

# get into app container and run migrations
docker exec -it testo-fur-deutsch_web_1 bash
python3 manage.py migrate

# create superuser
python3 manage.py createsuperuser
```



### Non dockerized app knowledge base:

Install postgress related stuff, create database with YOUR OWN credential (then type then in *secret.py*, ignored credentials file)

```bash
sudo apt-get install postgresql
sudo apt-get install python-psycopg2
sudo apt-get install libpq-dev

# create database in psql shell. Remember that postgres doesnt recognize case
sudo -i -u postgres # switch user
psql  # enter shell
CREATE DATABASE checkerdb;
CREATE USER checkerUser WITH PASSWORD 'password';
ALTER ROLE checkerUser SET client_encoding TO 'utf8';
ALTER ROLE checkerUser SET default_transaction_isolation TO 'read committed';
ALTER ROLE checkerUser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE checkerDB TO checkerUser;

# if no venv create it. Then install requiremets
# python3 -m venv venv

pip3 install -r requirements.txt

# run migrations in app root directory

python3 manage.py migrate

# try to run app

python3 manage.py runserver
```

### Planned tech stack

- API
  - Rest framework:  **Django Rest Framework**,
  - DBMS - **Postgres**
  - Docker
- Mobile:
  - React Native/Kotlin/Java/Flutter (not yet decided)
- Web
  - React

### Curl wiki:
- register: curl -X POST -d '{"username": "fred","password": "adminadmin"}' -H 'Content-Type: application/json'  localhost:8000/auth/users/
- login: curl -X POST -d '{"username": "fred","password": "adminadmin"}' -H 'Content-Type: application/json' localhost:8000/api/auth/token/login/
- get all words: curl -X GET localhost:8000/words/
- get certain word: curl -X GET localhost:8000/words/1/
- when view has limited visibility: curl -X GET -H  'Authorization: Token 6e30a5d59cdde84208133b8e68ce6cad92f9e4f2' localhost:8000/words/1/
- add learning set state: curl -X POST -H  'Authorization: Token 6e30a5d59cdde84208133b8e68ce6cad92f9e4f2' -d '{"learning_set": "2", "number_of_obligaory_rounds":"20"}' -H 'Content-Type: application/json' localhost:8000/get_my_views/
- get certain user's learning states: curl -X GET -H  'Authorization: Token 6e30a5d59cdde84208133b8e68ce6cad92f9e4f2' -H 'Content-Type: application/json' localhost:8000/get_my_views/