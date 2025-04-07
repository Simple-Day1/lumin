from lumin.domain.massage.massage import Massage
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class CreateMassage:
    @staticmethod
    def create_massage(massage: Massage) -> None:
        MassageRepository.add(massage)
