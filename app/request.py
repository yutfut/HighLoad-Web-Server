DEBUG = False
# DEBUG = True


class Request:
    def __init__(self, data):
        self.data = data
        self.method = None
        self.status = False
        self.path = None
        self.headers = {}

        try:
            self.parse_headers()
        except Exception as exp:
            print('Ощибка парсинга', exp)
            return

    def parse_headers(self):
        headers = self.data.split('\r\n')
        if len(headers) == 0:
            return

        self.method, self.path, _ = headers[0].split()

        if not DEBUG:
            for header in headers[1:]:
                if len(header.split(': ')) == 2:
                    header_name, header_value = header.split(': ')
                    self.headers[header_name] = header_value
        else:
            for header in headers[1:]:
                if len(header.split(': ')) == 2:
                    header_name, header_value = header.split(': ')
                    self.headers[header_name] = header_value
                elif len(header.split(': ')) == 1:
                    if header.split(': ')[0] == '':
                        print("пустая строка")
                    else:
                        print("ощибка")

                else:
                    print("много значений")

        self.status = True
