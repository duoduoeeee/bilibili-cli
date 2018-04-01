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
    payload = {"mid" : mid}

    requestURLGetCoinVideos = "https://"
    requestURLGetBangumiList = "https://"
    requestURLGetSubmitVideos = "https://"
    requestURLGetFavFolders = "https://"
    requestURLGetChannels = "https://"
    requestURLGetVipState = "https://space.bilibili.com/ajax/member/getVipStatus"
    requestURLGetUpStat = "https://api.bilibili.com/x/space/upstat?mid=" + mid + "&jsonp=jsonp"
    requestURLGetMyInfo = "https://space.bilibili.com/ajax/member/GetInfo?vmid=" + mid
    
    #make requests
    coinVideos = requests.get(requestURLGetCoinVideos)
    bangumiList = requests.get(requestURLGetBangumiList)
    submitVideos = requests.get(requestURLGetSubmitVideos)
    favFolders = requests.get(requestURLGetFavFolders)
    channels = requests.get(requestURLGetChannels)
    vipState = requests.get(requestURLGetVipState, params=payload)
    upStat = requests.get(requestURLGetUpStat)
    myInfo = requests.get(requestURLGetMyInfo)
    
    #jsonify
    jcoinVideos = coinVideos.json()
    jbangumiList = bangumiList.json()
    jsubmitVideos = submitVideos.json()
    jfavFolders = favFolsers.json()
    jchannels = channels.json()
    jvipState = vipState.json()
    jupStat = upStat.json()
    
    return
    
def getSpecifiedUserDetails(mid):
    if not mid:
        print("Failed to obtain information of specified user - mid not specified.")
    else:
        requestURLUserInfo = "https://"
