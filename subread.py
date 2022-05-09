import matplotlib.pyplot as plt
import pandas as pd

x = []           
ya = []
yb=[]
yc=[]
yd=[]
readxaxis=False
year=['2021', '2020','2019','2018']

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

for k in year:  
        read(k) 
fig2 , ax = plt.subplots()
fig2.subplots_adjust(hspace=1, wspace=1) #設定子圖的間隔
ax1 = fig2.add_subplot(221)  
ax1.plot(x, ya, color='red', linewidth=2, marker='o')

ax2 = fig2.add_subplot(222)  
ax2.plot(x, yb, color='blue', linewidth=2, marker='o')

ax3 = fig2.add_subplot(223)  
ax3.plot(x, yc, color='orange', linewidth=2, marker='o')

ax4 = fig2.add_subplot(224)  
ax4.plot(x, yd, color='green', linewidth=2, marker='o')

for i in range(4):
    read(year[i])
    plt.subplot(2, 2,i+1)
    plt.text(0.5, 0.5, str(year[i]), fontsize=18, ha='center')


plt.tight_layout()


plt.xticks(x)#x axis刻度
plt.rcParams['font.sans-serif']=['Microsoft YaHei']
#顯示節點資料
for a, b in zip(x, ya):
    ax1.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yb):
    ax2.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yc):
    ax3.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(x, yd):
    ax4.text(a, b, b, ha='center', va='bottom', fontsize=10)

plt.savefig('subworkflow.png')   # Step 5
plt.show()                    # Step 6
