from pydantic import BaseModel


class BotSchema(BaseModel):
    TOKEN: str
    PREFIX: str
    ADMINS: list[int]


class ConfigSchema(BaseModel):
    BOT: BotSchema
    DATABASE: str
