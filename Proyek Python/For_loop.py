"""
For Loop
@project_python
ⒸCopyright cone
"""

# Basic
print("basic")

fruit = ["apple","banana","cherry"]
for x in fruit:
    print(x) # appple, Banana, cherry

# Break
print("break")

huruf = "angka"
for y in huruf:
    print(y)
    if y == "g":
        break

#continue
print("continue")

nama = ['adit',"sopo","jarwo"]
for x in nama:
    if x == "sopo":
        continue
    print(x) # adit, jarwo


# Range (rentang)
print("range")

for z in range(5,50,10):
    print(z)
    #note:dimulai dari lima, Sampai 40, Naik 10


# else
        #a
print("else")

for x in range(5):
    print(x)
else:
    print("finally finished")

        #b
for j in range(6):
    if j == 3:  break
    print(j)
else:
    print("j berakhir") # tidak dijalankan karena diberhentikan oleh break


# Nested loop(loop bersarang)
    #loop dalam akan dieksekusi satu kali untuk setiap iterasi dari loop luar/loop dalam dituntaskan terlebih dahulu
print("nested loop")

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for xx in adj:
    for yy in fruits:
        print(yy)
        print(xx,yy)


# pass
    # for loop tidak boleh kosong/masukkan pass peernyataan untuk menghindari kesalahan for loop yang kosong
print("pass")

for x in range(0,1,2):
    pass



"""
note:

"""