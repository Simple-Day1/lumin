from lumin.domain.user.value_objects import Phone, Date
from lumin.domain.user.exceptions import UsernameValidationError, PhoneValidationError, DateValidationError


class UsernameValidation:
    def __init__(self, username: str) -> None:
        self.username = username

        if len(self.username) < 6:
            raise UsernameValidationError('Incorrect data!')


class PhoneValidation:
    def __init__(self, phone: Phone) -> None:
        self.phone = phone

        if len(self.phone.phone) != 12:
            raise PhoneValidationError('Incorrect data!')


class DateValidation:
    def __init__(self, date: Date) -> None:
        self.date = date

        if len(self.date.date) < 6:
            raise DateValidationError('Incorrect data!')
