import json
import re
import jsonschema as jsonschema
from typing import Any, Callable
from exceptions import InputParameterVerificationError, ResultVerificationError, OnFailRepeatTimesError


def valid_all(
        input_validation: Callable,
        result_validation: Callable,
        default_behavior: Callable = None,
        on_fail_repeat_times: int = 1
) -> Callable:
    """Универсальный декоратор для валидации входных и
    выходных параметров функции."""

    def decoration(func: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            print("Старт")

            # Проверка валидации json
            if not input_validation(*args, **kwargs):
                raise InputParameterVerificationError()
            else:
                result = func(*args, **kwargs)

            # Проверка регуляркой после валидации
            if not result_validation(result):
                error = ResultVerificationError()

                # При установке параметра в значение 0,
                # выдать написанное самостоятельно исключение
                if on_fail_repeat_times == 0:
                    raise OnFailRepeatTimesError()

                # Пока результат не пройдёт условия проверки,
                # либо будет выполняться вечно
                if on_fail_repeat_times < 0:
                    while not result_validation(result):
                        result = func(*args, **kwargs)

                # Повторения вызова функции при ошибке валидации результата:
                if on_fail_repeat_times >= 1:
                    for i in range(on_fail_repeat_times):
                        print("Попытка", i)
                        result = func(*args, **kwargs)

                        if not result_validation(result):
                            print(error)
                        else:
                            return result

                    if not default_behavior:
                        print('Количество попыток превышено.')
            else:
                return func(*args, **kwargs)

        return wrapper

    return decoration


def validate_json_with_schema(file: dict) -> Any:
    """Происходит валидация входных данных."""
    try:
        with open('sites.schema.json', 'r', encoding='utf-8') as file_schema:
            schema = json.load(file_schema)
            jsonschema.validate(file, schema)
            print("Валидация json пройдена")
            return file
    except jsonschema.exceptions.ValidationError as err:
        print("Ошибка валидации json:", err)
        return False


def check_ip_address_with_regex(file: dict) -> Any:
    """Проверка ip-адреса регулярным выражением."""
    regex_pattern = "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    ip_address = file["ip"]
    if re.fullmatch(regex_pattern, ip_address) is None:
        return False
    else:
        print("Строка проверена")
        return file


@valid_all(
    input_validation=validate_json_with_schema,
    result_validation=check_ip_address_with_regex,
    on_fail_repeat_times=5
)
def check(file: dict) -> dict:
    """Функция для валидации."""
    print(file)
    return file


def main():
    """App start: загрузка json, вызов функции."""
    # Не проходит регулярку:
    with open('not_regex_sites.json', 'r', encoding='utf-8') as file_json:
    # Не проходит валидацию:
    # with open('invalid_sites.json', 'r', encoding='utf-8') as file_json:
    # with open('sites.json', 'r', encoding='utf-8') as file_json:
        file = json.load(file_json)
        check(file)


main()
