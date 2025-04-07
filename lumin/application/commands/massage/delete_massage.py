from lumin.domain.massage.massage import Massage
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class DeleteMassage:
    @staticmethod
    def delete_massage(massage: Massage) -> None:
        MassageRepository.delete(massage)
