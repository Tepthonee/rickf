import os.path
from jepthon import jmthon
from telethon import events
from ..helpers import get_user_from_event

prog = [393120911, 705475246, 1374312239]

@jmthon.on(events.NewMessage(outgoing=False, pattern="منصب؟"))
async def isJep(event):
    if event.reply_to is not None:
        if event.from_id.user_id in prog :
            await event.reply('منصب جيبثون ✓')
