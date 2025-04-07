from uuid import UUID
from lumin.infrastructure.database.database import users_database
from lumin.domain.user.exceptions import UserIsNotExistError, UserIsAlreadyExistError
from lumin.domain.user.user import User
from lumin.domain.user.validation import UsernameValidation, PhoneValidation, DateValidation
from lumin.domain.user.value_objects import Phone, Date


class UserRepository:
    @staticmethod
    def add(user: User) -> None:
        if user.user_id in users_database.keys():
            raise UserIsAlreadyExistError('User is already exist!')
        else:
            ...

    @staticmethod
    def delete(user: User) -> None:
        try:
            users_database.pop(user.user_id)
        except KeyError:
            raise UserIsNotExistError('User is not exist!')

    @staticmethod
    def update(user: User) -> None:
        UsernameValidation(user.username)
        PhoneValidation(user.phone)
        DateValidation(user.date)
        users_database[user.user_id] = {
                'username': user.username,
                'description': user.description,
                'phone': user.phone.phone,
                'date': user.date.date
            }

    @staticmethod
    def with_id(user_id: UUID) -> User | None:
        if user_id in users_database.keys():
            return User(
                user_id=user_id,
                username=users_database[user_id]['username'],
                phone=Phone(users_database[user_id]['phone']),
                date=Date(users_database[user_id]['date'])
            )
        else:
            raise UserIsNotExistError('User is not exist!')
