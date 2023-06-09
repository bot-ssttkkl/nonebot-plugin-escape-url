from typing import Any

from nonebot import logger, Bot as BaseBot
from nonebot.typing import overrides

from .config import conf
from .core import escape_text

try:
    if "~onebot.v11" not in conf.escape_url_ignore_adapters:
        from nonebot.adapters.onebot.v11 import Bot, Message

        _origin_call_api = Bot.call_api


        @overrides(BaseBot)
        async def call_api(self, api: str, **data: Any) -> Any:
            if api == 'send_msg':
                message = data.get("message", None)

                if isinstance(message, str):
                    message = escape_text(message, conf.escape_url_replace_dot_by)
                elif isinstance(message, Message):
                    for seg in message:
                        if seg.type == 'text':
                            seg.data['text'] = escape_text(seg.data['text'], conf.escape_url_replace_dot_by)

                logger.trace(f"escaped message: {message}")
                data['message'] = message
            return await _origin_call_api(self, api, **data)


        Bot.call_api = call_api

        logger.opt(colors=True).success("Patched <y>OneBot V11</y> Adapter")
    else:
        logger.opt(colors=True).info("Skipped patching <y>OneBot V11</y> Adapter")
except ImportError as e:
    pass
