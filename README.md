# Flask Production Server Setup with Docker Compose

## Development

docker-compose up -d --build
docker-compose down -v
docker-compose logs -f
docker-compose logs -f

### Execute
docker-compose exec db psql --username=projectname --dbname=projectname
docker-compose exec web python manage.py create_db | seed_db

## Production
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml down

### Execute
docker-compose -f docker-compose.prod.yml exec db psql --username=projectname --dbname=projectname
docker-compose -f docker-compose.prod.yml exec web python manage.py create_db | seed_db