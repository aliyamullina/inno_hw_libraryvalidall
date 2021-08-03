import jsonschema as jsonschema
from typing import Any
from exceptions import InputParameterVerificationError, ResultVerificationError


def valid_all():
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


# json: сайт и ip-адрес
def validate_json_with_schema(file: dict, schema: dict) -> Any:
    """Происходит валидация входных данных."""
    try:
        jsonschema.validate(file, schema)
        return file
    except jsonschema.exceptions.ValidationError as err:
        print("Ошибка валидации json:", err)
        return False


def check_site_name(file: dict) -> Any:
    """Проверка доменных имен."""
    pass


@valid_all(
    input_validation=validate_json_with_schema,
    result_validation=check_site_name,
    # default_behavior=default_behavior,
    on_fail_repeat_times=4
)
def check_json(file: dict, schema: dict) -> tuple[dict, dict]:
    """Функция для валидации."""
    return file, schema


def main():
    """App start: загрузка json, вызов функции."""
    with open('sites.json') as f:
        file_json = f.load(f)

    with open('sites.schema.json.json') as s:
        schema_json = s.load(s)

    check_json(file_json, schema_json)


main()
