from config import log_write

class HTTPrequest:

    def __init__(self, path, address, enc_auth, body):
        """ Инициализируем запрос """
        self.path = path
        self.address = address
        self.enc_auth = enc_auth
        self.body = body
        pass

    def to_bytes(self) -> bytes:
        """ Создаем тело запроса и переводим его в битовый тип"""
        len_body = len(self.body)
        request = (
            f"POST {self.path} HTTP/1.1\r\n"
            f"Host: {self.address}\r\n"
            f"Authorization: Basic {self.enc_auth}\r\n"
            f"Content-Type: application/json\r\n"
            f"Content-Length: {len_body}\r\n"
            f"\r\n"
            f"{self.body}"
        )
        log_write("\nRequest body: \n")
        log_write(request)
        return request.encode('utf-8')


class HTTPresponse:
    def __init__(self, socket):
        """ Инициализируем ответ """
        self.response = b""
        self.socket = socket
        pass

    def HTTPresponse_get(self):
        """ Собираем HTTP ответ """
        socket = self.socket
        response = b""
        while True:
            part = socket.recv(1024)
            if not part:
                break
            response += part
            if b"\r\n\r\n" in response:
                break
        self.response = response
        return self.response

    def from_bytes(self):
        """ Переводим ответ из битового типа данных в строковой """
        respons = self.response.decode("utf-8")
        log_write("\nResponse body: \n")
        log_write(respons)
        return respons