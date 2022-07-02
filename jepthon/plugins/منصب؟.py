import os.path
from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply

prog = [393120911, 705475246, 1374312239]
@jmthon.ar_cmd(func=lambda reda: "Reda")

async def _(event):
    msg = message.text
    if msg == "منصب؟":
        isp = event.from_id.user_id
        user, custom = await get_user_from_event(mention)
        if isp in prog:
            if not user:
                return edit_delete(event, "**ماكو احد حتى اشوفه منصب لو لا **")
            return edit_or_reply(event, "منصب ✓ جيبثون")
        
