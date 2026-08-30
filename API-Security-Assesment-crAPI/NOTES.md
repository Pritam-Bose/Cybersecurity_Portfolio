sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker

You want:

active (running)


curl -L -o /tmp/crapi.zip https://github.com/OWASP/crAPI/archive/refs/heads/main.zip
unzip /tmp/crapi.zip
cd ~/crAPI-main/deploy/docker
docker compose pull
docker compose -f docker-compose.yml --compatibility up -d
docker compose ps


http://localhost:8888