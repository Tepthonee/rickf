import os.path
from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply


@jmthon.ar_cmd(pattern="موجود؟(?:\s|$)([\s\S]*)")

async def _(event):
    input_str = event.pattern_match.group(1)
    if input_str is None:
        await edit_delete(event, "قم بكتابة اسم البلوكن")
    return edit_or_reply(event, f"{input_str}\n{os.path.exists(f"jepthon/plugins/{input_str}.py"))
