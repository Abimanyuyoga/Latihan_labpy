import random
a = 0
jumlah = int(input("Masukan Jumlah N : "))
for x in range (0, jumlah) :
        i = random.uniform(.0,.5)
        a+=1
        print("Data ke-",a,"=>",i)