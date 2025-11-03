# print ("--------------------------")
# print ("nomor 1")
# print ("masukan kalimat/kata")
# kata = input()
# tulisan = kata [::-1]
# print ("maka akan terbalik menjadi : ", end="")
# print (tulisan)

# print ("--------------------------")
# print ("nomor 2")
# print ("masukan kalimat(jangan pake huruf besar)")
# kalimat = input()
# print ("lalu masukan huruf yang ingin dicari jumlahnya")
# huruf = input()
# jumlah = kalimat.count(huruf)
# print ("maka jumlah huruf nya :")
# print (jumlah)

# print ("--------------------------")
# print ("nomor 3")
# print ("masukan kalimat (jangan pakai huruf besar)")
# kalimat = input ()
# print ("maka jumlah karakter yang ada di kalimat itu adalah :")
# karakter = len(kalimat)
# print (karakter)

print ("--------------------------")
print ("nomor 4")
for a in range(1, 7):
    print (str(a)*a, end="")
print()

print ("--------------------------")
print("nomor 5")
for b in range(6,0, -1):
    print (str(b)*b, end="")
print()

print ("--------------------------")
print("nomor 6")
for c in range(1, 8):
    for d in range (1,c+1):
        print (d, end="")
print()

print ("--------------------------")
print("nomor 7")
for e in range (6, 0, -1):
    for f in range (e, 0, -1):
        print (f, end="")
print()

print ("--------------------------")
print("nomor 8")
for g in range (1, 7):# nilai g dari 1 sampai 6
    if g % 2 == 0:#kode mencari angka genap
        for h in range (1, g + 1):
            print(h, end="")
    else: print (str(g)*g, end="")#untuk ganjil
print()

print ("--------------------------")
print ("nomor 9")
for i in range (1, 7):
    if i % 2!=0:#jika iya, i dibagi 2 dan sisanya bukan 0 maka bilangan itu ganjil
        for j in range (1, i+1):
            print (j, end="")
    else: print (str(i)* i, end="")#jika tidak, maka str i dikali kan i
print()

print ("--------------------------")
print("nomor 10")
for k in range (6, 0, -1):
    print (k, end="")
print("5"*5, end="")
for k in range (4, 0, -1):
    print (k, end="")
print ("3"*3, end="")
print ("211")

print ("--------------------------")
print("nomor 11")
print("6"*6, end="")
for l in range(1, 6):
    print (l, end="")
print (str(4)*4, end="")
for m in range(1, 4):
    print (m,end="")
print("221")
print ("--------------------------")
print("nomor 12")
print("122", end="")
for n in range(1, 4):
    print(n, end="")
for o in range(1, 5):
    print(o, end="")
print (str(5)*5, end="")
print (str(6)*6, end="")
for n in range (1, 8):
    print(n, end="")
for o in range(1, 9):
    print(o, end="")
print(str(9)*9, end="")
print("...")
print ("--------------------------")
print("nomor 13")
print("1", end="")
for a in range(1, 3):
    print (a, end="")
for b in range(3, 5):
    print (str(b)*b, end="")
for a in range (1, 6):
    print(a, end="")
for b in range (1, 7):
    print(b, end="")
for a in range(7, 9):
    print (str(a)*a, end="")
for c in range(1, 10):
    print(c, end="")
print("...")
print ("--------------------------")
print("nomor 14")
for n in range (8, 6, -1):
    print(str(n)*n, end="")
for a in range(6, 0, -1):
    print(a, end="")
for b in range(5, 0, -1):
    print (b, end="")
for c in range (4, 2, -1):
    print (str(c)*c, end="")
print("211", end="")
print()
print ("--------------------------")
print("nomor 15")
for a in range(8, 0, -1):
    print (a, end="")
for b in range(7, 0, -1):
    print (b, end="")
for c in range (6, 4, -1):
    print(str(c)*c, end="")
for d in range(4, 0, -1):
    print(d, end="")
for e in range(3, 0, -1):
    print (e, end="")
print("221", end="")
print()
print ("--------------------------")
print("nomor 16")
a = 1
for b in range (12):
    print (a, end=" ")
    if b % 2 ==0:
        a +=4
    else: a-=2
print()
print ("--------------------------")
print("nomor 17")
a = 2
for b in range(10):
    print (a, end=" ")
    if b % 2==0:
        a+=10
    else:
        a-=5
print()
print ("--------------------------")
print("nomor 18")
a = 5
for b in range (12):
    print(a, end=" ")
    if b % 2==0:
        a-=3
    else:
        a+=5
print()
print ("--------------------------")
print("nomor 19")
a = 3
for b in range(10):
    print (a, end=" ")
    if b % 2==0:
        a *=3
    else:
        a-=5
print()
print ("--------------------------")
print("nomor 20")
a = 1
tambah = 1
for b in range(13):
    print(a, end=" ")
    a+=tambah
    tambah+=1
    if tambah>3:
        tambah = 1
print()
print ("--------------------------")
print("nomor 21")
a = 1
for b in range (10):
    print (a, end=" ")
    a*=2
print()
print ("--------------------------")
print("nomor 22")
n= 3
faktorial =1
print (n, end="")
for a in range(n, 0, -1):
    faktorial *=a
    if a!=1:
        print(a,"x",end="")
    else: print(a, "=", end="")
print(faktorial)

print ("--------------------------")
print("nomor 23")
maks = 30
a= 0
b= 1
print("deret vibonaci")
print(a, end=" ")
while b<=maks:
    print(b,end=" ")
    a, b=b, a+b#belom paham
print()
print ("--------------------------")
print("nomor 24")
nawal= 1
nakhir= 30
for a in range(nawal, nakhir, +1):
    if a %3==0:
        print(a, end=" ")
print()
print ("--------------------------")
print("nomor 25")
nawal=1
nakhir=60
for a in range (nawal, nakhir, +1):
    if a %4==0:
        print(a, end=" ")
print()
print ("--------------------------")
print("nomor 26")
nawal=1
nakhir=20
total=0
for a in range(nawal,nakhir, +1):
    total+=a
    print(f"Total bilangan positif dari {nawal} hingga {nakhir} adalah {total}")#belum paham
print ("--------------------------")
print("nomor 27")
nawal = 1
nakhir = 21
total = 0
print(nawal,nakhir)
for a in range(nawal, nakhir, +1):
    if a%2==0:
        print(a, end=" ")
        total +=1
print("jadi total biangan genap", end=" ")
print(total)
print ("--------------------------")
print("nomor 28")
nawal= 1
nakhir = 30
total= 0
print(f"awal {nawal} dan akhir {nakhir}")
for a in range(nawal, nakhir, +1):
    if a%2!=0:
        print (a, end=" ")
        total +=1
print(f"jadi total bilangan ganji adalah {total}", end="")
print()
print ("--------------------------")
print("nomor 29")#belom paham
nawal = 1
nakhir = 50
for a in range (nawal, nakhir, +1):
    if a>1:
        for b in range(2, a):
            if a % b==0:
                break
        else:
            print(a, end=" ")
print()
print ("--------------------------")
print("nomor 30")
nawal= 1
nakhir = 30
totalprima= 0
for a in range(nawal,nakhir,+1):
    if a>1:
        for b in range(2, a):
            if a % b ==0:
                break
        else:
            print(a, end=" ")
            totalprima+=1
print()
print("jumlah total bilangan prima dari 1 hingga 30 adalah")
print(totalprima)