# -*- coding: utf-8 -*-
import pandas as pd

data1 = {
            'id':[1,2,3,4],
            'ad':["Engin","Derin","Salih","Mehmet"],
            'soyad':["Demiroğ","Demiroğ","Demiroğ","Kaya"]
        }

data2 = {
            'id':[1,3,4,7],
            'ad':["Ayşe","Ali","Ahmet","Cemal"],
            'soyad':["Demiroğ","Demiroğ","Demiroğ","Kaya"]
        }

data1Df=pd.DataFrame(data1)
data2Df=pd.DataFrame(data2)

print(data1Df)
print(data2Df)

print(pd.merge(data1Df,data2Df,on='id',how='inner')) #id aynı olan dataları yanyana getir
print(pd.merge(data1Df,data2Df,on='id',how='left'))  #solda olup sağda olmayanları da getirir.
print(pd.merge(data1Df,data2Df,on='id',how='right')) #sağda olup solda olmayanları da getirir.

print(pd.concat([data1Df,data2Df],axis=1)) #concat işlemi biraraya getirme işlemidir. axis=1 yanyana bastırır.






