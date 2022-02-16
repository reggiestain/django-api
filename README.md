# django-api

docker build
docker-compose build
docker-compose run app sh -c "django-admin startproject app ."
docker-compose run app sh -c "python3 manage.py test"
docker-compose run app sh -c "python3 manage.py makemigrations core"
