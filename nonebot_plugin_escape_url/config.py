from typing import List

from nonebot import get_driver
from pydantic import BaseSettings


class Config(BaseSettings):
    escape_url_replace_dot_by: str = '。'
    escape_url_ignore_adapters: List[str] = []

    class Config:
        extra = "ignore"


conf = Config(**get_driver().config.dict())
