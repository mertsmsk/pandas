# -*- coding: utf-8 -*-

import pandas as pd

notlar = pd.read_csv("grades.csv")
"""
tablodaki kolon isimlerinde çift tırnak kullanıldığı için onları düzgün
çağıramıyoruz. Bu yüzden isimleri kendimiz düzenlemeliyiz.
bunun için columns fonksiyonunu kullanırız.
"""
notlar.columns = ["soyisim","isim","ssn","test1","test2",
                  "test3","test4","final","grade"]
print(notlar)
print(type(notlar))
print(notlar.head(3)) #head baştaki sonuçları gösterir.
print(notlar.tail(3)) #tail sondaki sonuçları gösterir.

print(notlar["isim"].head(3)) #ilk 5 ismi getir.
print(notlar.iloc[5])
print(notlar[1:4]) #1 den 4 e kadar notları göster. 4 dahil değil!