FROM python:3.8

#COPY . /app
#ADD . /app
COPY ./ /app

WORKDIR /app

EXPOSE 80

CMD python3 main.py
#CMD ["python3", "main.py"]