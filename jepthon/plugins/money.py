import json
import re

from telethon import Button

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



@jmthon.ar_cmd(command='start')


async def start(message):


    aw = glob.glob('./*.txt')


    if f"c{message.chat.id}.txt" not in aw:


        with open(f"c{message.chat.id}.txt","a")as xs:


            sta = await edit_or_reply(message, f"""<strong>


👋 Hi {message.chat.first_name},


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


        af = edit_or_reply(message, f"""


👋 Hi {message.chat.first_name},


- Wellcome To ReBackBank Bot! .


-  You Can Make Your Own Bank Account And Play To Be Beast in TopList! .


- You Can Take Awards In The Bot And More!


- Add Bot To Your Group Or You Can Use It Here ! .





 ━━━━━━━━━━━━━━━━━


Send : /MakeAccount To Make Account! """, parse_mode="html")

        


@jmthon.ar_cmd(command="فلوسي")


async def a(message):


    f = open(f"{message.chat.id}.txt").read()


    fl = open(f"c{message.chat.id}.txt").read()


    nn = f.split(":")[1]


    balance = f.split(":")[3]


    apcc = fl


    ba = await edit_or_reply(message,f"<strong>Your Balance : {apcc} 💵</strong>",parse_mode="html")


@jmthon.ar_cmd(commands="my")


async def a(message):


    global acc


    idp = message.from_user.id


    print(idp)


    aw = glob.glob('./*.txt')


    print(aw)


    if f"./{message.chat.id}.txt" in aw:


      me = types.InlineKeyboardMarkup()


      me.row_width = 1


      me.add(ch3)


      with open(f"{message.chat.id}.txt","r+")as df:


          


          f = open(f"{message.chat.id}.txt").read()


          fpp = open(f"blockTip.txt","r+")


          fpp.truncate(0)


          fppp = open(f"block.txt","r+")


          fppp.truncate(0)


          fl = open(f"c{message.chat.id}.txt").read()


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


@jmthon.ar_cmd(commands="MakeAccount")


async def mounth(message):


    global msg1


    iddd = message.from_user.id


    aw = glob.glob('./*.txt')


    print(aw)


    print(message.chat.first_name)


    if f"./{message.chat.id}.txt" in aw:


        edit_or_reply(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")


        


    else:


        me = types.InlineKeyboardMarkup()


        me.row_width = 1


        me.add(ch,ch2)


        msg1 = message.text


        sent = await edit_or_reply(message, "Send Bank Name :\nSpaceBank .\nRebackBank.\n\nChoice From List ?",parse_mode="html")





@jmthon.ar_cmd(func=lambda m:"راتب")


async def ga(message):


    global acc


    ms = message.text


    print(message)


    if ms == "delete" or ms == "حذف":


        os.system(f"rm -rf {message.from_user.id}.txt")


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


        edit_or_reply(message,f"<strong>{help}</strong>",parse_mode="html")


    if ms == "فلوسي" or ms == "فلوس":


        fl = open(f"c{message.from_user.id}.txt").read()


        edit_or_reply(message,f"<strong>Your Balance : <code>{fl}</code> 💵</strong>",parse_mode="html")


        


    if ms == "كنز":


          ca = open(f"blockTip.txt").read()


          if f"{message.chat.username}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              


              rt = randint(50,1000000)


              ratb = rt


              acc = open(f"c{message.chat.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{message.chat.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{message.chat.id}.txt","w")as va:


                  va.write(f"{ga}")


              edit_or_reply(message,f"<strong>💸 Your treasure  Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"blockTip.txt","w")as df:


                 df.write(f"{message.chat.username}\n")


                 


                 df.close()


    if "استثمار" in ms:


        value = message.text.replace("استثمار","")


        ls = ["Done","Fail"]


        


        if "Done" in ls:


            ppe = open(f"c{message.from_user.id}.txt").read()


            kf = float(value) + float(randint(float(ppe),float(ppe)))


            with open(f"c{message.from_user.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"c{message.from_user.id}.txt","w")as va:


                  va.write(f"{kf}")


            d = ["1%","2%","4%","8%","9%"]


            raa = random.choice(d)


            edit_or_reply(message,f"""<strong>


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


            pe = open(f"c{message.chat.id}.txt").read()


            kf = int(value) + int(randint(int(pe),int(pe)))


            with open(f"c{message.chat.id}.txt","r+")as fs:


                  fs.truncate(0)


            with open(f"c{message.chat.id}.txt","w")as va:


                  va.write(f"{kf}")


            edit_or_reply(message,f"""<strong>


- Congratulations you won in luck  🎉


- Your Money before  ↢ ( {pe}  💵 ) .


- Your Money now  ↢ ( {kf}  💵 ) .


.</strong>""",parse_mode="html")


        else:


            pep = open(f"c{message.chat.id}.txt").read()


            with open(f"c{message.chat.id}.txt","r+")as fs:


                  fs.truncate(0)


            edit_or_reply(message,f"""<strong>


- Unfortunately, I lost by luck  😬


- Your Money before  ↢ ( {pe} 💵 ) .


- Your Money now  ↢ ( {pep} 💵 ) .


.</strong>""",parse_mode="html")


    if ms == "بخشيش":


          ca = open(f"blockTip.txt").read()


          if f"{message.chat.username}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              


              rt = randint(50,1000)


              ratb = rt


              acc = open(f"c{message.chat.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{message.chat.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{message.chat.id}.txt","w")as va:


                  va.write(f"{ga}")


              edit_or_reply(message,f"<strong>💸 Your tip Is Available!🤩\n- You Got {ratb} 💵.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"blockTip.txt","w")as df:


                 df.write(f"{message.chat.username}\n")


                 


                 df.close()


    if ms == "راتب":


          ca = open(f"block.txt").read()


          if f"{message.chat.username}" in ca:


              edit_or_reply(message,f"<strong>So Quick!\nCome Here Again After 10m!</strong>",parse_mode="html")


          else:


              list = ["programmer 💻-10000","King 🤴-100000","President 👨‍⚖-200000","Worker 🧑‍🔧-1000","Robot 🤖-2300","Driver 🚓-4000","DrogsSeller 🚬-1000000","GunSeller 🔫-90000","Pilot ✈️-30000","Captain 🛳-10000"]


              rt = random.choice(list)


              name = rt.split("-")[0]


              ratb = rt.split("-")[1]


              acc = open(f"c{message.chat.id}.txt").read()


              ga = float(ratb) + float(acc)


              print(ratb)


              print(ga)


              with open(f"c{message.chat.id}.txt","r+")as fs:


                  fs.truncate(0)


              with open(f"c{message.chat.id}.txt","w")as va:


                  va.write(f"{ga}")


              edit_or_reply(message,f"<strong>💸 Your Salary Is Available!🤩\n- You Got {ratb} 💵\n- Because You Are {name}.\n- Your Balance Now its : {ga} 💵 .</strong>",parse_mode="html")


              with open(f"block.txt","w")as df:


                 df.write(f"{message.chat.username}\n")


                 df.close()


                 


@jmthon.callback_query_handler(func=lambda call: True)


async def qwere(call):


    if call.data == "RebackBank":


        RebackBank(call.message)


    if call.data == "SpaceBank":


        SpaceBank(call.message)


    if call.data == "d":


        dell(call.message)





def dell(message):


    os.system(f"rm -rf {message.chat.id}.txt")


    print("ok")


async def RebackBank(message):


    


    msg = message.text


    aw = glob.glob('./*.txt')


    if f"./{message.chat.id}.txt" in aw:


        edit_or_reply(message,f"<strong>Sorry You Already Have an Bank Account!</strong>",parse_mode="html")


    else:


        me = types.InlineKeyboardMarkup()


        me.row_width = 1


        me.add(ch3)


        chars = '1234567890'


        us = str(''.join((random.choice(chars) for i in range(15))))


        s = "5"+us


        try:


            with open(f"{message.chat.id}.txt","a")as x:


                x.write(f"name:{message.chat.first_name}:account:{s}:bank:RebackBank.")


                edit_or_reply(message,text=f"<strong>Done Create Banking Account! Account Detials :\nAccount Id : {s}\nBalance : 50 💵.\nBank Name : RebackBank.</strong>",parse_mode="html")


            with open(f"c{message.chat.id}.txt","a")as xs:


                xs.write("50")


                xs.close()


        except:


            pass
