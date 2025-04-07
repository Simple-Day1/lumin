from uuid import UUID
from massanger.infrastructure.repisitories.massage_repository import MassageRepository


class ChangeMassageContent:
    @staticmethod
    def change_massage_content(massage_id: UUID, new_content: UUID) -> None:
        massage = MassageRepository.with_id(massage_id)
        massage.content = new_content
        MassageRepository.update(massage)
