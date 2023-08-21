import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime
# data=pd.DataFrame([])

fig,ax=plt.subplots()
for i,path in enumerate(os.listdir(r'F:\FLSS-561 粤电和三峡电导率相关数据分析\相邻场域数据')):
    df=pd.read_csv('F:\FLSS-561 粤电和三峡电导率相关数据分析\相邻场域数据\\'+path)
    df=df[['Date and Time','Water Conductivity']]
    # df['site']=path.split('_')[0]
    df['Date and Time']=pd.to_datetime(df['Date and Time'])
    # data=pd.merge(data,df,on='Date and Time')
    df.set_index('Date and Time', inplace=True)
    try:
        ax.plot(df.loc['2023-06-5':'2023-06-30','Water Conductivity'],label=path.split('_')[0])
    except:
        pass

    # data=pd.concat([data,df],ignore_index = False)
    # print(path)
plt.legend()
plt.show()
