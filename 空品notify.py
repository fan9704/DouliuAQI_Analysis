import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import schedule
#https://www.taiwanstat.com/realtime/pm2.5/
# driverPath = "C:\\Users\cxz12\Downloads\chromedriver.exe"
browser = webdriver.Chrome()
aqitxt = ''
token = 'JpyvNjw2pC140aZsHpOGfWwHgVwfWcGwkeaPXsj1LAj'
url = 'https://airtw.epa.gov.tw'
browser.get(url)
browser.maximize_window()
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

def PM25():
    county=Select(browser.find_element_by_id('ddl_county'))
    site=Select(browser.find_element_by_id('ddl_site'))
    county.select_by_visible_text('雲林縣')
    site.select_by_visible_text('斗六')

    info=browser.find_element_by_class_name('info').find_element_by_class_name('date').text
    aqival=browser.find_element_by_class_name('aquval').text
    aqitxt=browser.find_element_by_class_name('aqitxt').text
    if aqitxt=="良好":
        quality="今天天氣不錯喔"
    elif aqitxt=="普通":
        quality="天氣一般般"
    elif aqitxt=="對敏感族群不健康":
        quality="建議戴口罩喔"
    elif aqitxt=="非常不健康":
        quality="戴口罩喔今天天氣不太好"
    elif aqitxt=="危害":
        quality="!!!!!一定要戴口罩喔今天天氣不太好!!!!!"  
    PM_str = info + ("\nAQI:  %6s  %6s\n小叮嚀 :%20s"%(aqival,aqitxt,quality))
    #----txt
    with open("data.txt","r") as f1:
                        f1.seek(0)
                        count=f1.readline()
                        count=int(count)
    with open("data.txt","w") as f2:
                        f2.seek(0)
                        if count == 31:
                            count=0
                        f2.write(str(count))
    count=int(count)+1
    #----txt
    #----pandas
    df = pd.read_excel('2021_05.xlsx',sheet_name="斗六空氣監測",usecols=["編號", "地點","日期","AQI",])
    rows = df.shape[0]
    row=0
    col=0
     #-----------------------------------
    row=count-1
    df.iloc[row, col]=count
    df.iloc[row, col+1]='雲林縣 斗六'
    df.iloc[row, col+2]=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    df.iloc[row, col+3]=int(aqival)
    df.to_excel('2022_05.xlsx',sheet_name="斗六空氣監測")
    #-----------------------------------
    #----pandas
    print(PM_str)
    return PM_str
def main():
    PM25_data = PM25()
    lineNotifyMessage_text(token, str(PM25_data))
main()
schedule.every().day.at('09:30').do(main)
while True:
      schedule.run_pending()
      time.sleep(1)
