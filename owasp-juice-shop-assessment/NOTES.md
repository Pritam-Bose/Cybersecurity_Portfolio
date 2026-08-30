sudo docker pull bkimminich/juice-shop

Then:

sudo docker run --rm -p 127.0.0.1:3000:3000 bkimminich/juice-shop
nmap -sV 127.0.0.1 -p 3000
curl -I http://127.0.0.1:3000

Browser:

http://localhost:3000