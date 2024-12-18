from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message

from db import User


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):

    async def __call__(self, message: Message, bot: Bot) -> bool:
        return True if await User.is_admin(telegram_id=message.from_user.id) else False
