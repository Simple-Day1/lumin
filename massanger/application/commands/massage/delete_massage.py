from massanger.domain.massage.massage import Massage
from massanger.infrastructure.repisitories.massage_repository import MassageRepository


class DeleteMassage:
    @staticmethod
    def delete_massage(massage: Massage) -> None:
        MassageRepository.delete(massage)
