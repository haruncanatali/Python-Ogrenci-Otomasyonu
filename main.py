#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import pyplot as plt1
import math as mt
from scipy.stats import norm as nrm
from scipy.stats import binom
import seaborn as sns


# In[ ]:


sinifList = []
mevcud = 0
dosyaOkumaKontrol = 0
basariNotuHesaplaKontrol = 0

class ogrenci:
    basariNotu=0.0
    basariDurumu=""
    harfNotu=""
    
    ogrenciNo=0
    ogrenciAd=""
    ogrenciSoyad=""
    vize1=0
    vize2=0
    final=0


# In[ ]:


def dosyaOku():
    global dosyaOkumaKontrol
    import csv
    with open('Sinif.csv') as s:
                read = csv.reader(s)
                sayac = 0
                for satir in read:
                    sayac = sayac+1 #ogrenciNo,ad,soyad sinav sutun adlarini gecmek icin
                    if(sayac>1):

                        n1 = ogrenci()

                        n1.ogrenciNo = satir[0]
                        n1.ogrenciAd = satir[1]
                        n1.ogrenciSoyad = satir[2]
                        n1.vize1 = satir[3]
                        n1.vize2 = satir[4]
                        n1.final = satir[5]
                        sinifList.append(n1)
                dosyaOkumaKontrol=dosyaOkumaKontrol+1
def basariNotuHesapla():
    global basariNotuHesaplaKontrol
    basariNotuHesaplaKontrol=basariNotuHesaplaKontrol+1
    for i in range(len(sinifList)):
            no1 = (float(sinifList[i].vize1)*0.20)
            no2 = (float(sinifList[i].vize2)*0.30)
            no3 = (float(sinifList[i].final)*0.50)
            Notu = no1+no2+no3

            kontrolStringi = str(Notu)

            for x in range(0,len(kontrolStringi)):
                     if(kontrolStringi[x] == '.'):
                            if(int(kontrolStringi[x+1])>=5):
                                  Notu = mt.ceil(Notu)
                            else:
                                 Notu = mt.floor(Notu)

            sinifList[i].basariNotu = Notu

            if(sinifList[i].basariNotu>=90 and sinifList[i].basariNotu<=100):
                    sinifList[i].harfNotu="AA"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=85 and sinifList[i].basariNotu<=89):
                    sinifList[i].harfNotu="BA"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=80 and sinifList[i].basariNotu<=84):
                    sinifList[i].harfNotu="BB"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=75 and sinifList[i].basariNotu<=79):
                    sinifList[i].harfNotu="CB"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=70 and sinifList[i].basariNotu<=84):
                    sinifList[i].harfNotu="CC"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=65 and sinifList[i].basariNotu<=69):
                    sinifList[i].harfNotu="DC"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=60 and sinifList[i].basariNotu<=64):
                    sinifList[i].harfNotu="DD"
                    sinifList[i].basariDurumu="Geçti"
            elif(sinifList[i].basariNotu>=50 and sinifList[i].basariNotu<=59):
                    sinifList[i].harfNotu="FD"
                    sinifList[i].basariDurumu="Şartlı Geçti"
            elif(sinifList[i].basariNotu<=49):
                    sinifList[i].harfNotu="FF"
                    sinifList[i].basariDurumu="Kaldı"


# In[ ]:


def listele():
    i = 0
    j = 0
    for index in range(len(sinifList)):
        j = index
        while (j > 0) and (int(sinifList[j-1].ogrenciNo) > int(sinifList[j].ogrenciNo)):
            sinifList[j-1] , sinifList[j] = sinifList [j] , sinifList[j-1]
            j -= 1
    for i in range(len(sinifList)):   
        print('{0} {1} {2} {3} {4} {5}'.format(sinifList[i].ogrenciNo,sinifList[i].ogrenciAd,sinifList[i].ogrenciSoyad,sinifList[i].vize1,sinifList[i].vize2,sinifList[i].final))
        
def guncelle():
    durum = 0
    try:
        ogrNo = int(input('Güncellenecek Öğrencinin Öğrenci Numarasını Giriniz : '))
        try:
            for i in range(len(sinifList)):
                if(int(sinifList[i].ogrenciNo) == ogrNo):
                    durum = 1
                    guncellemeIslemiFonk(i)
                    break
            if(durum == 0):
                a = 1/0
        except ZeroDivisionError:
            print('Öğrenci Numarası Bulunamadı!')
            
                    
    except ValueError:
        print('Numerik Değer Giriniz !')
        
       
        
def guncellemeIslemiFonk(indis):
    
    print('Öğrenci Adı :{0} Öğrenci Soyadı :{1} Vize1 :{2} Vize2 :{3} Final :{4}'.format(sinifList[indis].ogrenciAd,sinifList[indis].ogrenciSoyad,sinifList[indis].vize1,sinifList[indis].vize2,sinifList[indis].final))
    
    
    islem = int(input('1)Vize1 Notu Güncelle 2)Vize2 Notu Güncelle 3)Final Notu Güncelle'))
    if(islem == 1):
        sinifList[indis].vize1=int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    elif(islem == 2):
        sinifList[indis].vize2=int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    elif(islem == 3):
        sinifList[indis].final=int(input('Notu Giriniz : '))
        print('Güncelleme Başarılı Oldu')
    else:
        print('Uygun Giriş Yapınız !')

def kayitEkleme():
    durum = 0
    try:
        numara = int(input('Eklenecek Öğrenci Numarasını Giriniz : '))
        try:
            durum = 1
            for i in range(len(sinifList)):
                if(int(sinifList[i].ogrenciNo) == numara):
                    durum=0
            deneme = 1/(durum)
            eklemeIslemiFonk(numara)
        except ZeroDivisionError:
            print('Bu Öğrenci Numarası Sisteme Kayıtlıdır')
    except ValueError:
        print('Numerik Değerler Giriniz !')
        
def eklemeIslemiFonk(gelenNumara):
    o2 = ogrenci
    
    o2.ogrenciNo = gelenNumara
    o2.ogrenciAd = input('Öğrencinin Adını Giriniz : ')
    o2.ogrenciSoyad = input('Öğrencinin Soyadını Giriniz : ')
    o2.vize1 = int(input('Öğrencinin Vize1 Notunu Giriniz : '))
    o2.vize2 = int(input('Öğrencinin Vize2 Notunu Giriniz : '))
    o2.final = int(input('Öğrencinin Final Notunu Giriniz : '))
    
    sinifList.append(o2)
    print('Ekleme İşlemi Başarılı Oldu')
    
def kayitSilme():
    try:
        numara = int(input('Silinecek Öğrencinin Numarasını Giriniz'))
        try:
            durum = 0
            index = 0
            for i in range(len(sinifList)):
                if(int(sinifList[i].ogrenciNo) == numara):
                    durum = 1
                    index = i
            deneme = 1/(durum)
            kayitSilmeIslemiFonk(index)
        except ZeroDivisionError:
            print('Sisteme Kayıtlı Öğrenci Numarası Bulunamadı!')
    except ValueError:
        print('Numerik Değer Giriniz')
        
def kayitSilmeIslemiFonk(indis):
    del sinifList[indis]
    print('Kayıt Silme Başarılı Oldu')

def basariNotuSiralama():
    i = 0
    j = 0
    for index in range(len(sinifList)):
        j = index
        while (j > 0) and (sinifList[j-1].basariNotu < sinifList[j].basariNotu):
            sinifList[j-1] , sinifList[j] = sinifList [j] , sinifList[j-1]
            j -= 1
    for i in range(len(sinifList)):       
        print('{0} {1} {2} {3} {4} {5} {6} {7} {8}'.format(sinifList[i].ogrenciNo,sinifList[i].ogrenciAd,sinifList[i].ogrenciSoyad,sinifList[i].vize1,sinifList[i].vize2,sinifList[i].final,sinifList[i].basariNotu,sinifList[i].harfNotu,sinifList[i].basariDurumu))

    
def istatistik():
    enYuksekBasariNotu = 0
    enDusukBasariNotu = 0
    sinifOrtalamasi = 0.0
    ortalamayiGecenOgrenciSayisi = 0
    standartSapma = 0.0
    
    sinifNotListesi = []
    for i in range(len(sinifList)):
        sinifNotListesi.append(sinifList[i].basariNotu)
    
    list1 = np.array(sinifNotListesi)
    
    enYuksekBasariNotu = list1.max()
    enDusukBasariNotu = list1.min()
    sinifOrtalamasi = list1.mean()
    standartSapma = list1.std()
    
    sayac = 0
    for i in range(len(list1)):
        if(list1[i]>sinifOrtalamasi):
            sayac=sayac+1
    ortalamayiGecenOgrenciSayisi = sayac
    
    
    print('En Yüksek Başarı Notu : {0}'.format(enYuksekBasariNotu))
    print('En Düşük Başarı Notu : {0}'.format(enDusukBasariNotu))
    print('Sınıf Ortalaması : {0}'.format(sinifOrtalamasi))
    print('Ortalamayı Geçen Öğrenci Sayısı : {0}'.format(ortalamayiGecenOgrenciSayisi))
    print('Standart Sapma : {0}'.format(standartSapma))
    
    mean = sinifOrtalamasi
    standard_deviation = standartSapma

    x_values = np.arange(-3, 3, 0.1)
    y_values = nrm(mean, standard_deviation)

    plt.plot(x_values, y_values.pdf(x_values))
    plt.show()
   
    harfNotlari = []
    
    harfNotlari.append('AA')
    harfNotlari.append('BA')
    harfNotlari.append('BB')
    harfNotlari.append('CB')
    harfNotlari.append('CC')
    harfNotlari.append('DC')
    harfNotlari.append('DD')
    harfNotlari.append('FD')
    harfNotlari.append('FF')
    
    
    AA=0
    BA=0
    BB=0
    CB=0
    CC=0
    DC=0
    DD=0
    FD=0
    FF=0
    
    for i in range(len(sinifList)):
        if(sinifList[i].harfNotu == 'AA'):
            AA=AA+1
        elif(sinifList[i].harfNotu == 'BA'):
            BA=BA+1
        elif(sinifList[i].harfNotu == 'BB'):
            BB=BB+1
        elif(sinifList[i].harfNotu == 'CB'):
            CB=CB+1
        elif(sinifList[i].harfNotu == 'CC'):
            CC=CC+1
        elif(sinifList[i].harfNotu == 'DC'):
            DC=DC+1
        elif(sinifList[i].harfNotu == 'DD'):
            DD=DD+1
        elif(sinifList[i].harfNotu == 'FD'):
            FD=FD+1
        elif(sinifList[i].harfNotu == 'FF'):
            FF=FF+1
            
    harfNotlariSayac = []
    harfNotlariSayac.append(AA)
    harfNotlariSayac.append(BA)
    harfNotlariSayac.append(BB)
    harfNotlariSayac.append(CB)
    harfNotlariSayac.append(CC)
    harfNotlariSayac.append(DC)
    harfNotlariSayac.append(DD)
    harfNotlariSayac.append(FD)
    harfNotlariSayac.append(FF)
            
            
            
            
    plt.subplot(2,1,2)
    plt.bar(harfNotlari,harfNotlariSayac)
    plt.ylabel('Harf Notu Dağılımı')
    plt.show()
def dosyaYaz():  
    i = 0
    j = 0
    for index in range(len(sinifList)):
        j = index
        while (j > 0) and (sinifList[j-1].basariNotu < sinifList[j].basariNotu):
            sinifList[j-1] , sinifList[j] = sinifList [j] , sinifList[j-1]
            j -= 1
    import csv
    with open("Output.csv", "w", newline="",encoding='utf8') as y:
        yazıcı = csv.writer(y)
        yazıcı.writerow(['OgrenciNo','Ad','Soyad','Vize1','Vize2','Final','BasariNotu','HarfNotu','BasariDurumu'])
        for i in range(len(sinifList)):
             yazıcı.writerow([sinifList[i].ogrenciNo,sinifList[i].ogrenciAd,sinifList[i].ogrenciSoyad,sinifList[i].vize1,sinifList[i].vize2,sinifList[i].final,sinifList[i].basariNotu,sinifList[i].harfNotu,sinifList[i].basariDurumu])
                


# In[ ]:


def menu():
    print('-------------------------------------------------')
    print('1)Dosya Oku')
    print('2)Yeni Kayıt Ekle')
    print('3)Kayıt Güncelle')
    print('4)Kayıt Sil')
    print('5)Kayıtları Listele')
    print('6)Sınıf Başarı Notlarını Hesapla')
    print('7)Kayıtları Başarı Notuna Göre Sırala')
    print('8)İstatistiki Bilgiler')
    print('9)Dosyaya yaz')
    print('10)Çıkış')
    
    try:
        secim = int(input('Yapmak İstediğiniz İşlemi Belirtiniz : '))
        
        if(secim == 1):
            if (dosyaOkumaKontrol == 0):
                dosyaOku()
                print('Dosya Okundu')
            else:
                print('Olası Hataların Önüne Geçebilmek İçin Programda Dosya Bir Defaya Mahsus Okunabilir!')
        elif(secim == 2):
            kayitEkleme()
        elif(secim == 3):
            guncelle()
        elif(secim == 4):
            kayitSilme()
        elif(secim == 5):
            if(dosyaOkumaKontrol == 1):
                listele()
            else:
                print('Sisteminize Kayıtlı Listelenecek Öge Bulunamadı! Lütfen Dosya Okuma İşlemini Yapınız!')
        elif(secim == 6):
            if(dosyaOkumaKontrol == 1):
                basariNotuHesapla()
                print('Başarı Notu Hesaplandı')
            else:
                print('Lütfen Dosya Okuma İşlemini Yapınız!')
        elif(secim == 7):
            if(basariNotuHesaplaKontrol>0):
                basariNotuSiralama()
            else:
                print('Önce Başarı Notlarını Hesaplayınız')
        elif(secim == 8):
            if(basariNotuHesaplaKontrol>0 and dosyaOkumaKontrol==1):
                istatistik()
            else:
                print('Dosya Okunup , Başarı Notu Hesaplandıktan Sonra Bu Fonksiyon Çalışabilir')
        elif(secim == 9):
            if(basariNotuHesaplaKontrol>0 and dosyaOkumaKontrol==1):
                dosyaYaz()
                print('Dosyaya Yazma Başarılı Oldu')
            else:
                print('Dosya Okunup , Başarı Notu Hesaplandıktan Sonra Bu Fonksiyon Çalışabilir')
        elif(secim == 10):
             return 'Çıkış Yapıldı'
        menu()
    except ValueError:
        print('Numerik Bir Değer Giriniz')
        menu()
    
    
menu()


# In[ ]:




