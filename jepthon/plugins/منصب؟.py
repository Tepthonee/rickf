import os.path
from jepthon import jmthon
from ..helpers import get_user_from_event

prog = [393120911, 705475246, 1374312239]
@jmthon.ar_cmd(func=lambda reda: "Reda")

async def _(event):
    msg = event.text
    if "منصب؟" in msg:
        isp = event.from_id.user_id
        replied_user, error_i_a = await get_user_from_event(event)
        if not replied_user:
            return
        if isp in prog:
            return event.reply("منصب ✓ جيبثون")
        
