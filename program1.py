print("Progam1.py")
print(" ")
print("Seorang pengusaha menginvestasikan uangnya untuk memulai usahanya dengan modal awal 100 juta, pada bulan pertama dan kedua belum mendapatkan laba. pada bulan ketiga baru mulai mendapatkan laba sebesar 1% dan pada bulan ke 5, pendapatan meningkat 5%. selanjutnya pada bulan ke 8 mengalami penurunan keuntungan sebesar 2%, sehingga laba menjadi 3%. Hitung total keuntungan selama 8 bulan berjalan usahanya.")
print(" ")
a = int(input("Masukan Laba       : "))
print(" ")
for x in range(1,9):
    if(x>=1 and x<=2):
        b=a*0
        print("Laba Bulan ke -",x," :",b)
    if(x>=3 and x<=4):
        c=a*0.1
        print("Laba Bulan ke -",x," :",c)
    if(x>=5 and x<=7):
        d=a*0.5
        print("Laba Bulan ke -",x," :",d)
    if(x==8):
        e=a*0.2
        print("Laba Bulan ke -",x," :",e)
total=b+b+c+c+d+d+d+e
print(" ")
print("\nTotal Laba Adalah :",total)