import matplotlib.pyplot as plt
import pandas as pd
import os
x = []           
ya = []
yb=[]
yc=[]
yd=[]
readxaxis=False
year=['2021', '2020','2019','2018']
fig = plt.figure() 
plt.xlabel("X-axis Day")#日期
plt.ylabel("Y-axis AQI value")#空氣品質
plt.title("Every Year of May AQI Value")#各年度年五月前兩周空氣品質分析
#2021
def read(year):
    filename=year+"_05.xlsx"
    print(filename)
    f= pd.read_excel(filename,usecols=["編號", "地點","日期","AQI",]) 
    for row in range(15):
                x1=int(f.iloc[ row , 3 ])
                if(year=="2021"):
                    ya.append(x1)
                    y1=f.iloc[row,0]
                    x.append("5/"+str(y1))
                    readxaxis=True
                elif(year=="2020"):
                    yb.append(x1)
                elif(year=="2019"):
                    yc.append(x1)
                elif(year=="2018"):
                    yd.append(x1)
                print(x1,end="  ")#row
    print()


'''
print("Year of 2021")
f1 = pd.read_excel('2021_05.xlsx',usecols=["編號", "地點","日期","AQI",])
for row in range(15):
    y1=f1.iloc[row,0]
    x.append("5/"+str(y1))
    x1=int(f1.iloc[ row , 3 ])
    ya.append(x1)
    print(f1.iloc[ row , 3 ],end="  ")#row
print()
#2020
print("Year of 2020")
f2 = pd.read_excel('2020_05.xlsx',usecols=["編號", "地點","日期","AQI",])
for row in range(15):
    x1=int(f2.iloc[ row , 3 ])
    yb.append(x1)
    print(x1,end="  ")#row
print()
#2019
print("Year of 2019")
f3 = pd.read_excel('2019_05.xlsx',usecols=["編號", "地點","日期","AQI",])
for row in range(15):
    x1=int(f3.iloc[ row , 3 ])
    yc.append(x1)
    print(x1,end="  ")#row
print()
#2018
print("Year of 2018")
f4 = pd.read_excel('2018_05.xlsx',usecols=["編號", "地點","日期","AQI",])
for row in range(15):
    x1=int(f4.iloc[ row , 3 ])
    yd.append(x1)
    print(x1,end="  ")#row
print() '''
for k in year:  
        read(k)
plt.plot(x, ya, color='red', linewidth=2, marker='o') 
plt.plot(x, yb, color='blue', linewidth=2, marker='o')  
plt.plot(x, yc,color='orange', linewidth=2, marker='o')
plt.plot(x, yd,color='green', linewidth=2, marker='o')
plt.legend(year)
plt.xticks(x)#x axis刻度
plt.rcParams['font.sans-serif']=['Microsoft YaHei']


#顯示節點資料
'''
for a, b in zip(x, ya):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yb):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yc):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yd):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
'''
plt.savefig('workflow.png')   # Step 5
plt.show()                    # Step 6
