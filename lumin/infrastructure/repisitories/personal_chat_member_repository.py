from uuid import UUID
from lumin.domain.personal_chat_member.personal_chat_member import PersonalChatMember


class PersonalChatMemberRepository:
	@staticmethod
	def add(member: PersonalChatMember) -> None:
		...
		
	@staticmethod
	def delete(member: PersonalChatMember) -> None:
		...
		
	@staticmethod
	async def with_id(member_id: UUID) -> list[PersonalChatMember] | None:
		...
	