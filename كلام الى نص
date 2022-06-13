# speech to text module for catuserbot by uniborg (@spechide)
import os
from datetime import datetime
import SpeechRecognition as sr
import requests

from . import jmthon

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..helpers import media_type

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="حول نص$",
    command=("حول نص", plugin_category),
    info={
        "header": "speech to text module.",
        "usage": "{tr}stt",
    },
)
async def _(event):
    "تحويل الكلام الى نص."
    
    start = datetime.now()
    lan = event.pattern_match.group(1)
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
    #audio_data = r.record(source)
    text = r.recognize_google(data, language=str(lan))
    
    end = datetime.now()
    ms = (end - start).seconds
    
        string_to_show = "**Language : **`{}`\n**Time Taken : **`{} seconds`\n**No Results Found**".format(
            lan, ms
        )
    else:
        string_to_show = "**Language : **`{}`\n**Transcript : **`{}`\n**Time Taken : **`{} seconds`\n**Confidence : **`{}`".format(
            lan, transcript_response, ms, transcript_confidence
        )
    await jepevent.edit(string_to_show)
    # now, remove the temporary file
    os.remove(required_file_name)
