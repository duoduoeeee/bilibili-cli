import requests
import json
import collections
import os
import getpass

def getBilibiliLoginStateByCaptcha ():
    print ("Proceeding with username/password combination.")
    print ("Requesting captcha image...")
    requestURL = requests.get("https://passport.bilibili.com/captcha")
    captcha = open("captcha.jpeg", "w+")
    captcha.write(requestURL)
    captcha.close()
    print ("Please open up the captcha.jpeg file just located at current directory, and fill the following login credentials.")
    email = input("Email address:")
    password = getpass.getpass(prompt='Password: ', stream=None)
    captcha = input("Captcha:")
    
    payload = {
        'type' : 'access_key',
        'email' : email,
        'password' : password,
        'captcha' : captcha,
        }
    r1 = requests.post('https://bilibili.zrhdwz.cn/request/api.php', params=payload)
    bililogin = requests.get(r1)['url']
    r2 = requests.get(bililogin)
    if r2['code'] != 0 
        print ("Server failed (" + r2['code'] + "). Message: " + r2['message'])
    else
        accesskey = r2['access_key']
        mid = r2['mid']
        print ('accesskey: ' + accesskey)
        print ('mid:' + mid)
        
        
    
    
def getBilibiliLoginState (accesskey):
    print ("Proceeding with access key.")
    payload = {
        'type' : "cookie",
        'access_key' : accesskey
    }
    r1 = requests.post("https://bilibili.zrhdwz.cn/request/api.php", params=payload)
    r2 = requests.get(requests.get(r1).json()['url'])
    cookie = r2.cookies
    if cookie:
        file = open("cookie.txt", "w+")
        file.write(cookie)
        file.close()
        return [cookie]
    else:
        print("No cookies. Check whether your access_key is correct.")
        return None


def getBilibiliUserDetails (accesskey):
    print ("Obtaining basic information...\n")
    payload = {'access_key' : accesskey}
    requestURL = requests.get("https://api.kaaass.net/biliapi/user/info", params=payload)
    serverResponse = requestURL.json()
    ts = serverResponse['ts']
    status = serverResponse['status']
    mid = serverResponse['info']['mid']
    appid = serverResponse['info']['appid']
    access_key = serverResponse['info']['access_key']
    create_at = serverResponse['info']['create_at']
    userid = serverResponse['info']['userid']
    uname = serverResponse['info']['uname']
    expires = serverResponse['info']['expires']
    permission = serverResponse['info']['permission']

    #exceptions handler
    if status != "OK":
        print('Failed to log in to Bilibili.\nState:' + status)
        return [status]
    else:
        print('Welcome to Bilibili, ' + uname + '.\n')
        file = open("userdetails.txt", "w+")
        file.write(serverResponse)
        file.close()
        return [ts, status, mid, appid, access_key, create_at, userid, uname, expires, permission]

def readBilibiliLoginState(filename):
    if not filename:
        filename = "cookie.txt"

    file = open(filename, "r")
    cookie = file
    file.close()

    return [cookie]

def readBilibiliUserDetails(filename):
    if not filename:
        file = "userdetails.txt"
    else:
        file = filename

    file.open(filename, "r")
    serverResponse = file.json()
    ts = serverResponse['ts']
    status = serverResponse['status']
    mid = serverResponse['info']['mid']
    appid = serverResponse['info']['appid']
    access_key = serverResponse['info']['access_key']
    create_at = serverResponse['info']['create_at']
    userid = serverResponse['info']['userid']
    uname = serverResponse['info']['uname']
    expires = serverResponse['info']['expires']
    permission = serverResponse['info']['permission']
    file.close()
    return [ts, status, mid, appid, access_key, create_at, userid, uname, expires, permission]

def deleteBilibiliLoginState(cookie, loginstate):
    file.open(loginstate, "r")
    serverResponse = file.json()
    mid = serverResponse['info']['mid']
    userid = serverResponse['info']['userid']
    uname = serverResponse['info']['uname']
    file.close()
    print ("Deleting states of " + uname + "(" + userid + "," + mid + ")" + "...")
    os.remove(cookie)
    os.remove(loginstate)
    print ("Completed operation.")

