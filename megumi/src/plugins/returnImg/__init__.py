from pathlib import Path
import nonebot
from nonebot import get_driver
from .config import Config
from nonebot.adapters import Bot,Event
from nonebot import on_keyword
import requests
from nonebot.adapters.onebot.v11 import Message, MessageSegment
import random
global_config = get_driver().config
config = Config.parse_obj(global_config)

pic=on_keyword({'二次元图','随机图'})
@pic.handle()
async def _(bot:Bot,event:Event):
    msg = await suijitu()
    await pic.send(Message(msg))

async def suijitu():
    urls = ['https://iw233.cn/api.php','http://api.iw233.cn/api.php','http://ap1.iw233.cn/api.php','https://dev.iw233.cn/api.php']
    sorts = ['random','iw233','top','yin','cat','xing','mp','pc']
    url = f'{urls[random.randint(0,3)]}?sort={sorts[random.randint(0,7)]}'
    # url='https://iw233.cn/api.php?sort=random'
    pic = requests.get(url)
    pic_ti = f"[CQ:image,file={pic.url}]"
    return pic_ti


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").
    resolve()))

