import os
pdf=[]
txt=[]
jpg=[]
mp3=[]
mp4=[]
url=input("Please write path of the file! Ex. C:/Users/user/Desktop")
for i,j,k in os.walk(url):
    for a in k:
        if a.endswith(".txt"):
            txt.append(a)
        elif a.endswith(".pdf"):
            pdf.append(a)
        elif a.endswith(".jpg"):
            jpg.append(a)

with open("txt_dosyaları.txt","w",encoding="utf-8") as dosya1:
    for i in txt:
        dosya1.write(i +"\n")

with open("pdf_dosyaları.txt","w",encoding="utf-8") as dosya2:
    for i in pdf:
        dosya2.write(i +"\n")

with open("jpg_dosyaları.txt","w",encoding="utf-8") as dosya3:
    for i in jpg:
        dosya3.write(i +"\n")

with open("mp3_dosyaları.txt","w",encoding="utf-8") as dosya4:
    for i in txt:
        dosya4.write(i +"\n")

with open("mp4_dosyaları.txt","w",encoding="utf-8") as dosya5:
    for i in txt:
        dosya5.write(i +"\n")