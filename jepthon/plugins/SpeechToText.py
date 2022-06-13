
import os
from datetime import datetime
import speech_recognition as sr
#import requests

from jepthon import jmthon
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type

plugin_category = "utils"


@jmthon.ar_cmd(pattern="احجي(?:\s|$)([\s\S]*)",
               command=("احجي", plugin_category),
              )
async def _(event):
    "تحويل الكلام الى نص."
    
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    lan = input_str
    te = await edit_or_reply(event, lan)
    return
    #ted = await edit_or_reply(event, str(lan))
    if not os.path.isdir(Config.TEMP_DIR):
        os.makedirs(Config.TEMP_DIR)
    mediatype = media_type(reply)
    if not reply or (mediatype and mediatype not in ["Voice", "Audio"]):
        return await edit_delete(
            event,
            "`قم بالرد على رسالة او مقطع صوتي لتحويله الى نص.`",
        )
    jepevent = await edit_or_reply(event, "`يجري تنزيل الملف...`")
    required_file_name = await event.client.download_media(reply, Config.TEMP_DIR)
    await jepevent.edit("`يتم التحويل الى نص....`")
    
    data = open(required_file_name, "rb").read()
    r = sr.Recognizer()
    with sr.AudioFile(required_file_name) as source:
         text = r.recognize_google(data, language=str(lan))
    
    end = datetime.now()
    ms = (end - start).seconds
    red = "شنهي"
    string_to_show = "**اللغة : **`{}`\n**النص : **`{}`\n**الوقت المستغرق : **`{} ثانيه`\n**الثقة : **`{}`".format(
            lan, red, ms, text
        )
    await jepevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(required_file_name)
