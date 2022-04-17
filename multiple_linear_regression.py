#!/usr/bin/env python
# coding: utf-8

# # MULTIPLE LINEAR REGRESSION
# 
# Multiple Linear Regression'da birden fazla bağımsız(independent) değişkene karşılık bir bağımlı(dependent) dğeişken bulunur.
# 
# Linear Regression veriler arasında var olan korelasyonu(ilişkiyi) kullanarak yeni gelecek verileri tahmin etme modelidir. Burada makine öğrenimi bize veriler arasındaki bu ilişkiyi belirlememize yardımcı olur ve bu sayede yeni verileri tahmin edebiliriz. 







import pickle


mymodel=pickle.load(open("fiyatlistesimodeli.pickle",'rb'))





ram = int(input("Ram değeri giriniz: "))

cpu=int(input("Cpu değeri giriniz: "))

ssd=int(input("SSD değeri giriniz: "))




y = mymodel.predict([[ram,cpu,ssd]])

print("Fiyat: ",y)






