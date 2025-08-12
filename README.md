# electro_shop
# Project consists from some parts:

## postgreSQL (it's about configurations of Docker for PostgreSQL)
## electro_shop (it's a Django REST API)
## frontend

# For install
## 1. Clone the repository
## Uncomment necessary settings in shop_api/.env  
## 2. Use command 'docker-compose up --build' in folder 'electro_shop'

# If you use PostgreSQL or Redis, use command line in terminal
1. sudo /etc/init.d/postgresql stop
2. sudo /etc/init.d/redis-server stop

# !!! After installing in Docker use next command in Docker Container "web"
1. pipenv run seed all

# For Test project use link: 
Swagger - http://127.0.0.1:8000/doc#/
Admin - http://127.0.0.1:8000/admin/
Mailcatcher WEB - http://127.0.0.1:1080/
Frontend React - http://localhost:3000/

# User Admin has all permissions, other users can view only their own shops