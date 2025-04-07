from uuid import UUID
from lumin.domain.massage.exceptions import MassageIsAlreadyExistError, MassageIsNotExistError
from lumin.domain.massage.massage import Massage
from lumin.infrastructure.database.database import massages_database


class MassageRepository:
    @staticmethod
    def add(massage: Massage) -> None:
        if massage.massage_id in massages_database:
            raise MassageIsAlreadyExistError('Massage is already exist!')
        else:
            ...

    @staticmethod
    def delete(massage: Massage) -> None:
        if massage.massage_id in massages_database:
            ...
        else:
            raise MassageIsNotExistError('Massage is not exist!')

    @staticmethod
    def update(massage: Massage) -> None:
        if massage.massage_id in massages_database:
            ...
        else:
            raise MassageIsNotExistError('Massage is not exist!')

    @staticmethod
    def with_id(massage_id: UUID) -> Massage | None:
        if massage_id in massages_database:
            ...
        else:
            raise MassageIsNotExistError('Massage is not exist!')
