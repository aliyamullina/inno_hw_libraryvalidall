import pytest
from exceptions import (
    InputParameterVerificationError,
    ResultVerificationError
)
from main import (
    main,
    check_ip_address_with_regex,
    validate_json_with_schema
)


class TestValidAll:
    """Тестирование декоратора."""

    def test_validate_json_with_schema(self):
        """Валидация входного json-параметра."""
        # Не проходит валидацию:
        assert validate_json_with_schema({"name": {'site': 'duckduckgo.com', 'ip': '5.8.5.6'}}) is False
        assert validate_json_with_schema({'site': 'duckduckgo.com', 'ip': '5.8.5.6'}) is True

    def test_check_ip_address_with_regex(self):
        """Валидация строки по регулярному выражению."""
        assert check_ip_address_with_regex({'site': 'google.com', 'ip': '88.8.8'}) is False
        assert check_ip_address_with_regex({'site': 'google.com', 'ip': '8.8.8.8'}) is True

    def test_valid_all_exception_input(self):
        """Проверка что при определенных условиях поднимается исключение
        InputParameterVerificationError."""
        with pytest.raises(InputParameterVerificationError) as er:
            # Файл не проходит валидацию:
            main("sites_invalid.json")
            assert "Ошибка валидации параметра" in er.value

    def test_valid_all_exception_result(self):
        """Проверка что при определенных условиях поднимается исключение
        ResultVerificationError."""
        with pytest.raises(ResultVerificationError) as er:
            # Не проходит регулярку:
            main("sites_not_regex.json")
            assert "Ошибка валидации результата" in er.value


if __name__ == "__main__":
    pytest.main()
