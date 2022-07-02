import os.path
from jepthon import jmthon
from telethon import events
prog = [393120911, 705475246, 1374312239]

@jmthon.on(events.NewMessage(outgoing=False, pattern='منصب؟'))
async def isJep(event):
    sender = await event.get_sender()
    if sender.id in prog :
        await event.reply('منصب جيبثون ✓')
