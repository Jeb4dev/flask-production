# Flask Production Server Setup with Docker Compose

## Development

### Build

``docker-compose up -d --build``
``docker-compose down -v``
``docker-compose logs -f``

### Execute

``docker-compose exec db psql --username=**CHANGE_ME** --dbname=**CHANGE_ME**``
``docker-compose exec web python manage.py create_db | seed_db``

## Production

### Build

``docker-compose -f docker-compose.prod.yml up -d --build``
``docker-compose -f docker-compose.prod.yml down``
``docker-compose -f docker-compose.prod.yml logs``

### Execute

``docker-compose -f docker-compose.prod.yml exec db psql --username=**CHANGE_ME** --dbname=**CHANGE_ME**``
``docker-compose -f docker-compose.prod.yml exec web python manage.py create_db``
``docker-compose -f docker-compose.prod.yml exec web python manage.py seed_db``