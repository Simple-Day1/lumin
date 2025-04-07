from lumin.domain.user.user import User
from lumin.domain.channel.channel import Channel


class ChannelSubscriber:
	def __init__(self, channel: Channel, subscriber: User, role: str) -> None:
		self.channel = channel
		self.subscriber = subscriber
		self.role = role
