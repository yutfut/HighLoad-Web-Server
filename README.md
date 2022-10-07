# HighLoad-Web-Server

## начало работы

> python3 -m venv venv

> source venv/bin/activate

## library:

> pip install pycopy-urllib.parse

## Docker

> docker build -t nginx ./nginx

> docker run -d --rm -p 8888:8888 --name nginx -t nginx

## Docker test

> ab -c 100 -n 1000 http://127.0.0.1:8888/wikipedia_russia.html

> ab -c 100 -n 1000 http://127.0.0.1:8888/httptest/wikipedia_russia.html

## HighLoad Server

> docker build -t server .

> docker run -d --rm -p 80:80 --name server -t server 

> docker run -p 80:80 -v $(PWD)/httptest:/app/httptest:ro --name server -t server 

> docker run -d --rm -p 80:80 -v $(PWD)/httptest:/app/httptest:ro --name server -t server 

## Docker Server install [ab](https://bobcares.com/blog/apache-benchmark-install-ubuntu/)

> apt-get update

> apt-get install apache2-utils 

> ab -V

## Server test

> ab -c 100 -n 1000 http://127.0.0.1:8000/httptest/wikipedia_russia.html

ab -c 100 -n 1000 http://localhost:80/httptest/wikipedia_russia.html