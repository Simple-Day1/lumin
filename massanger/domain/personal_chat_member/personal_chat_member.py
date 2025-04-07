from massanger.domain.user.user import User
from massanger.domain.personal_сhat.personal_chat import PersonalChat


class PersonalChatMember:
	def __init__(self, personal_chat: PersonalChat, member: User, role: str) -> None:
		self.personal_chat = personal_chat
		self.member = member
		self.role = role
