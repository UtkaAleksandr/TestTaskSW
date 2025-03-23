import tomllib

""" Берем конфигурации из toml и переводим их в словарь """
def config_out():
    with open("config.toml", "rb") as file:
        config = tomllib.load(file)
    return config

""" Создаем и записываем сообщение в лог файл """
def log_write(string):
    with open("log.txt", "a") as file:
        file.write("\n"+(" ".join(string.split("\n"))))

""" Проверяем номер телефона на правильность ввода, брал стабильные Российские номера в которых 11 цифр и есть возможность встрерить + """
def check_number():
    number = input()
    number = number.replace("-", "")
    number = number.replace("(", "")
    number = number.replace(")", "")
    if len(number) <= 12 and number[0] == "+" and number[1:].isdigit():
        return number
    elif len(number) <= 11 and number.isdigit():
        return number
    else:
        print("Неверный номер, попробуйте снова:")
        check_number()



""" Получаем значения номеров и текста от пользователя """
def new_message():
    dict = {}
    print("Введите номер отправителя:")
    dict["sender"] = check_number()
    print("Введите номер получателя:")
    dict["recipient"] = check_number()
    dict["message"] = input("Введите текст сообщения: \n")
    return str(dict).replace("'", "\"")


""" Обрабатываем ответ и возвращаем код и тело"""
def response_code_body(response):
    response = response.split("\n")
    response_code = response[0].split()[1:]
    response_code = response_code[0] + " " +  response_code[1]
    response_body = response[-1]
    return (f"Код ответа: {str(response_code)}\n"
        f"Тело ответа: {str(response_body)}")
