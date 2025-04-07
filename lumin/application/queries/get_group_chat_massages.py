from lumin.domain.group_chat.group_chat import GroupChat
from lumin.domain.massage.massage import Massage
from lumin.infrastructure.repisitories.massage_repository import MassageRepository


class GetChannelMassages:
    @staticmethod
    async def get_channel_massages(group_chat: GroupChat) -> list[Massage] | None:
        massages = []
        for massage in group_chat.massages:
            massages.append(await MassageRepository.with_id(massage))

        return massages
