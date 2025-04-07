from uuid import UUID
from massanger.infrastructure.repisitories.massage_repository import MassageRepository


class ChangeMassageStatus:
    @staticmethod
    def change_massage_status(massage_id: UUID, new_status: str) -> None:
        massage = MassageRepository.with_id(massage_id)
        massage.status = new_status
        MassageRepository.update(massage)
