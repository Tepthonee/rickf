#By @FeelDeD
import random
from jepthon import jmthon
from ..core.managers import edit_delete
from ..helpers.utils import reply_id

plugin_category = "useless"

@jmthon.ar_cmd(
    pattern="ist ?(.*)",
    command=("ist", plugin_category),
    info={
        "header": "Inline Write-On Sticker",
        "examples": ["{tr}ist dead", "{tr}ist dead;0"],
        "usage": [
            "{tr}ist <your text>",
            "{tr}ist <your text>;<number 0/4>",
        ],
    },
)
async def ist(odi):
    "Some kinda shit"
    try:
        bot = "QuotAfBot"
        reply_to_id = await reply_id(odi)
        text = odi.pattern_match.group(1).replace(" ", "-")
        if not text:
            return await edit_delete(odi, "`Give me a text`")
        if ";" in text:
            query, num = text.split(";")
        else:
            query = text
            num = random.choice(range(0, 4))

        run = await odi.client.inline_query(bot, query.replace("-", " "))
        result = await run[int(num)].click("me")
        await odi.client.send_message(odi.chat_id, result, reply_to=reply_to_id)
        await odi.delete()
        await result.delete()
    except Exception:
        return await edit_delete(odi, "`You did something wrong`")
