import pytest


class TestValidAll(pytest.TestCase):
    """Тестирование декоратора."""

    def test_validate_json_with_schema(self):
        """Валидация входного json-параметра."""
        # Не проходит валидацию:
        # with open('invalid_sites.json', 'r', encoding='utf-8') as file_json:
        pass

    def test_check_ip_address_with_regex(self):
        """Валидация строки по регулярному выражению."""
        # Не проходит регулярку:
        # with open('not_regex_sites.json', 'r', encoding='utf-8') as file_json:
        pass

    def test_valid_all_validation(self):
        """Проверка валидации возвращаемого результата."""
        pass

    def test_valid_all_exception(self):
        """Проверка что при определенных условиях действительно поднимаются исключения
        InputParameterVerificationError, ResultVerificationError."""
        pass


if __name__ == "__main__":
    pytest.main()
