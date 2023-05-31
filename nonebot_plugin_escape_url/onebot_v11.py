from nonebot.typing import overrides

try:
    from typing import Any, Union

    from nonebot import logger, Bot as BaseBot
    from nonebot.adapters.onebot.v11 import Bot, Event, Message, MessageSegment

    from .core import escape_text

    _origin_call_api = Bot.call_api

    @overrides(BaseBot)
    async def call_api(self, api: str, **data: Any) -> Any:
        if api == 'send_msg':
            message = data.get("message", None)

            if isinstance(message, str):
                message = escape_text(message)
            elif isinstance(message, Message):
                for seg in message:
                    if seg.type == 'text':
                        seg.data['text'] = escape_text(seg.data['text'])

            logger.trace(f"escaped message: {message}")
            data['message'] = message
        return await _origin_call_api(self, api, **data)


    Bot.call_api = call_api

    logger.opt(colors=True).success("Patched <y>OneBot V11</y> Adapter")

except ImportError as e:
    pass
