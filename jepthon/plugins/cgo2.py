#----------A9AA99A,huks3,i_m_q-RICKTHON
#شعندك بلملف تريد تخمط؟
#تخمط وماتذكر حقوق انت اكبر فرخ
from bs4 import BeautifulSoup
from ..core.session import jepiq
import asyncio,requests
import time
class AiArt:
	def __init__(self, query, *vars):
		self.r = requests.Session()
		self.query = query
		self._main_()
	def _main_(self):
		authorization = requests.post("https://securetoken.googleapis.com/v1/token?key=AIzaSyDCvp5MTJLUdtBYEKYWXJrlLzu1zuKM6Xw", data={"grant_type": "refresh_token", "refresh_token": "AOEOulYxSBtIcIUxZJXlnRNkUtRRFaqDpaQeOEu8ELuSg2LovVGbHSBNf1vFjFD6vVzsSqj81NO5-XUdueMr5g100iP8gN8Hit0zRaJDxVdIcGSL8ktAq9PoET806WIUThrJKAheBz4DTqiDCCRX5UeR23xClCObrhbCWvqmXobRUe09_yAPanY"}).json()
		self.r.headers = {"authorization":f"{str(authorization['token_type']).lower()} {str(authorization['access_token'])}"}
		self.id = self.r.post("https://paint.api.wombo.ai/api/tasks", data='{"premium":false}').json()["id"]
		self.r.put("https://paint.api.wombo.ai/api/tasks/"+self.id, data='{"input_spec":{"prompt":"'+self.query+'","style":3,"display_freq":10}}')
	def Generator(self):
		while True:
			response = self.r.get("https://paint.api.wombo.ai/api/tasks/"+self.id).json()
			if response["state"] == "completed":
				return response["result"]["final"]
			time.sleep(1.5)

@jepiq.on(admin_cmd(pattern=r"\وعد بخ (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat,'بخشيش')
        await asyncio.sleep(605)
@jepiq.on(admin_cmd(pattern=r"\وعد ر (.*)"))
async def _(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await jepiq.send_message(chat,'راتب')
        await asyncio.sleep(605)
        
#تخمط بدون ماتذكر حقوق انيج اختك 
#RICKTHON
@jepiq.on(admin_cmd(pattern=r"\وعد اس (.*)"))
async def _(event):
        for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
            
            chat = event.chat_id
            await jepiq.send_message(chat, 'فلوسي')
            await asyncio.sleep(0.5)
            masg = await jepiq.get_messages(chat, limit=1)
            masg = masg[0].message
            masg = ("".join(masg.split(maxsplit=2)[2:])).split(" ", 2)
            msg = masg[0]
            if int(msg) > 500000000:
                await jepiq.send_message(chat, f"استثمار {msg}")
                await asyncio.sleep(10)
                mssag2 = await jepiq.get_messages(chat, limit=1)
                await mssag2[0].click(text="اي ✅")
            else:
                await jepiq.send_message(chat, f"استثمار {msg}")
            await asyncio.sleep(1210)
@jepiq.on(admin_cmd(pattern=r'^\.تك'))
async def e(event):
                chat = event.get_chat()
                h = event.text
                mes = h.replace('.تك ','')
                
                url = f"https://tiktok-best-experience.p.rapidapi.com/user/{mes}"
                headers = {
		"x-rapidapi-key":"d0cbbe1f79mshe3c74080d9d0da5p1de4ddjsn21db44140e77",
		"x-rapidapi-host":"tiktok-best-experience.p.rapidapi.com",
		"User-Agent":"TikTracker/1.2 (com.markuswu.TikTracker; build:1; iOS 14.4.0) Alamofire/5.4.4"
	}
                r = (requests.get(url,headers=headers).json())
                
                if r['status'] == 'ok':
                 
                  insta = ''
                  uid = ''
                  name=''
                  yc=''
                  bio=''
                  h=''
                  fg=''
                  fs=''
                  p= r['data']['avatar_medium']['url_list'][0]
                  try:
                      uid = r["data"]["uid"]
                  except:
                      uid='not found'
                  try:
                      yc = r["data"]["youtube_channel_id"]
                  except:
                      yc='not found'
                  try:
                      h = r["data"]["total_favorited"]
                  except:
                      h='0'
                  try:
                      fg = r["data"]["following_count"]
                  except:
                      fg='0'
                  try:
                      fs = r["data"]["follower_count"]
                  except:
                      fs='0'
                  try:
                      name = r["data"]["nickname"]
                  except:
                      name='not found'
                  try:
                      bio = r["data"]["signature"]
                  except:
                      bio = 'not found'
    
                  try:
                      insta = r["data"]["ins_id"]
                  except:
                      insta = 'not found'
           
                await event.edit(f'''
• Name : {name}

• Followers : {fs}

• Following : {fg}

• Instagram : {insta}

• Youtube Chanel : {yc}

• Likes : {h}

• Bio : {bio}

• iD : {uid}
= = = = = = = = = = = = = = = = = = = = 
By : @A9AA99A , @HUKS3 , @I_m_q To : @RICKTHON''')
#RICKTHON
@jepiq.on(admin_cmd(pattern=r'^\.ذك'))
async def hne(event):
    chat = await event.get_chat()
    command = event.raw_text.replace('.ذك ','')
    
    
    await jepiq.send_file(event.to_id, AiArt(query=command).Generator(),
                           caption=f'Done Art \nArt name : {command}\n\n•••••••••••••••\nBy : @A9AA99A , @HUKS3 ,@i_m_q')
    await jepiq.delete_messages(chat, event.message)
@jepiq.on(admin_cmd(pattern=r'^\.سيارات'))
async def bi(event):
    
    k = event.raw_text.replace('.سيارات ', '')
    r = k.split(':')[0]
    t = k.split(':')[1]
    n = k.split(':')[2]
    l = k.split(':')[3]
    headers = {
        'authority': 'itp.gov.iq',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'ar;q=0.5',
        'cache-control': 'max-age=0',
        'origin': 'https://itp.gov.iq',
        'referer': 'https://itp.gov.iq/carSearch.php',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36',
    }
    data = {
        'CarLetter': l,
        'CarNumber': n,
        'CarType': t,
        'CarReg': r,
        'submit': 'بحث',
    }
    r = requests.post('https://itp.gov.iq/carSearch.php', headers=headers, data=data)

    if 'لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ' in r.text:
        await event.edit('لا توجد غرامات مفروضة على المركبة - شكرا لالتزامكم بقواعد السير الامن ')
    else:
        suop = BeautifulSoup(r.text, "html.parser")
        m = suop.find_all("table", {"class": "blueTable"})
        for i in m:
            u = (str(i.text).replace('<td>', ''))
            o = str(u.replace('رقم المخالفة', ''))
            ou = str(o.replace('مبلغ المخالفة', ''))
            oo = str(ou.replace('مكان المخالفة', ''))
            uu = str(oo.replace('الوقت', ''))
            await event.edit(uu)
@jepiq.on(admin_cmd(pattern=r'^\.سكرين'))
async def hf(event):
    chat = await event.get_chat()
    query = event.raw_text.replace('.سكرين ','')
    q = (f'https://mr-abood.herokuapp.com/Screenshot/API?Link={query}')
    await jepiq.delete_messages(chat, event.message)
    await jepiq.send_file(event.to_id, q,caption=f'Done screen \nscreen url : {query}\n\n•••••••••••••••\nBy : @A9AA99A , @huks3 , @i_m_q')

@jepiq.on(admin_cmd(pattern=r'^\.بن'))
async def bv(event):
    chat = await event.get_chat()
    command = event.raw_text.split(" ")
    query = event.raw_text.replace('.بن','')
    
    url = 'https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=/search/my_pins/?q=avengers&rs=rs&eq=naruto%208K&etslf=15092&term_meta[]=avengers%7Crecentsearch%7C4&data={"options":{"article":null,"applied_filters":null,"appliedProductFilters":null,"auto_correction_disabled":false,"corpus":null,"customized_rerank_type":null,"filters":null,"query":"'+query+'","query_pin_sigs":null,"redux_normalize_feed":true,"rs":"direct_navigation","scope":"pins","source_id":null,"no_fetch_context_on_resource":false},"context":{}}&_=1662617352806'
    headers = {
        'accept': 'application/json, text/javascript, */*, q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en,ar;q=0.9,en-US;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'csrftoken=0e018d7a846bbb9b8fa7832662c63ed2; _b="AWbcYA0FqcRO6pt4TXz6L96G+/bXeigv/QK5RoON+UKFoKfeyCZZ/IQx+Ka7R9tJhOc="; g_state={"i_l":0}; _auth=1; _pinterest_sess=TWc9PSZoUjNlM2o4dlk2Nis0K3M5bThOOWlzcVVZQ2xKK0grQVhScjU0Vk14M0dYTEswUUMrako1YmNiYk8xaStHSHpnQ2Ezbzc1Rlg1TkZqZkM3djVqRkg2VEg3MTNGZEd4UURRZHc2Njlpam5BdmxFV1hhaW9LNzJ2TWpLdkg3K3krTDJzYXhqbndWeXltYUh5NzVQNEF0M2NQZTc4dVl5RkhDNlFkbGNBa1F0cU0rSEpHclY0dDJHRGdrRWdRdkpoeXhBK3lmMkp3MHh2Z3NJZzVkVm1WTDdJd2ZsQTB3YWI4N2h3c3hnU2tiWU9zYW5sQUJxWFBiSElyRGZTY3hWd2MrZURnSk9idnZ2cFhoUmtTTlRjWGhxTHhNVE9EaTVSQ1FMM2toQmRIYjdCSmVDSklJSFNlMVVycjJ6STdXbnNBaG5nL0xRUFVZYmhxZEtMOUJTKzNqTE9zK1ZYTDNHeEpzOWxXTmpVWkRXRHg4SDUyVkZIZEtxMzZBVnVBZjd2czBKSHp1K0QyV21rOEt3OG03MUdYcVFIVTEvci9VRW9jblplSHE2TGFQZVgrKzlvS2JJK2pRcis1S1JHbU9IYUtYSkVJaENaT05pZXNvd2krMUxNeDVkYnhtK3N0cEMwMzRlMSsrZXVQUEpZdTJtSXZsTTBxWGs1ZmtqYnBUcmJJMlEwSW55ak1mWXVtclV5bzhtTEhadGtLV21LbkVqdzFKelBZWmVlZWE4eGRVNjQ4NFNablRDUTJnb3F0ZTVkWWx1UHdjOXVJWGtwRWtsSit2dHpkMmVzeUxEOHFzdzdmS3NKVnFITDJwUjlDYnRMWWJSeURtQWZ5MloxV1c0WEp4RkQ3SWRKTm1Bc0ZYMDdUR0pubkRXUVpKRS8xNmxQNWNvYUpSb3dtNHlWencvWncrS2hkOXFBNlNsTW5Ha1lpVkdhZ2dMQmhsOUxGN2s4cmdwQUpDRmV5ODVDb0sreWtnNzdhdjZUWjBnLzJ4MlJjdXVHOVI2ZXovUm1KTTQwVmFTREJTUkVvWUF3WEx0QnhwWEtEU2NxSmpXZjNWREcxTWpTb0MrOCtiOW1JbFEvOUlUUFJCNTc4SzJkSTByOG5ieW94UWZ0OWVFR3RPUmpWRGZ2NFRYNTYzRGd5RVlZK1o3UkhVTG5xVUZ5cVlzakl6a2U0Vks1YmQ5SUpkckgvVTlTY2tqblVIU3dmUnRTdkhtL2F6SnFWUnVsMkVwZGRyUlQ5Rk9CMlNzb2VieFYxTDc2UU8vcnBZcjFMR1h5aFV2VFRSRlFrbGppczNYYVh4NXAwcG54TUx3TnpiczZhQTJOMHMxdzgyVitFPSZtUTFDTnV5UTdrNit6R0Q5VDJyS0dXZGN3R0k9; _routing_id="2446e1bc-a370-4e3c-8e3c-ec9ec536d20f"; sessionFunnelEventLogged=1; cm_sub=none',
        'pragma': 'no-cache',
        'referer': 'https://www.pinterest.com/',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'x-app-version': 'a332b16',
        'x-pinterest-appstate': 'active',
        'x-pinterest-experimenthash': 'c519017d978aab61a2dc39b3ed657696bcb130c2aa27632777fcafe1dcae2bce503172a4f5554e6bf64bdce07f29915629f8bc0c126647930a83f3fe6f8d8795',
        'x-pinterest-pws-handler': 'www/search/[scope].js',
        'x-pinterest-source-url': '/search/pins/?q=avengers&rs=typed&term_meta[]=avengers%7Ctyped',
        'x-requested-with': 'XMLHttpRequest',
    }
    req = requests.get(url, headers=headers)
    u='لا بأس من وجود بعض العري في Pinterest، ولكن ضمن حدود الآداب.'
   
    try:
        import random
        h = ['1','2','3','4','5']
        q = req.json()['resource_response']['data']['results'][int(random.choice(h))]['images']['orig']['url']
        await jepiq.delete_messages(chat, event.message)

        await jepiq.send_file(event.to_id, q,
                               caption=f'Done Serch \nserch name : {query}\n\n•••••••••••••••\nBy : @A9AA99A , @huks3 , @i_m_q')
                               
    except Exception as s:
        uk=(requests.get(url, headers=headers).json()['resource_response']['data']['nag']['messages'])
        await jepiq.delete_messages(chat, event.message)
        um = f'{uk}'.replace('"','')
        un = um.replace("'",'')
        ub = un.replace('[','')
        uv = ub.replace(']','')
        await jepiq.send_message(chat,f'{uv}',parse_mode='htm')
