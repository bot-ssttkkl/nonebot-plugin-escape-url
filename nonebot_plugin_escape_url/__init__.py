from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="链接防夹",
    description="自动转换发送消息中的URL，逃避URL检测",
    usage="无"
)

from . import onebot_v11
from . import qqguild
