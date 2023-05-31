from functools import wraps

from nonebot import logger
from nonebot.adapters.qqguild.api import API_HANDLERS

from nonebot_plugin_escape_url.core import escape_text


def patch(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        content = kwargs.get("content", None)
        if content is not None:
            content = escape_text(content)
            logger.trace(f"escaped content: {content}")
            kwargs["content"] = content

        return await func(*args, **kwargs)

    return wrapper


API_HANDLERS["post_messages"] = patch(API_HANDLERS["post_messages"])
API_HANDLERS["post_dms_messages"] = patch(API_HANDLERS["post_dms_messages"])

logger.success("Patched <y>QQ Guild</y> Adapter")
