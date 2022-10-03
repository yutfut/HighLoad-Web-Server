import socket
import os

from app.handler import handler

HOST = "localhost"
PORT = 80
LIMIT_CONNECTIONS = 256
LIMIT_FORKS = 8
WORKERS = []
DEBUG = False
# DEBUG = True


def start():
    che = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    che.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    che.bind((HOST, PORT))
    che.listen(LIMIT_CONNECTIONS)
    print('Сервер запустился ', HOST, ':', PORT)

    if not DEBUG:
        for thread in range(LIMIT_FORKS):
            pid = os.fork()

            if pid != 0:
                print('Новый дочерний процесс: ', pid)
                WORKERS.append(pid)
            else:
                while True:
                    connection, address = che.accept()

                    try:
                        handler(connection)
                    except Exception as exp:
                        print('Error in prefork ', str(exp))

                    connection.close()

        for worker in WORKERS:
            os.waitpid(worker, 0)
    else:
        while True:
            connection, address = che.accept()

            try:
                handler(connection)
            except Exception as exp:
                print('Error in prefork ', str(exp))

            connection.close()
