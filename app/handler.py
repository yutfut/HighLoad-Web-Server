from urllib.parse import unquote

import os

from app.request import Request
from app.response import Response

ALLOWED_METHODS = ['HEAD', 'GET']


def read_file(path):
    with open(path, 'rb') as f:
        content = f.read()
    return content


def handler(che):
    in_buffer = b''
    while not in_buffer.endswith(b'\n'):
        in_buffer += che.recv(1024)
    data = in_buffer.decode()
    request = Request(data)

    if request.method not in ALLOWED_METHODS:
        che.sendall(Response("405").encode())
        return

    if not request.status:
        che.sendall(Response("400").encode())
        return

    if '/../' in request.path:
        che.sendall(Response("403").encode())
        return

    request.path = unquote(request.path.split('?')[0])
    request.path = os.getcwd() + request.path

    if os.path.isdir(request.path):
        request.path += 'index.html'
        if not os.path.isfile(request.path):
            che.sendall(Response("403").encode())
            return

    if not os.path.exists(request.path):
        che.sendall(Response("404").encode())
        return
    try:
        body = read_file(request.path)
    except Exception as exp:
        print('Ошибка чтения файла', str(exp))
        return
    che.sendall(Response("200", request.path, request.method, body).encode())
