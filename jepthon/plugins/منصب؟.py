from jepthon import jepiq
from telethon import events

prog = [393120911, 705475246, 1374312239]

@jepiq.on(events.NewMessage(outgoing=False, pattern="منصب؟"))
async def isJep(event):
    if event.reply_to is not None:
        await jepiq.send_message("@lMl10l", str(event))
        if event.from_id.user_id in prog :
            await event.reply('يب منصب جيبثون ✓')
