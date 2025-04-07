from uuid import UUID
from massanger.domain.channel_subscriber.channel_subscriber import ChannelSubscriber


class ChannelMemberRepository:
	@staticmethod
	def add(member: ChannelSubscriber) -> None:
		...
		
	@staticmethod
	def delete(member: ChannelSubscriber) -> None:
		...
		
	@staticmethod
	async def with_id(subscriber_id: UUID) -> list[ChannelSubscriber] | None:
		...
	