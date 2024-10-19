from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="链接防夹",
    description="自动转换发送消息中的URL，逃避URL检测",
    usage="无",
    type="application",
    homepage="https://github.com/bot-ssttkkl/nonebot-plugin-escape-url",
    config=Config,
    supported_adapters={"~onebot.v11"}
)

from . import onebot_v11
