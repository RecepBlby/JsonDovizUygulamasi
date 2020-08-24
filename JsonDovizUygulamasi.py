# JSON farklı diller arasında iletişimi sağlamak için geliştirilmiş basit bir
# veri formatıdır.
# JSON (JavaScript Object Notation), okuyup yazabilmesi oldukça kolay,
# uygulamalarda kolaylıkla tarayıp üzerinden ilerlenebilecek yapısal olarak
# oldukça hafif ve esnek bir veri değişim formatıdır ve temel amacı veri
# alış verişi yaparken daha küçük boyutlarda veri değiştokuşu yapmaktır.
# Makinaların tarayıp, yaratabilmesi kolaydır. Bu veri formatı
# Python’daki sözlük ve listelere çok benzer.
# Birincisi anahtar-değer mantıyla çalışır.
# {
#     "Ad": "Fırat",
#     "Soyad": "Özgül"
# }
# JSON ifadelerinde her öğe arasında virgül olmalıdır.
# Anahtar ve değer ikilisi arasında ise iki nokta kullanılır.
# İkinci kullanımı ise liste tipine çok benzer.
# Bu kullanımda anahtar-değer değil, sadece değer verilir.
# {
#     "Fırat",
#     "Özgül"
# }
# JSON modülünde 4 ana fonksiyon bulunuyor.
# Bunlardan ikisi Python ile JSON oluşturmaya yararken diğer ikisi
# JSON verilerini çözmeye yarar. JSON oluşturan fonksiyonlar şu ikisidir:
# json.dump
# json.dumps
# dump fonksiyonu çıktıyı illaki bir dosya içine aktarır. Bize bu enin istediğin
# JSON çıktısı demez. Bunu diyen dumps fonksiyonudur.
# dumps fonksiyonu str tipinde bir değer döndürürken dump fonksiyonu
# hiçbir değer döndürmez.ğer dump fonksiyonunu kullanacaksanız JSON’a
# dönüşmesini istediğiniz ifadeden sonra dosyayı bulunduran değişkeni yazın.
# JSON verilerini çözen iki fonksiyon ise şunlardır:
# json.load
# json.loads

import requests

url = " http://data.fixer.io/api/latest?access_key=9ce5eea03916d2feff59655544dd667d&format=1"
second = input("Çevirmek istenilen döviz:  ")
total = float(input("Miktar: "))

response = requests.get(url+second)
json_data = response.json()
print("{} Euronun {} karşılığı : ".format(total,second))
print(float(json_data["rates"][second])*total)

# from bs4 import BeautifulSoup
# from urllib.request import urlopen, Request
# def DolarParse():
#     pasteURL = "http://tr.investing.com/currencies/usd-try"
#     data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
#     parse = BeautifulSoup(data)
#     for dolar in parse.find_all('span', id="last_last"):
#         liste = list(dolar)
#         print("Güncel Dolar Kuru: " + str(liste))
# def EuroParse():
#     pasteURL = "http://tr.investing.com/currencies/eur-try"
#     data = urlopen(Request(pasteURL, headers={'User-Agent': 'Mozilla'})).read()
#     parse = BeautifulSoup(data)
#     for dolar in parse.find_all('span', id="last_last"):
#         liste = list(dolar)
#         print("Güncel Euro Kuru: " + str(liste))
# DolarParse()
# EuroParse()
