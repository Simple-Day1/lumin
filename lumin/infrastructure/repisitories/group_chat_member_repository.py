from uuid import UUID
from lumin.domain.group_chat_member.group_chat_member import GroupChatMember


class GroupChatMemberRepository:
	@staticmethod
	def add(member: GroupChatMember) -> None:
		...
		
	@staticmethod
	def delete(member: GroupChatMember):
		...
		
	@staticmethod
	def update(member: GroupChatMember):
		...
		
	@staticmethod
	async def with_id(member_id: UUID) -> list[GroupChatMember] | None:
		...
	