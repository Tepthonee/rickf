# By Reda for Jepthon
# Tel: @rd0r0
# شعندك داخل للملف تريد تخمطة ههههههههه اخمط ونسبة لنفسك ماوصيك :*
from jepthon import jepiq
import asyncio
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError

spam_chats = []

@jepiq.ar_cmd(pattern="منشن(?:\s|$)([\s\S]*)")
async def menall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.reply("__يمكنك استعمال هذا الامر في القنوات والمجموعات فقط!__")
    msg = event.pattern_match.group(1)
    if not msg:
        return await event.reply("**⌯︙ضع رسالة للمنشن اولاً**")
    is_admin = False
    try:
        partici_ = await jepiq(GetParticipantRequest(
          event.chat_id,
          event.sender_id
        ))
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
        return await event.reply("**⌯︙يجب ان تكون مشرف في المجموعة **")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in jepiq.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrtxt = f"{msg}\n\n[{usr.first_name}](tg://user?id={usr.id}) "
        await jepiq.send_message(chat_id, usrtxt)
        await asyncio.sleep(2)
    try:
        spam_chats.remove(chat_id)
    except:
        pass
@jepiq.ar_cmd(pattern="الغاء منشن")
async def ca_sp(event):
  if not event.chat_id in spam_chats:
    return await event.reply('**⌯︙لايوجد منشن لألغائه **')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.reply('**⌯︙تم الغاء المنشن بنجاح ✅**')
