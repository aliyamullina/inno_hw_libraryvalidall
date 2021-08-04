import json
import re
import jsonschema as jsonschema
from typing import Any, Callable
from exceptions import InputParameterVerificationError, ResultVerificationError


def valid_all(
        input_validation: Callable,
        result_validation: Callable,
        default_behavior: Callable = None,
        on_fail_repeat_times: int = 4
) -> Callable:
    """Универсальный декоратор для валидации входных и
    выходных параметров функции."""

    def input_validation():
        """Декоратор."""
        try:
            pass
        except InputParameterVerificationError as err:
            print(err)

    def result_validation():
        """Декоратор."""
        try:
            pass
            default_behavior()
        except ResultVerificationError as err:
            print(err)

    def default_behavior():
        """Декоратор."""
        pass

    def on_fail_repeat_times():
        """Декоратор."""
        pass


def validate_json_with_schema(file: dict) -> Any:
    """Происходит валидация входных данных."""
    try:
        with open('sites.schema.json', 'r', encoding='utf-8') as file_schema:
            schema = json.load(file_schema)
            jsonschema.validate(file, schema)
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
        return file


@valid_all(
    input_validation=validate_json_with_schema,
    result_validation=check_ip_address_with_regex,
    default_behavior=None,
    on_fail_repeat_times=1
)
def check(file: dict) -> dict:
    """Функция для валидации."""
    return file


def main():
    """App start: загрузка json, вызов функции."""
    with open('sites.json', 'r', encoding='utf-8') as file_json:
        file = json.load(file_json)
        check(file)


main()
