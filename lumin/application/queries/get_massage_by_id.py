from uuid import UUID
from lumin.domain.massage.massage import Massage
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class GetMassageById:
    @staticmethod
    async def get_massage_by_id(massage_id: UUID) -> Massage | None:
        massage = MassageRepository.with_id(massage_id)
        return massage
