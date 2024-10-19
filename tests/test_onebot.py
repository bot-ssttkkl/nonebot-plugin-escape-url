import pytest
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Message
from nonebug import App

from tests.utils import mock_obv11_message_event, create_obv11_bot


@pytest.mark.asyncio
async def test_onebot(app: App):
    from nonebot_plugin_saa import Text, MessageFactory

    matcher = on_message()

    @matcher.handle()
    async def process():
        await MessageFactory(Text("https://github.com")).send()

    async with app.test_matcher(matcher) as ctx:
        bot = create_obv11_bot(ctx)
        msg_event = mock_obv11_message_event(Message("321"))
        ctx.receive_event(bot, msg_event)
        ctx.should_call_api(
            "send_msg",
            data={
                "message": Message("github。com"),
                "user_id": 2233,
                "message_type": "private",
            },
            result={
                "message_id": 667788,
            },
        )
