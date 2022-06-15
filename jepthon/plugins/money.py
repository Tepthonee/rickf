import time
import json
import re
from ..Config import Config
from ..sql_helper.bank import add_bank, del_bank, get_bank, update_bank
from telethon import Button, events
from telethon.events import CallbackQuery, InlineQuery
import glob, os

from telethon import types

from random import randint

import random

from . import jmthon

from ..core.managers import edit_delete, edit_or_reply

import asyncio

plugin_category = "utils"
#----Timers----#
t = {}
#--------------#
def convert(seconds): 

    seconds = seconds % (24 * 3600) 

    seconds %= 3600

    minutes = seconds // 60

    seconds %= 60

    return "%02d:%02d" % (minutes, seconds)

def savetimers():
    if bool(t):
        with open('timers.json', 'w') as f:
            json.dump(t, f)

#-------load unfinished timers-------#
async def loadtimers():
    if os.exist('timers.json'):
      f = open('timers.json')
      tda = json.load(f)
      if 'كنز' in tda:
          t["كنز"] = time.time() + tda['كنز']
          await asyncio.sleep(tda['كنز'])
          del t["كنز"]
    os.remove('timers.json')
loadtimers()
#-------end of load------#
@jmthon.ar_cmd(
    pattern="البنك(?:\s|$)([\s\S]*)",
    command=("البنك", plugin_category),
)
async def start(event):
    me = await event.client.get_me()
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


        


@jmthon.ar_cmd(
    pattern="فلوسي(?:\s|$)([\s\S]*)",
    command=("فلوسي", plugin_category),
)

async def a(message):
    me = await message.client.get_me()
    if get_bank(me.id) is None:
         noa = await edit_or_reply(message, f"<strong>انت لا تملك حساب في البنك</strong>", parse_mode="html")
    else:
         acc = get_bank(me.id)
         mo = int(acc.balance)
         ba = await edit_or_reply(message,f"<strong>اموالك : {mo}  💵</strong>",parse_mode="html")



@jmthon.ar_cmd(
    pattern="بنكي(?:\s|$)([\s\S]*)",
    command=("بنكي", plugin_category),
)

async def myb(message):

    me = await message.client.get_me()
    
    if get_bank(me.id) is not None:
         acc = get_bank(me.id)
         nn = acc.first_name
         balance = acc.balance
         ba = acc.bank
         ifn = f"""
- ================= -
• الاسم : {nn} 
• رقم الحساب : {me.id} 
• الاموال : {balance} 💵
• اسم المصرف : {ba} 
- ================= -
          """
         acinfo = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")
         
    else:
         ca = await edit_or_reply(message,f"<strong>ليس لديك حساب في البنك!</strong>",parse_mode="html")


@jmthon.ar_cmd(func=lambda m:"راتب")

async def ga(message):
    mee = await message.client.get_me()
    ms = message.text
    acc = get_bank(mee.id)
    if ms == ".حذف حسابي" or ms == ".حذف حساب":
         if acc is None:
              await edit_delete(message, "لا تملك حساب مصرفي لحذفه")
         else:
              del_bank(mee.id)
              await edit_delete(message, "تم حذف حسابك المصرفي بنجاح")


              mde = await edit_or_reply(message,f"<strong>تم حذف حسابك في البنك .</strong>",parse_mode="html")


    if ms == "المصرف." or ms == "البانك." or ms == "مصرف.":


        help = """


Wellcome In Help List Or Commands List!


1- استثمار (مبلغ) 


مثال : .استثمار 10000


2- حظ (مبلغ).


مثال : حظ 1000


3- مضاربه (مبلغ).


مثال : مضاربه 1000


4- راتب.


5- كنز.


6-بخشيش.


7- فلوسي | لرؤية فلوسك.





Done All Commands .


        """


        hr = await edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == ".كنز":
        if "كنز" in t:
              tii = t["كنز"] - time.time()
              return await edit_or_reply(message,"<strong> ليس هنالك كنز لقد اخذته بالفعل انتضر {}</strong>".format(convert(tii)),parse_mode="html")
     
        else:
              rt = randint(50,3000)
              acca = get_bank(mee.id).balance
              ga = int(rt) + int(acca)
              update_bank(mee.id, ga)
              tx = await edit_or_reply(message,f"<strong>💸 لقد حصلت على الكنز!🤩\n- حصلت على {rt} 💵.\n- اموالك الان : {ga} 💵 .</strong>",parse_mode="html")
              t["كنز"] = time.time() + 600 
              await asyncio.sleep(600)
              del t["كنز"]
     
    if ".استثمار" in ms:
        value = message.text.replace(".استثمار","")
        if "استثمار" in t:
            ti2 = t["استثمار"] - time.time()
            return await edit_or_reply(message,"<strong> للاستثمار مجدداً انتضر {}</strong>".format(convert(ti2)),parse_mode="html")
        lss = ["Done","Fail"]
        ls = random.choice(lss)
        ppe = acc.balance
        if int(value) > int(ppe):
            return await edit_delete(message, "<strong>! انت لا تملك هذا القدر من الاموال للاستثمار</strong>", parse_mode="html")
        #isv = value.isnumeric()
        #if not isv:
         #    return await edit_delete(message, "<strong>!ادخل رقم صالِح للاستثمار</strong>", parse_mode="html")
        if "Done" in ls:
            kf = int(value) + int(randint(int(ppe),int(ppe)))
            update_bank(mee.id, kf)
            d = ["1%","2%","4%","8%","9%"]
            ra = random.choice(d)
            ma = await edit_or_reply(message,f"""<strong>


- Successful Investment  💰


- Profit Ratio  ↢ {ra}


- Profit Amount  ↢ ( {ppe} 💵 )


- Your Money Now  ↢ ( {kf}  💵 )


.</strong>""",parse_mode="html")
            t["استثمار"] = time.time() + 600
            await asyncio.sleep(600)
            del t["استثمار"]
        if "Fail" in ls:
             await edit_or_reply(message, "استثمار فاشل لم تحصل على اي ارباح")
             t["استثمار"] = time.time() + 600
             await asyncio.sleep(600)
             del t["استثمار"]
             

    if f"{ms} حظ."in message.text:


        value = message.text.replace("حظ.","")


        ls = ["Done","Fail"]


        sv = random.choice(ls)


        if "Done" in sv:


            pe = open(f"{mee.id}.txt").read()


            kf = int(value) + int(randint(int(pe),int(pe)))

            with open(f"{mee.id}.txt","w")as va:


                  va.write(f"{int(kf)}")


            cong = await edit_or_reply(message,f"""<strong>


- Congratulations you won in luck  🎉


- Your Money before  ↢ ( {pe}  💵 ) .


- Your Money now  ↢ ( {kf}  💵 ) .


.</strong>""",parse_mode="html")


        else:


            pep = open(f"{mee.id}.txt").read()


            with open(f"{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            heh = await edit_or_reply(message,f"""<strong>


- Unfortunately, I lost by luck  😬


- Your Money before  ↢ ( {pe} 💵 ) .


- Your Money now  ↢ ( {pep} 💵 ) .


.</strong>""",parse_mode="html")


    if ms == ".بخشيش":


          ca = open(f"blockTip.txt").read()


          if f"{mee.username}" in ca:


              qu = await edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:
              rt = randint(50,1000)

              ratb = rt

              acc = open(f"{mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              with open(f"{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"{mee.id}.txt","w")as va:


                  va.write(f"{int(ga)}")


              tp = await edit_or_reply(message,f"<strong>💸 Your tip Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"blockTip.txt","w")as df:


                 df.write(f"{mee.username}\n")



                 df.close()


    if ms == ".راتب":


          ca = open(f"block.txt").read()


          if f"{mee.username}" in ca:


              gof = await edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              list = ["programmer 💻-10000","King 🤴-100000","President 👨‍⚖-200000","Worker 🧑‍🔧-1000","Robot 🤖-2300","Driver 🚓-4000","DrogsSeller 🚬-1000000","GunSeller 🔫-90000","Pilot ✈️-30000","Captain 🛳-10000"]


              rt = random.choice(list)


              name = rt.split("-")[0]


              ratb = rt.split("-")[1]


              acc = open(f"{mee.id}.txt").read()


              ga = float(ratb) + float(acc)




              with open(f"{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"{mee.id}.txt","w")as va:


                  va.write(f"{int(ga)}")


              sal = await edit_or_reply(message,f"<strong>💸 Your Salary Is Available!🤩\n- You Got {ratb} 💵\n- Because You Are {name}.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"block.txt","w")as df:


                 df.write(f"{mee.username}\n")


                 df.close()



@jmthon.ar_cmd(pattern="غلق حساب (.*)")
   
async def d(message):
    mee = await message.client.get_me()
    if not get_bank(mee.id):
         cbs = edit_or_reply(message, "ليس لديك حساب مصرفي لحذفه")
    else:
         del_babk(mee.id)
         cbbs = await edit_or_reply(message, "تم حذف حسابك المصرفي")



@jmthon.ar_cmd(pattern="انشاء حساب (.*)")
async def bankar(message):
    input = message.pattern_match.group(1)
    mee = await message.client.get_me()
    if get_bank(mee.id) is not None:
        return await edit_or_reply(message, f"<strong>لديك حساب مصرفي بالفعل</strong>",parse_mode="html")
    if input == "جيبثون الاسلامي":
        bankn = "مصرف جيبثون الاسلامي"
    elif input == "الرافدين":
    	bankn = "مصرف الرافدين"
    elif input != "الرافدين" or "جيبثون الاسلامي":
         return await edit_or_reply(message, "لا يوجد هكذا مصرِف !")
    add_bank(mee.id, mee.first_name, 50, bankn)
    cbs = await edit_or_reply(message,f"<strong>تم انشاء حساب مصرفي بالمعلومات التالية:\nاسم صاحب الحساب:{mee.first_name}|\nايدي الحساب:{mee.id}|\nاسم المصرف:{bankn}|\nالاموال المودعة:50$</strong>", parse_mode="html")

