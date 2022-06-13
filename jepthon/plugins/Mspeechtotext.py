
import os
from datetime import datetime
import speech_recognition as sr
#import requests

from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="احجي$",
    command=("احجي", plugin_category),
    info={
        "header": "speech to text module.",
        "usage": "{tr}stt",
    },
)
async def _(event):
    "تحويل الكلام الى نص."
    
    start = datetime.now()
    lan = event.pattern_match.group(0)
    ted = await edit_or_reply(event, str(lan))
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    reply = await event.get_reply_message()
    mediatype = media_type(reply)
    if not reply or (mediatype and mediatype not in ["Voice", "Audio"]):
        return await edit_delete(
            event,
            "`قم بالرد على رسالة او مقطع صوتي لتحويله الى نص.`",
        )
    jepevent = await edit_or_reply(event, "`يجري تنزيل الملف...`")
    required_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
    await jepevent.edit("`يتم التحويل الى نص....`")
    headers = {
        "Content-Type": reply.media.document.mime_type,
    }
    data = open(required_file_name, "rb").read()
    r = sr.Recognizer()
    with sr.AudioFile(required_file_name) as source:
         text = r.recognize_google(data, language=str(lan))
    
    end = datetime.now()
    ms = (end - start).seconds
    
    string_to_show = """**Language : **`{}`\n**Transcript : **`{}`\n**Time Taken : **`{} seconds`\n**Confidence : **`{}`".format(
            str(lan), transcript_response, ms, text
        """
    await jepevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(required_file_name)
