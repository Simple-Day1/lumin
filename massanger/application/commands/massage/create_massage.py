from massanger.domain.massage.massage import Massage
from massanger.infrastructure.repisitories.massage_repository import MassageRepository


class CreateMassage:
    @staticmethod
    def create_massage(massage: Massage) -> None:
        MassageRepository.add(massage)
