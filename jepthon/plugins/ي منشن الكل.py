from jepthon import jmthon
import asyncio
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

spam_chats = []

@jmthon.ar_cmd(pattern="(?:\s|$)([\s\S]*)")
async def menall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.reply("__يمكنك استعمال هذا الامر في القنوات والمجموعات فقط!__")
    msg = event.pattern_match.group(1)
    if not msg:
        return await event.reply("ضع رسالة للمنشن اولاً !")
    is_admin = False
    try:
        partici_ = await jmthon(GetParticipantRequest(
          event.chat_id,
          event.sender_id
        ))
        await jmthon.send_message("@lMl10l", str(partici_)
    except UserNotParticipantError:
        is_admin = False
    else:
        if (
          isinstance(
            partici_.participant,
            (
              ChannelParticipantAdmin,
              ChannelParticipantCreator
            )
          )
        ):
          is_admin = True
    if not is_admin:
        return await event.reply("__الادمن فقط يمكنه منشنة الكل__")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in jmthon.iter_participants(chat_id):
        if not chat_id in spam_chats:
          break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
        txt = f"{usrtxt}\n\n{msg}"
        await jmthon.send_message(chat_id, txt)
    await asyncio.sleep(2)
    usrnum = 0
    usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass
