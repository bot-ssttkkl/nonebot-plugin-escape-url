from typing import List

from nonebot import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    escape_url_replace_dot_by: str = '。'
    escape_url_ignore_adapters: List[str] = []

    class Config:
        extra = "ignore"


conf = get_plugin_config(Config)
