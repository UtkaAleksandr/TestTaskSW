import socket as Socket
import base64

from config import *
from clases import *


def send_message():
    """ Присваиваем переменной конфиг, словать с значениями файла config.toml """
    config = config_out()

    """ Собираеам данные для авторизации"""
    username = config["owner"]["username"]
    password = config["owner"]["password"]
    auth = f"{username}:{password}"
    enc_auth = base64.b64encode(auth.encode('utf-8')).decode('utf-8')

    """ Собираем данные для post запроса """
    address = config["database"]["host"]
    port = config["database"]["port"]

    """ Создаем сокет и подключаемся к серверу """
    socket = Socket.socket(Socket.AF_INET, Socket.SOCK_STREAM)
    socket.connect((address, port))

    """ Формируем post http запрос """
    request = HTTPrequest("/send_sms", address, enc_auth, new_message())

    """ Отправляем запрос """
    socket.sendall(request.to_bytes())

    """ Получаем ответ """
    response = HTTPresponse(socket)
    response.HTTPresponse_get()

    """ Выводим код и тело ответа ответа """
    print(response_code_body(response.from_bytes()))
    print("Если хотите продолжить отправку сообщений напишите 'Yes': ")
    if input().lower() == 'yes':
       send_message()
    else:
        """ Закрывем сокет """
        socket.close()





if __name__ == "__main__":
    send_message()