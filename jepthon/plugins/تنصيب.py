from telethon import events, Button
from ..Config import Config
from ..sql_helper.globals import gvarstatus
from JepIQ.razan.resources.mybot import *

ROZ_PIC = "https://telegra.ph/file/632932f6b937df7d1ac4f.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("السورس") and event.query.user_id == bot.uid:
            buttons = [[Button.url("1- شرح التنصيب", "https://youtu.be/eXaxtjZPEj8"), Button.url("2- استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("3- ستخراج تيرمكس", "https://replit.com/@saif61/generatestringsession#main.py"), Button.url("4- بوت فاذر", "http://t.me/BotFather"),],[Button.url("5- رابط التنصيب", "https://app.koyeb.com/apps/deploy?type=git&repository=github.com/rick1128/rickthoniq&branch=rickthon&name=rickthon&env[APP_ID]=ضع_ابب_ايدي&env[API_HASH]=ضع_ايبي_هاش&env[ENV]=ANYTHING&env[DATABASE_URL]=قاعدة_البيانات&env[STRING_SESSION]=كود_تريمكس&env[TG_BOT_USERNAME]=معرف_البوت&env[TG_BOT_TOKEN]=توكن_البوت&env[ALIVE_NAME]=اسم_المستخدم&env[TZ]=Asia/Baghdad"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/a9aa99a"),]]
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
