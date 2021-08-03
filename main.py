from exceptions import InputParameterVerificationError, ResultVerificationError

# json: сайт и ip-адрес
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


@valid_all(
    input_validation,
    result_validation,
    default_behavior,
    on_fail_repeat_times
)
def main():
    pass


main()
