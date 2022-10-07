import socket
import os

from test.handler_test import handler_test
from app.handler import handler
from app.response import Response

HOST = "localhost"
PORT = 8000
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
                        # handler_test(connection)
                    except Exception:
                        connection.sendall(Response("500").encode())

                    connection.close()

        for worker in WORKERS:
            os.waitpid(worker, 0)
    else:
        while True:
            connection, address = che.accept()

            try:
                handler(connection)
                # handler_test(connection)
            except Exception:
                connection.sendall(Response("500").encode())

            connection.close()
