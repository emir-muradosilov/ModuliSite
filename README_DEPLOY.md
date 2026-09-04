cd /home/site

git pull

docker compose build

docker compose up -d --remove-orphans

docker compose ps

docker compose logs web --tail=100