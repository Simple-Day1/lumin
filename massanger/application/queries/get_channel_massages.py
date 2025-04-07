from massanger.domain.channel.channel import Channel
from massanger.domain.massage.massage import Massage
from massanger.infrastructure.repisitories.massage_repository import MassageRepository


class GetChannelMassages:
    @staticmethod
    async def get_channel_massages(channel: Channel) -> list[Massage] | None:
        massages = []
        for massage in channel.massages:
            massages.append(await MassageRepository.with_id(massage))

        return massages
