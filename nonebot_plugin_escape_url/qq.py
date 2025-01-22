from nonebot import logger

from .config import conf
from .core import escape_text as do_escape_text

try:
    if "~qq" not in conf.escape_url_ignore_adapters:
        from nonebot.adapters.qq import Bot, Message, MessageSegment

        _origin_extract_send_message = Bot._extract_send_message

        @staticmethod
        def _extract_send_message(message: Message, escape_text: bool = True):
            new_msg = Message()
            for seg in message:
                if seg.is_text():
                    new_msg.append(MessageSegment.text(do_escape_text(seg.data['text'])))
                else:
                    new_msg.append(seg)

            return _origin_extract_send_message(new_msg, escape_text)


        Bot._extract_send_message = _extract_send_message

        logger.opt(colors=True).success("Patched <y>QQ</y> Adapter")
    else:
        logger.opt(colors=True).info("Skipped patching <y>QQ</y> Adapter")
except ImportError as e:
    pass
