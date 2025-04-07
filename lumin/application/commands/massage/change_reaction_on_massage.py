from uuid import UUID
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class ChangeReactionOnMassage:
    @staticmethod
    def change_reaction_on_massage(massage_id: UUID, new_reaction_id: UUID) -> None:
        massage = MassageRepository.with_id(massage_id)
        massage.reaction = new_reaction_id
        MassageRepository.update(massage)
