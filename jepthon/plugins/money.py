
import re
from ..Config import Config
from JepIQ.razan.resources.assistant import *
from ..core.decorators import check_owner
from telethon import Button, events
from telethon.events import CallbackQuery, InlineQuery
import glob, os

from telethon import types

from random import randint

import random

from . import jmthon

from ..core.managers import edit_delete, edit_or_reply

import asyncio


ch = Button.inline("RebackBank.", data = "RebackBank")


ch2 = Button.inline("SpaceBank.", data = "SpaceBank")


ch3 = Button.inline("Delete Account.", data = "d")

plugin_category = "utils"


@jmthon.ar_cmd(
    pattern="البنك(?:\s|$)([\s\S]*)",
    command=("البنك", plugin_category),
)
async def start(event):
    me = await event.client.get_me()
    aw = glob.glob('./*.txt')


    if f"c{me.id}.txt" not in aw:


        with open(f"c{me.id}.txt","a")as xs:


            sta = await edit_or_reply(event, f"""<strong>


👋 Hi {me.first_name},


- Wellcome To ReBackBank Bot! .


-  You Can Make Your Own Bank Account And Play To Be Beast in TopList! .


- You Can Take Awards In The Bot And More!


- Add Bot To Your Group Or You Can Use It Here ! .





 ━━━━━━━━━━━━━━━━━
ارسل .انشاء حساب 
لانشاء حساب في البنك

</strong>""",parse_mode="html")


            xs.write("50")


            xs.close()


    else:


        af = await edit_or_reply(event, f"""


👋 Hi {me.first_name},


- Wellcome To ReBackBank Bot! .


-  You Can Make Your Own Bank Account And Play To Be Beast in TopList! .


- You Can Take Awards In The Bot And More!


- Add Bot To Your Group Or You Can Use It Here ! .





 ━━━━━━━━━━━━━━━━━


Send : /MakeAccount To Make Account! """, parse_mode="html")

        


@jmthon.ar_cmd(
    pattern="فلوسي(?:\s|$)([\s\S]*)",
    command=("فلوسي", plugin_category),
)

async def a(message):
    me = await message.client.get_me()
    aw = glob.glob('./*.txt')
    if f"c{me.id}.txt" not in aw:
         noa = await edit_or_reply(message, f"<strong>انت لا تملك حساب في البنك", parse_mode="html")
    else:
         f = open(f"{me.id}.txt").read()
         fl = open(f"c{me.id}.txt").read()
         nn = f.split(":")[1]
         balance = f.split(":")[3]
         apcc = fl
         ba = await edit_or_reply(message,f"<strong>Your Balance : {apcc} 💵</strong>",parse_mode="html")



@jmthon.ar_cmd(
    pattern="بنكي(?:\s|$)([\s\S]*)",
    command=("بنكي", plugin_category),
)

async def myb(message):

    me = await message.client.get_me()
    global acc
    aw = glob.glob('./*.txt')
    if f"./{me.id}.txt" in aw:
      with open(f"{me.id}.txt","r+")as df:
          f = open(f"{me.id}.txt").read()
          fpp = open(f"blockTip.txt","r+")
          fpp.truncate(0)
          fppp = open(f"block.txt","r+")
          fppp.truncate(0)
          fl = open(f"c{me.id}.txt").read()
          nn = f.split(":")[1]
          balance = f.split(":")[3]
          acc = fl
          ifn = f"""
- Name : {nn} .
- Account Id : {balance} .
- Balance : {acc} 💵.
- ================= -
          """
          acinfo = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")
         
          df.close()
    else:

          ca = await edit_or_reply(message,f"<strong>ليس لديك حساب في البنك!</strong>",parse_mode="html")

teX = "اختر بنك لانشاء حساب به"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

         @tgbot.on(events.InlineQuery)
         async def inline_handler(event):
              mee = await event.client.get_me()
              aw = glob.glob('./*.txt')
              if f"./{mee.id}.txt" in aw:
                   ala = await edit_or_reply(event,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")
              else:
                   builder = event.builder
                   result = None
                   query = event.text
                   await bot.get_me()
                   if query.startswith("انشاء حساب") and event.query.user_id == bot.uid:
                        buttons = [
                   [
                    Button.inline("RebackBank.", data = "RebackBank"),
                    Button.inline("SpaceBank.", data = "SpaceBank")
                   ]
               ]
              result = builder.article(
                         title="JEPTHON",
                         text=teX,
                         buttons=buttons,
                         link_preview=False,
                     )
              wae = await event.answer([result] if result else None)

@bot.on(admin_cmd(outgoing=True, pattern="انشاء حساب"))
async def repo(event):
    if event.fwd_from:
        return
    RR7PP = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(RR7PP, "انشاء حساب")
    await response[0].click(event.chat_id)
    await event.delete()



#async def mounth(message):

#    mee = await message.client.get_me()
  #  global msg1


  #  aw = glob.glob('./*.txt')

   # if f"./{mee.id}.txt" in aw:
         
   #      edit_or_reply(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")

  #  else:
 #       msg1 = message.text
 #       sent = await edit_or_reply(message, "Send Bank Name :\nSpaceBank .\nRebackBank.\n\nChoice From the List ?",parse_mode="html")


@jmthon.ar_cmd(func=lambda m:"راتب")

async def ga(message):
    aw = glob.glob('./*.txt')
    if f"./block.txt" not in aw:
         open(f"block.txt","a")    
    if f"./blockTip.txt" not in aw:
         open(f"./blockTip.txt","a")
              
    mee = await message.client.get_me()
    global acc

    ms = message.text

    print(ms + "reda")


    if ms == ".حذف حسابي" or ms == ".حذف حساب":


        os.system(f"rm -rf {mee.id}.txt")


        mde = await edit_or_reply(message,f"<strong>تم حذف حسابك في البنك .</strong>",parse_mode="html")


    if ms == ".المصرف" or ms == ".البانك" or ms == ".مصرف":


        help = """


Wellcome In Help List Or Commands List!


1- استثمار (مبلغ) 


مثال : استثمار 10000


2- حظ (مبلغ)


مثال : حظ 1000


3- مضاربه (مبلغ)


مثال : مضاربه 1000


4- راتب


5- كنز


6-بخشيش


7- فلوسي | لرؤية فلوسك





Done All Commands .


        """


        hr = await edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == ".فلوسي" or ms == ".فلوس":


        fl = open(f"./{mee.id}.txt").read()


        yb = await edit_or_reply(message,f"<strong>Your Balance : <code>{fl}</code> 💵</strong>",parse_mode="html")


        


    if ms == ".كنز":


          ca = open(f"./blockTip.txt").read()


          if f"{mee.username}" in ca:


              gfu = await edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              


              rt = randint(50,3000)


              ratb = rt


              acc = open(f"{./mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              with open(f"{./meeid}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"{./mee.id}.txt","w")as va:


                  va.write(f"./{int(ga)}")


              tx = await edit_or_reply(message,f"<strong>💸 Your treasure  Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"./blockTip.txt","w")as df:


                 df.write(f"{./mee.username}\n")



                 df.close()


    if ".استثمار" in ms:


        value = message.text.replace(".استثمار","")


        ls = ["Done","Fail"]


        if "Done" in ls:


            ppe = open(f"{./mee.id}.txt").read()


            kf = float(value) + float(randint(float(ppe),float(ppe)))


            with open(f"{./mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"{./mee.id}.txt","w")as va:


                  va.write(f"{int(kf)}")


            d = ["1%","2%","4%","8%","9%"]


            raa = random.choice(d)


            mac = await edit_or_reply(message,f"""<strong>


- Successful Investment  💰


- Profit Ratio  ↢ {raa}


- Profit Amount  ↢ ( {ppe} 💵 )


- Your Money Now  ↢ ( {kf}  💵 )


.</strong>""",parse_mode="html")


    if f"{ms} حظ."in message.text:


        value = message.text.replace("حظ.","")


        ls = ["Done","Fail"]


        sv = random.choice(ls)


        if "Done" in sv:


            pe = open(f"{./mee.id}.txt").read()


            kf = int(value) + int(randint(int(pe),int(pe)))


            with open(f"{./mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"{./mee.id}.txt","w")as va:


                  va.write(f"{int(kf)}")


            cong = await edit_or_reply(message,f"""<strong>


- Congratulations you won in luck  🎉


- Your Money before  ↢ ( {pe}  💵 ) .


- Your Money now  ↢ ( {kf}  💵 ) .


.</strong>""",parse_mode="html")


        else:


            pep = open(f"./{mee.id}.txt").read()


            with open(f"./{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            heh = await edit_or_reply(message,f"""<strong>


- Unfortunately, I lost by luck  😬


- Your Money before  ↢ ( {pe} 💵 ) .


- Your Money now  ↢ ( {pep} 💵 ) .


.</strong>""",parse_mode="html")


    if ms == ".بخشيش":


          ca = open(f"./blockTip.txt").read()


          if f"{./mee.username}" in ca:


              qu = await edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:
              rt = randint(50,1000)

              ratb = rt

              acc = open(f"{./mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              with open(f"{./mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"{./mee.id}.txt","w")as va:


                  va.write(f"{int(ga)}")


              tp = await edit_or_reply(message,f"<strong>💸 Your tip Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"./blockTip.txt","w")as df:


                 df.write(f"{./mee.username}\n")



                 df.close()


    if ms == ".راتب":


          ca = open(f"./block.txt").read()


          if f"{./mee.username}" in ca:


              gof = await edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              list = ["programmer 💻-10000","King 🤴-100000","President 👨‍⚖-200000","Worker 🧑‍🔧-1000","Robot 🤖-2300","Driver 🚓-4000","DrogsSeller 🚬-1000000","GunSeller 🔫-90000","Pilot ✈️-30000","Captain 🛳-10000"]


              rt = random.choice(list)


              name = rt.split("-")[0]


              ratb = rt.split("-")[1]


              acc = open(f"./{mee.id}.txt").read()


              ga = float(ratb) + float(acc)




              with open(f"./{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"{mee.id}.txt","w")as va:


                  va.write(f"{int(ga)}")


              sal = await edit_or_reply(message,f"<strong>💸 Your Salary Is Available!🤩\n- You Got {ratb} 💵\n- Because You Are {name}.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"block.txt","w")as df:


                 df.write(f"{mee.username}\n")


                 df.close()


                 
#@jmthon.tgbot.on(CallbackQuery(func=lambda call: True))

async def qwere(call):


    if call.data == "RebackBank":


        Bankre(call.message)


    if call.data == "SpaceBank":


        Bankar(call.message)


    if call.data == "d":


        dell(call.message)




@jmthon.ar_cmd(pattern="غلق حساب (.*)")
   
async def d(message):
    mee = await message.client.get_me()
    aw = glob.glob('./*.txt')
    if f"{mee.id}.txt" not in aw:
         cbs = edit_or_reply(message, "ليس لديك حساب مصرفي لحذفه")
    else:
         os.system(f"rm -rf {mee.id}.txt")
         cbbs = await edit_or_reply(message, "تم حذف حسابك المصرفي")


@jmthon.ar_cmd(pattern="انشاء حساب (.*)")
async def Bankre(message):
    input = event.pattern_match.group(1)
    if input is None:
        await edit_or_reply(message, "<strong>ضع اسم المصرف</strong>", parse_mode="html")
    mee = await message.client.get_me()
    aw = glob.glob('./*.txt')
    if f"{mee.id}.txt" in aw:
        cbbs = await edit_or_reply(message, "لديك حساب مصرفي بالفعل")
    else:
        chars = '1234567890'
        us = str(''.join((random.choice(chars) for i in range(15))))
        s = "5"+us
        try:
            with open(f"{mee.id}.txt","a")as x:
                x.write(f"name:{mee.first_name}:account:{s}:bank:RebackBank.")
                #dm = await edit_or_reply(message,text=f"<strong>Done Create Banking Account! Account Detials :\nAccount Id : {s}\nBalance : 50 💵.\nBank Name : RebackBank.</strong>",parse_mode="html")
            with open(f"c{mee.id}.txt","a")as xs:
                xs.write("50")
                xs.close()                
                cbs = await edit_or_reply(message, f"<strong>:تم انشاء حساب مصرفي لك!\nمعلومات الحساب\nايدي الحساب: {s}\nالاموال: 50$\nاسم المصرف: مصرف جيبثون الاسلامي.</strong>", parse_mode="html")
        
@jmthon.ar_cmd(pattern="انشاء حساب (.*)")
async def bankar(message):
    input = event.pattern_match.group(1)
    if input is None:
        await edit_or_reply(message, "<strong>ضع اسم المصرف</strong>", parse_mode="html")
    mee = await message.client.get_me()
    aw = glob.glob('./*.txt')
    if f"{mee.id}.txt" in aw:
        await edit_or_reply(message, f"<strong>لديك حساب مصرفي بالفعل</strong>",parse_mode="html")
    if input == "جيبثون الاسلامي":
        
        chars = '1234567890'
        us = str(''.join(random.choice(chars) for i in range(15)))
        s = "5"+us
        try:
            with open(f"{mee.id}.txt","a")as x:
                x.write(f"name:{mee.first_name}:account:{s}:bank:BankSpace")
                #ft = await edit_or_reply(message,text=f"<strong>Done Create Banking Account! Account Detials :\nAccount Id : {s}\nBalance : 50 💵.\nBank Name : SpaceBank.</strong>",parse_mode="html",reply_markup=me)
            with open(f"{mee.id}.txt","a")as xs:
                xs.write("50")
                xs.close()
              
                cbs = await edit_or_reply(message, f"<strong>:تم انشاء حساب مصرفي لك!\nمعلومات الحساب\nايدي الحساب: {s}\nالاموال: 50$\nاسم المصرف:ي.</strong>", parse_mode="html")
                
        finally:
             await message.send_message(f"رقم حسابك: {s}")
    else:
           await edit_or_reply(message, "لا يوجد هكذا مصرف")
