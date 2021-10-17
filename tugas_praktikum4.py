print(" menghitung hari dalam satubulan")
print(" Enter -1 to stop the program")
n = ''
o = ''
while n != -1:
    n = int(input(" masukan bulan (1-12) = "))
    if n == 1:
        print(" ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 2:
        p = int(input(" masukan tahun (e.g., 2021) = "))
        if p % 4 == 0 and p % 100 != 0 or p % 400 == 0:
            print (" Ada 29 hari dalam satu bulan ")
            print(" Masukkan -1 untuk menghentikan program ")
        else:
            print(" Ada 28 hari dalam satu bulan ")
            print(" Masukkan -1 untuk menghentikan program ")
    elif n == 3:
        print(" Ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 4:
        print(" Ada 30 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 5:
        print(" Ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 6:
        print(" Ada 30 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 7:
        print(" Ada 31 hari dalam setu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 8:
        print(" Ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 9:
        print(" Ada 30 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 10:
        print(" Ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 11:
        print(" Ada 30 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n == 12:
        print(" Ada 31 hari dalam satu bulan ")
        print(" Masukkan -1 untuk menghentikan program ")
    elif n >= 12:
        print(" tidak ada bulan = ", n)
        print(" Masukkan -1 untuk menghentikan program ")
    else:
        print(" selesai ")