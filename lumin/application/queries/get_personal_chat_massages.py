from uuid import UUID
from lumin.application.queries.get_personal_chat_by_id import GetPersonalChatById
from lumin.domain.massage.massage import Massage
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class GetPersonalChatMassages:
    @staticmethod
    async def get_channel_massages(personal_chat_id: UUID) -> list[Massage] | None:
        personal_chat = await GetPersonalChatById.get_personal_chat_by_id(personal_chat_id)
        personal_chat_massages = []
        for massage in personal_chat.massages:
            personal_chat_massages.append(await MassageRepository.with_id(massage))

        return personal_chat_massages
