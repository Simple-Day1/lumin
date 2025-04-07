from sqlalchemy import (MetaData,
                        Table,
                        Column,
                        String,
                        Date,
                        UUID,
                        TIMESTAMP,
                        ARRAY,
                        Boolean)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("user_id", UUID, primary_key=True),
    Column("username", String(50), nullable=False),
    Column("email", String(120), unique=True),
    Column("description", String(120)),
    Column("phone", String(120)),
    Column("date", Date),
)

personal_chats_table = Table(
    "personal_chats",
    metadata,
    Column("personal_chat_id", UUID, primary_key=True),
)

group_chat_table = Table(
    "group_chats",
    metadata,
    Column("group_chat_id", UUID, primary_key=True),
)

channels_table = Table(
    "channels",
    metadata,
    Column("channel_id", UUID, primary_key=True),
)

massages_table = Table(
 "massages",
 metadata,
 Column("massage_id", UUID, primary_key=True),
 Column("content", String(4096)),
 Column("sender_id", UUID),
 Column("recipient_id", UUID),
 Column("timestamp", TIMESTAMP),
 Column("chat_id", UUID),
 Column("photo_urls", ARRAY(String(2083))),
 Column("video_urls", ARRAY(String(2083))),
 Column("status", String(8)),
 Column("reaction_id", UUID),
 Column("fixed", Boolean),
)

personal_chats_members_table = Table(
    "personal_chats_members",
    metadata,
    Column("personal_chat_member_id", UUID, primary_key=True),
    Column("personal_chat_id", UUID),
    Column("role", String)
)

group_chats_members_table = Table(
    "group_chats_members",
    metadata,
    Column("group_chat_member_id", UUID, primary_key=True),
    Column("group_chat_id", UUID),
    Column("role", String)
)

subscribers_of_channels_table = Table(
    "subscribers_of_channels",
    metadata,
    Column("subscribers_of_channel_id", UUID, primary_key=True),
    Column("channel_id", UUID),
    Column("role", String)
)
