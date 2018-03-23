import requests
import json
import time

def getCurrentUserDetails(filename):
    if not filename:
        file = "userdetails.txt"
    else:
        file = filename
    details = open(file, "r")
    contents = details.read()
    contentsjson = contents.json()
    mid = contentsjson[info][mid]

    requestURLGetCoinVideos = "https://"
    requestURLGetBangumiList = "https://"
    requestURLGetSubmitVideos = "https://"
    requestURLGetFavFolders = "https://"
    requestURLGetChannels = "https://"
    requestURLGetVipState = "https://space.bilibili.com/ajax/member/getVipStatus?mid=" + mid
    requestURLGetUpStat = "https://api.bilibili.com/x/space/upstat?mid=" + mid + "&jsonp=jsonp"
    requestURLGetMyInfo = "https://space.bilibili.com/ajax/member/GetInfo?vmid=" + mid
    
