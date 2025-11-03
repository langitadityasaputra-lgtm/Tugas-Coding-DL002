print ("nomor 1===============")
tinggi = 6
for a in range(tinggi):
    for bintang in range(tinggi - a):
        print("*", end="")    
    for spasi in range (2 * a - 1):
        print(" ", end="")
    for bintang in range(tinggi - a):
            print("*", end="")
    print()
print ("nomor 2===============")
tinggi = 7
for a in range(tinggi):
    for spasi in range(tinggi - a - 1):
        print (" ", end="")
    for bintang in range(2 * a - 1):
        print("*", end="")
    print()

print ("nomor 3================")
tinggi = 3
for a in range (tinggi):
    for bintang in range(1 * a + 1):
        print("*", end="")
    print()
tinggi = 3
for b in range(tinggi):
    for spasi in range(tinggi - b - 1):
        print(" ", end="")
    for bintang in range (b + 1):
        print("*", end="")
    print()
print ("nomor 4================")
tinggi = 5
for a in range(tinggi):
    for bintang in range(a + 1):
        print("*", end="")
    for spasi in range((tinggi - a - 1)*2):
        print(" ", end="")
    for bintang in range(a + 1):
        print("*", end="")
    print()
for bintang in range(tinggi * 2):
    print("*", end="")
print()
print ("nomor 5================")
tinggi = 6
for a in range (tinggi, 0, -1):
    for spasi in range (tinggi - a):
        print(" ", end="")
    for bintang in range(2*a-1):
        print("*", end="")
    print()
print ("nomor 6================")
tinggi = 3
for a in range (tinggi):
    for spasi in range(tinggi - a - 1):
        print (" ", end="")
    for bintang in range(a+1):
        print("*", end="")
    print()
tinggi = 3
for a in range(tinggi):
    for bintang in range(1 * a +1):
        print("*", end="")
    print()
print ("nomor 7================")
tinggi = 5
for a in range(tinggi, 0, -1):
    for spasi in range(tinggi - a):
        print(" ", end="")
    for bintang in range(a):
        print("*", end="")
    print()
for a in range(2, tinggi + 1):
    for spais in range(tinggi - a):
        print(" ", end="")
    for bintang in range(a):
        print("*", end="")
    print()
print ("nomor 8================")
baris = 6
kolom = 11

for i in range(baris):
    if i == baris - 1:
        print("0" * kolom)
    else:
        print("0" + "*" * (kolom - 1))
print ("nomor 9================")
baris = 6
kolom = 11

for i in range(baris):
    if i == baris - 1:
        print("0" * kolom)
    else:
        print("*" * (kolom - 1) + "0")
print ("nomor 10===============")
tinggi = 5
for a in range(tinggi, 0, -1):
    print("*" * a)
for a in range(2, tinggi + 1):
    print("*" * a)
print ("nomor 11===============")
baris = 6
kolom = 11

for i in range(baris):
    if i == 0:
        print("0" * kolom)
    else:
        print("0" + "*" * (kolom - 1))
print ("nomor 12===============")
baris = 6
kolom = 11

for i in range(baris):
    if i == 0:
        print("0" * kolom)
    else:
        print("*" * (kolom - 1) + "0")
print ("nomor 13===============")
tinggi = 6

for i in range(tinggi):
    print("0" * (i + 1) + "*" * (tinggi - i))
print ("nomor 14===============")
tinggi = 6
for i in range(tinggi):
    print("*" * (i + 1) + "0" * (tinggi - i))
print ("nomor 15===============")
tinggi = 6
for i in range(tinggi):
    print("0" * (tinggi - i) + "*" * (i + 1))
print ("nomor 16===============")
tinggi = 6
for i in range(tinggi):
    print("0" * (tinggi - i) + "*" * (i + 1))
print ("nomor 17===============")
tinggi = 7
for i in range(tinggi):
    for j in range(tinggi):
        if j == tinggi - i - 1:
            print("*", end="")
        else:
            print("0", end="")
    print()
print ("nomor 18===============")
tinggi = 7
for i in range(tinggi):
    for j in range(tinggi):
        if j == i:
            print("*", end="")
        else:
            print("0", end="")
    print()
print ("nomor 19===============")
baris = 6
kolom = 7
for i in range(baris):
    for j in range(kolom):
        if i == 0 or i == baris - 1: 
            print("0", end="")
        elif j == 0 or j == kolom - 1:
            print("0", end="")
        else:                         
            print("*", end="")
    print()
print ("nomor 20===============")
baris = 6
kolom = 7
for i in range(baris):
    if i % 3 == 0:
        print("0" * kolom)
    elif i % 3 == 1:
        print("*" * kolom)
    else:
        print("=" * kolom)