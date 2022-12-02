from telethon import events, Button
from ..Config import Config
from ..sql_helper.globals import gvarstatus
from JepIQ.razan.resources.mybot import *

ROZ_PIC = "https://telegra.ph/file/f1e757035e56613a9ef92.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [[Button.url("1- قناة السورس", "https://t.me/Tepthone"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://replit.com/@saif61/generatestringsession#main.py"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://app.koyeb.com/apps/deploy?type=git&repository=github.com/Tepthonee/tepthoniq&branch=Tepthon&name=tepthon&env[APP_ID]=%D8%B6%D8%B9_%D8%A7%D8%A8%D8%A8_%D8%A7%D9%8A%D8%AF%D9%8A&env[API_HASH]=%D8%B6%D8%B9_%D8%A7%D9%8A%D8%A8%D9%8A_%D9%87%D8%A7%D8%B4&env[ENV]=ANYTHING&env[DATABASE_URL]=%D9%82%D8%A7%D8%B9%D8%AF%D8%A9_%D8%A7%D9%84%D8%A8%D9%8A%D8%A7%D9%86%D8%A7%D8%AA&env[STRING_SESSION]=%D9%83%D9%88%D8%AF_%D8%AA%D8%B1%D9%8A%D9%85%D9%83%D8%B3&env[TG_BOT_USERNAME]=%D9%85%D8%B9%D8%B1%D9%81_%D8%A7%D9%84%D8%A8%D9%88%D8%AA&env[TG_BOT_TOKEN]=%D8%AA%D9%88%D9%83%D9%86_%D8%A7%D9%84%D8%A8%D9%88%D8%AA&env[ALIVE_NAME]=%D8%A7%D8%B3%D9%85_%D8%A7%D9%84%D9%85%D8%B3%D8%AA%D8%AE%D8%AF%D9%85&env[TZ]=Asia/Baghdad&env[COMMAND_HAND_LER]=.&env[ELEPHANT_API_KEY]=%D8%B6%D8%B9_%D8%A7%D9%8A%D8%A8%D9%8A_%D9%83%D9%8A&env[KOYEB_APP_NAME]=%D8%B6%D8%B9_%D8%A7%D8%B3%D9%85_%D8%A7%D9%84%D8%AA%D8%B7%D8%A8%D9%8A%D9%82"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/PPF22"),]]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False)
            elif ROZ_PIC:
                result = builder.document(ROZ_PIC,title="Jepthon",text=ROZ,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="Jepthon",text=ROZ,buttons=buttons,link_preview=False)
            await event.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="السورس"))
async def repo(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(TG_BOT, "السورس")
    await response[0].click(event.chat_id)
    await event.delete()

# edit by ~ @lMl10l
