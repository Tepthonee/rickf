import json
import re
from ..core.decorators import check_owner
from telethon import Button
from ..helpers import get_user_from_event
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


Send : /MakeAccount To Make Account! .





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


async def a(message):

    me = await message.client.get_me()
    global acc
    idp = me.from_user.id
    print(idp)


    aw = glob.glob('./*.txt')


    print(aw)


    if f"./{me.id}.txt" in aw:


      me = types.InlineKeyboardMarkup()


      me.row_width = 1


      me.add(ch3)


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


          az = await edit_or_reply(message,f"<strong>{ifn}</strong>",parse_mode="html")


         


          df.close()


    else:


          edit_or_reply(message,f"<strong>Error,Cant Find You At DataBase! Now Make account .</strong>",parse_mode="html")


          mounth(message)


@jmthon.ar_cmd(
    pattern="انشاء حساب(?:\s|$)([\s\S]*)",
    command=("انشاء حساب", plugin_category),
)


async def mounth(message):

    mee = await message.client.get_me()
    global msg1


    aw = glob.glob('./*.txt')


    print(aw)


    print(mee.first_name)


    if f"./{mee.id}.txt" in aw:


        edit_or_reply(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")


        


    else:


        me = types.InlineKeyboardMarkup()


        me.row_width = 1


        me.add(ch,ch2)


        msg1 = message.text


        sent = await edit_or_reply(message, "Send Bank Name :\nSpaceBank .\nRebackBank.\n\nChoice From List ?",parse_mode="html")





@jmthon.ar_cmd(func=lambda m:"راتب")


async def ga(message):

    mee = await message.client.get_me()
    global acc


    ms = message.text


    print(message)


    if ms == "delete" or ms == "حذف":


        os.system(f"rm -rf {mee.from_user.id}.txt")


        mde = await edit_or_reply(message,f"<strong>Done Delete your Account .</strong>",parse_mode="html")


    if ms == "help" or ms == "الاوامر" or ms == "امر":


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


        hr = edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == "فلوسي" or ms == "فلوس":


        fl = open(f"c{mee.from_user.id}.txt").read()


        edit_or_reply(message,f"<strong>Your Balance : <code>{fl}</code> 💵</strong>",parse_mode="html")


        


    if ms == "كنز":


          ca = open(f"blockTip.txt").read()


          if f"{mee.username}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              


              rt = randint(50,1000000)


              ratb = rt


              acc = open(f"c{mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{meeid}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{mee.id}.txt","w")as va:


                  va.write(f"{ga}")


              tx = edit_or_reply(message,f"<strong>💸 Your treasure  Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"blockTip.txt","w")as df:


                 df.write(f"{mee.username}\n")


                 


                 df.close()


    if "استثمار" in ms:


        value = message.text.replace("استثمار","")


        ls = ["Done","Fail"]


        


        if "Done" in ls:


            ppe = open(f"c{mee.from_user.id}.txt").read()


            kf = float(value) + float(randint(float(ppe),float(ppe)))


            with open(f"c{mee.from_user.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"c{mee.from_user.id}.txt","w")as va:


                  va.write(f"{kf}")


            d = ["1%","2%","4%","8%","9%"]


            raa = random.choice(d)


            mac = edit_or_reply(message,f"""<strong>


- Successful Investment  💰


- Profit Ratio  ↢ {raa}


- Profit Amount  ↢ ( {ppe} 💵 )


- Your Money Now  ↢ ( {kf}  💵 )


.</strong>""",parse_mode="html")


    if f"حظ {ms}"in message.text:


        value = message.text.replace("حظ","")


        ls = ["Done","Fail"]


        sv = random.choice(ls)


        if "Done" in sv:


            pe = open(f"c{mee.id}.txt").read()


            kf = int(value) + int(randint(int(pe),int(pe)))


            with open(f"c{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"c{mee.id}.txt","w")as va:


                  va.write(f"{kf}")


            edit_or_reply(message,f"""<strong>


- Congratulations you won in luck  🎉


- Your Money before  ↢ ( {pe}  💵 ) .


- Your Money now  ↢ ( {kf}  💵 ) .


.</strong>""",parse_mode="html")


        else:


            pep = open(f"c{mee.id}.txt").read()


            with open(f"c{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


            edit_or_reply(message,f"""<strong>


- Unfortunately, I lost by luck  😬


- Your Money before  ↢ ( {pe} 💵 ) .


- Your Money now  ↢ ( {pep} 💵 ) .


.</strong>""",parse_mode="html")


    if ms == "بخشيش":


          ca = open(f"blockTip.txt").read()


          if f"{meeusername}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              


              rt = randint(50,1000)


              ratb = rt


              acc = open(f"c{mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{mee.id}.txt","w")as va:


                  va.write(f"{ga}")


              edit_or_reply(message,f"<strong>💸 Your tip Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"blockTip.txt","w")as df:


                 df.write(f"{mee.username}\n")


                 


                 df.close()


    if ms == "راتب":


          ca = open(f"block.txt").read()


          if f"{mee.username}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              list = ["programmer 💻-10000","King 🤴-100000","President 👨‍⚖-200000","Worker 🧑‍🔧-1000","Robot 🤖-2300","Driver 🚓-4000","DrogsSeller 🚬-1000000","GunSeller 🔫-90000","Pilot ✈️-30000","Captain 🛳-10000"]


              rt = random.choice(list)


              name = rt.split("-")[0]


              ratb = rt.split("-")[1]


              acc = open(f"c{mee.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{mee.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{mee.id}.txt","w")as va:


                  va.write(f"{ga}")


              edit_or_reply(message,f"<strong>💸 Your Salary Is Available!🤩\n- You Got {ratb} 💵\n- Because You Are {name}.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"block.txt","w")as df:


                 df.write(f"{mee.username}\n")


                 df.close()


                 
#jmthon.tgbot.on(CallbackQuery(data=lambda call: True)
@jmthon.tgbot.on(CallbackQuery(data=re.compile(rb"lambda")))
@check_owner

async def qwere(call):


    if call.data == "RebackBank":


        RebackBank(call.message)


    if call.data == "SpaceBank":


        SpaceBank(call.message)


    if call.data == "d":


        dell(call.message)





async def dell(message):

    mee = await event.client.get_me()
    os.system(f"rm -rf {mee.id}.txt")


 


async def RebackBank(message):
    me = await message.client.get_me()

    msg = message.text


    aw = glob.glob('./*.txt')


    if f"./{mee.id}.txt" in aw:


        edit_or_reply(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")


    else:


        me = types.InlineKeyboardMarkup()


        me.row_width = 1


        me.add(ch3)


        chars = '1234567890'


        us = str(''.join((random.choice(chars) for i in range(15))))


        s = "5"+us


        try:


            with open(f"{mee.id}.txt","a")as x:


                x.write(f"name:{mee.first_name}:account:{s}:bank:RebackBank.")


                cb = edit_or_reply(message,text=f"<strong>Done Create Banking Account! Account Detials :\nAccount Id : {s}\nBalance : 50 💵.\nBank Name : RebackBank.</strong>",parse_mode="html")


            with open(f"c{mee.id}.txt","a")as xs:


                xs.write("50")


                xs.close()


        except:


            pass
