import requests
token = 'JpyvNjw2pC140aZsHpOGfWwHgVwfWcGwkeaPXsj1LAj'

def lineNotifyMessage_text(token,msg):
    headers = {
        "Authorization":"Bearer " + token,
        "Content-Type":"application/x-www-form-urlencoded"
        }
    payload = {'message':msg}
    r = requests.post("https://notify-api.line.me./api/notify",
                      headers = headers,params=payload)
    print(r.status_code)
    return r.status_code

lineNotifyMessage_text(token,"Hi Line Notify API我是測試系統")