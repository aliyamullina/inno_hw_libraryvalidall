import pytest


class TestValidAll(pytest.TestCase):
    """Попробовать разные json в main."""
    # Не проходит регулярку:
    # with open('not_regex_sites.json', 'r', encoding='utf-8') as file_json:
    # Не проходит валидацию:
    # with open('invalid_sites.json', 'r', encoding='utf-8') as file_json:

    def test_what(self):
        pass


if __name__ == "__main__":
    pytest.main()
