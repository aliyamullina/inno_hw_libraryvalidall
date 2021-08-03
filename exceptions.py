class InputParameterVerificationError(Exception):
    """Исключение для input_validation()."""

    def __init__(self, message='Ошибка валидации параметра'):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message


class ResultVerificationError(Exception):
    """Исключение для result_validation()."""

    def __init__(self, message='Ошибка валидации результата'):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message
