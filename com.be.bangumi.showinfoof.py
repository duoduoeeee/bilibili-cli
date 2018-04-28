import requests
import json
import collections
import os

def getBangumiFeed ():
    requestURL = requests.get("https://bangumi.bilibili.com/api/timeline_v2_global")
    serverResponse = requestURL.json()
    serverstate = serverResponse['code']
    servermessage = serverResponse['message']
    if serverstate != 0
        print ("Server failed. " + servermessage)
    else 
        continue

    bangumiinfo = serverResponse['result']
    print ("=========++++++++++++++++++++++==========Bilibili Bangumi Feed===========++++++++++++++++++++++=========")
    print ("Area   Finished   Weekday  State  Name                               URL                    Followers   ")
    for allinfo in bangumiinfo:
        title = allinfo['title']
        area = allinfo['area']
        followers = allinfo['attention']
        bangumitype = allinfo['bgmcount']
        seasonid = allinfo['season_id']
        bangumistate = allinfo['is_finish']
        bangumibadge = allinfo['badge']
        bangumiweekday = allinfo['weekday']
        
        #以下是优化输出
        seasonurl = "https://bangumi.bilibili.com/anime/" + seasonid
        if bangumistate == 0 :
            bangumistateout = "连载中"
        else if bangumistate == 1 :
            bangumistateout = "完结"
        
        if bangumiweekday == 1 :
            bangumiweekdayout = "MON"
        else if bangumiweekday == 2 :
            bangumiweekdayout = "TUE"
        else if bangumiweekday == 3 :
            bangumiweekdayout = "WED"
        else if bangumiweekday == 4 :
            bangumiweekdayout == "THU"
        else if bangumiweekday == 5 :
            bangumiweekdayout == "FRI"
        else if bangumiweekday == 6 :
            bangumiweekdayout == "SAT"
        else if bangumiweekday == 0 :
            bangumiweekdayout == "SUN"
        
        # 以下输出到终端
        print area + "  " + bangumistateout + "      " + bangumiweekdayout + "      " + bangumistateout + "   " + title + "  " + seasonurl + "  " + followers
    print ("=========++++++++++++++++++++++==========Bilibili Bangumi Feed===========++++++++++++++++++++++=========")

