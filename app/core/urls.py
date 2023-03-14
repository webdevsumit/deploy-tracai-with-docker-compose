from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', helloWorld, name='helloWorld'),
]

'''
SERVER
    For UnknownChats
    ssh ec2-user@ec2-15-206-73-113.ap-south-1.compute.amazonaws.com
    For Rentyug
    ssh -i "my-hp.pem" ec2-user@ec2-3-109-205-56.ap-south-1.compute.amazonaws.com

# SOME IMPORTANT DOCKER GUIDE

To see the space - The extra spce consumed by the old images which are not in use
    docker system df

To delete those images, congainers, etc.
    docker volume prune
    docker container prune
    docker image prune
    docker network prune

    To clear build cache
    docker builder prune

all above by
    docker system prune

    all other
    docker system prune -a
    
    All of these have a --help option.
    https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes

Docker commands to build app without loosing database and without deps/logs
    docker-compose -f docker-compose-deploy.yml build app
    docker-compose -f docker-compose-deploy.yml up --no-deps -d app

Rnning Django commands or docker command to run django commands like makemigrations...
    docker-compose -f docker-compose-deploy.yml run --rm app sh -c "python manage.py makemigrations"
    docker-compose run --rm app sh -c "python manage.py makemigrations"


'''













