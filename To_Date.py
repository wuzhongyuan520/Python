import pandas as pd
from datetime import datetime

reader = pd.read_csv('F:\\data\\All1-12.txt')

df=pd.DataFrame(reader)

df.columns = ['date', 'b', 'c', 'd']

df['date'] = pd.to_datetime(df['date']) #����������ת��Ϊ��������
df = df.set_index('date') # ��date����Ϊindex

i=15
num_1=str(i)
num_2=str(i+1)
df = df['2016-01-'+num_1+' 21:00:00':'2016-01-'+num_2+' 00:00:00']

df.to_csv('F:\\timedata\\15.txt')




