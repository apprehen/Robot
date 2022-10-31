from asyncio import events
from multiprocessing import Event
from pathlib import Path

import nonebot
from nonebot import get_driver
from .config import Config
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message,MessageSegment
from nonebot.adapters import Bot,Event
import requests
import time
global_config = get_driver().config
config = Config.parse_obj(global_config)

day_anime = on_keyword({'今日更新番剧','今日新番','今天动画'})
@day_anime.handle()
async def _(bot:Bot,event:Event):
    msg = await spiderfan()
    await day_anime.send(Message(msg))

async def spiderfan():
    day = time.localtime(time.time())
    thistime = str(day.tm_mon) + '-' + str(day.tm_mday)
    anime_list = requests.get("https://api.bilibili.com/pgc/web/timeline?types=1&before=6&after=6").json()['result']
    i_list = []
    anime = ''
    for i in anime_list:
        if i['date'] == thistime:
            i_list = i['episodes']
    for it in i_list:
        url = it['ep_cover']
        anime += it['pub_time'] + '  更新  ' + it['title'] + '  ' + it['pub_index'] +'\n' + f'[CQ:image,file={url}]' + '\n' +'-----------------' + '\n'
    return anime


_sub_plugins = set()
_sub_plugins |= nonebot.load_plugins(
    str((Path(__file__).parent / "plugins").resolve()))

