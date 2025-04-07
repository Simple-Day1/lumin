from lumin.domain.user.user import User
from lumin.domain.group_chat.group_chat import GroupChat


class GroupChatMember:
	def __init__(self, group_chat: GroupChat, member: User, role: str) -> None:
		self.group_chat = group_chat
		self.member = member
		self.role = role
