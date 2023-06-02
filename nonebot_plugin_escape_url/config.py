from nonebot import get_driver
from pydantic import BaseSettings


class Config(BaseSettings):
    escape_url_replace_dot_by: str = '。'

    class Config:
        extra = "ignore"


conf = Config(**get_driver().config.dict())
