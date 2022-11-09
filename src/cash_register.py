import os

# Inisialisasi variabel
lagi = 'y'
Troli = []
Harga = []
Cash = []
Jumlah = []

# Definisi prosedur (login, welcome, main menu, hp, accessories, exit) 
def login():
    log = False
    while (log == False):
        print()
        print ("******************************")
        print ("            Login             ")
        print ("******************************")
        print()
        nama = input("Masukkan username: ")
        pswd = input("Masukkan password: ")
        if(nama == 'Admin' and pswd == '12345678' ):
            os.system('cls')
            log = True
        else:
            print()
            print("Username/Paswword salah, silahkan coba lagi!")
            os.system('cls')
            continue

def welcome():
    print ()   
    print ("==============================")
    print (" Selamat Datang di STEI-phone ")
    print ("==============================")

def mainmenu():
    print()
    print("Barang yang tersedia")
    print()
    print ("1 | Handphone                 ")
    print ("2 | Accessories               ")
    print ("3 | Exit                      ")
    print()
    print ("Masukkan nomor pilihan: ",end='')

# Pilihan pertama (Hp, Accessories, Exit)
def hp():
    while(lagi == 'y' or lagi == 'Y'):
        print()
        print("1. Samsung")
        print("2. Xiaomi")
        print("3. Iphone")
        print()
        merk = int(input("Masukkan nomor pilihan: "))
        if(merk == 1):
            os.system('cls')
            samsung("Samsung A51", "Samsung A71")
            tipesamsung = int(input("Masukkan tipe samsung: "))
            if (tipesamsung > 2 or tipesamsung < 1 ):
                os.system('cls')
                continue
            else:
                jumlahsamsung = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahsamsung)
                c = hargasamsung(tipesamsung)
                Harga.append(c)
                h = jumlahsamsung*hargasamsung(tipesamsung)
                Cash.append(h)
                n = namasamsung(tipesamsung)
                Troli.append(n)
                break
       
        elif(merk == 2):
            os.system('cls')
            xiaomi("Redmi Note 10s", "Redmi Note 10 5G")
            tipexiaomi = int(input("Masukkan tipe xiaomi: "))
            if (tipexiaomi > 2 or tipexiaomi < 1 ):
                os.system('cls')
                continue
            else:
                jumlahxiaomi = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahxiaomi)
                c = hargaxiaomi(tipexiaomi)
                Harga.append(c)
                h = jumlahxiaomi*hargaxiaomi(tipexiaomi)
                Cash.append(h)
                n = namaxiaomi(tipexiaomi)
                Troli.append(n)
                break  

        elif(merk == 3):
            os.system('cls')
            iphone("iPhone 12 mini", "iPhone 12")
            tipeiphone = int(input("Masukkan tipe Iphone: "))
            if (tipeiphone > 2 or tipeiphone < 1 ):
                os.system('cls')
                continue
            else:
                jumlahiphone = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahiphone)
                c = hargaiphone(tipeiphone)
                Harga.append(c)
                h = jumlahiphone*hargaiphone(tipeiphone)
                Cash.append(h)
                n = namaiphone(tipeiphone)
                Troli.append(n)
                break 

        else:
            os.system('cls')
            continue

def accessories():
    while(lagi == 'y' or lagi == 'Y'):
        print()
        print("1. Case Hp")
        print("2. Charger")
        print("3. Galaxy Buds")
        print()
        accessories = int(input("Masukkan nomor pilihan: "))
        if(accessories == 1):
            os.system('cls')
            case("Samsung A51", "Samsung A71", "Xiaomi Redmi Note 10s", "Xiaomi Redmi Note 10 5G", "IPhone 12 mini", "IPhone 12")
            tipecase = int(input("Masukkan tipe case: "))
            if (tipecase > 6 or tipecase < 1 ):
                os.system('cls')
                continue
            else:
                jumlahcase = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahcase)
                c = hargacase(tipecase)
                Harga.append(c)
                h = jumlahcase*hargacase(tipecase)
                Cash.append(h)
                n = namacase(tipecase)
                Troli.append(n)
                break
       
        elif(accessories == 2):
            os.system('cls')
            charger("Micro USB", "Type C", "Lightning")
            tipecharger = int(input("Masukkan tipe charger: "))
            if (tipecharger > 3 or tipecharger < 1 ):
                os.system('cls')
                continue
            else:
                jumlahcharger = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahcharger)
                c = hargacharger(tipecharger)
                Harga.append(c)
                h = jumlahcharger*hargacharger(tipecharger)
                Cash.append(h)
                n = namacharger(tipecharger)
                Troli.append(n)
                break   
        elif(accessories == 3):
            os.system('cls')
            galaxybuds("Galaxy Buds2", "Galaxy Buds Pro")
            tipegalaxybuds = int(input("Masukkan tipe Galaxy Buds: "))
            if (tipegalaxybuds > 2 or tipegalaxybuds < 1 ):
                os.system('cls')
                continue
            else:
                jumlahgalaxybuds = int(input("Masukkan kuantitas: "))
                Jumlah.append(jumlahgalaxybuds)
                c = hargagalaxybuds(tipegalaxybuds)
                Harga.append(c)
                h = jumlahgalaxybuds*hargagalaxybuds(tipegalaxybuds)
                Cash.append(h)
                n = namagalaxybuds(tipegalaxybuds)
                Troli.append(n)
                break 
        else:
            os.system('cls')
            continue
def exit():
  print()
  print("You have been successfully logged out")
  print()


def panjangTroli():
    l = len(Troli[i])
    while (l<25):
        print(" ",end='')
        l += 1

def panjangHarga():
    l = len(str(Harga[i]))
    while (l<25):
        print(" ",end='')
        l += 1

def samsung(pil1,pil2):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print()

def xiaomi(pil1,pil2):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print()

def iphone(pil1,pil2):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print()

def galaxybuds(pil1, pil2):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print()

def case(pil1, pil2, pil3, pil4, pil5, pil6):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print("3 |",str(pil3))
    print("4 |",str(pil4))
    print("5 |",str(pil5))
    print("6 |",str(pil6))
    print()

def charger(pil1, pil2, pil3):
    print()
    print("1 |",str(pil1))
    print("2 |",str(pil2))
    print("3 |",str(pil3))
    print()

# Fungsi harga
def hargasamsung(x):
    if(x == 1):
        h = 4999000
        return h 
    elif(x == 2):
        h = 6999000
        return h

def hargaxiaomi(x):
    if(x == 1):
        h = 2699000
        return h 
    elif(x == 2):
        h = 2799000
        return h

def hargaiphone(x):
    if(x == 1):
        h = 10999000
        return h 
    elif(x == 2):
        h =  12999000
        return h

def hargacase(x):
    if(x == 1):
        h = 150000
        return h 
    elif(x == 2):
        h = 200000
        return h
    elif(x == 3):
        h = 100000
        return h
    elif(x == 4):
        h = 100000
        return h
    elif(x == 5):
        h = 150000
        return h
    elif(x == 6):
        h = 200000
        return h

def hargacharger(x):
    if(x == 1):
        h = 150000
        return h 
    elif(x == 2):
        h = 100000
        return h
    elif(x == 3):
        h = 200000
        return h

def hargagalaxybuds(x):
    if(x == 1):
        h = 1699000
        return h 
    elif(x == 2):
        h = 2499000
        return h

# Fungsi nama
def namasamsung(x):
    if(x == 1):
        n = 'Samsung A51'
        return n
    elif(x == 2):
        n = 'Samsung A71'
        return n

def namaxiaomi(x):
    if(x == 1):
        n = 'Redmi Note 10s'
        return n
    elif(x == 2):
        n = 'Redmi Note 10 5G'
        return n

def namaiphone(x):
    if(x == 1):
        n = 'IPhone 12 mini'
        return n
    elif(x == 2):
        n = 'IPhone 12'
        return n

def namacase(x):
    if(x == 1):
        n = 'Case Samsung A51'
        return n
    elif(x == 2):
        n = 'Case Samsung A71'
        return n
    elif(x == 3):
        n = 'Case Redmi Note 10s'
        return n
    elif(x == 4):
        n = 'Case Redmi Note 10 5G'
        return n
    elif(x == 5):
        n = 'Case IPhone 12 mini'
        return n
    elif(x == 6):
        n = 'Case IPhone 12'
        return n

def namacharger(x):
    if(x ==1 ):
        n = 'Charger Micro USB '
        return n
    elif(x == 2):
        n = 'Charger Type C '
        return n
    elif(x == 3):
        n = 'Charger Lightning '
        return n

def namagalaxybuds(x):
    if(x == 1):
        n = 'Galaxy Buds 2'
        return n
    elif(x == 2):
        n = 'Galaxy Buds Pro'
        return n

# Main Program        
login()
welcome()
while(lagi == 'y' or lagi == 'Y'):
    mainmenu()
    opt = int(input())
    if (opt==1):
      os.system('cls')
      hp()
    elif (opt == 2):
      os.system('cls')
      accessories()
    elif (opt == 3):
      exit()
      break

    os.system('cls')
    X1 = len(Troli)
    print("Daftar yang dibeli: ")
    for i in range (X1):
        print(' ', Jumlah[i], sep='', end = '')
        print(' x ', Troli[i], sep='')
        print()
    print()
    lagi = input("Apakah ingin belanja lagi? {Y/T}: ")
    if(lagi == 'y'):
        os.system('cls')
        continue
    elif(lagi == 't' or lagi == 'T'):
        os.system('cls')
        total = sum(Cash)
        print()
        print("=============================================================================")
        print("                                 STEI-phone                                   ")
        print("=============================================================================")
        print()
        import datetime
        print(" Telp: 0854-3212-3456                             ", datetime.datetime.now().replace(microsecond=0).isoformat(' '))
        pembeli = (input(" Pembeli: "))
        print(" Nama Barang                 | Harga Satuan              | Harga Total     ")
        X1 = len(Troli)
        for i in range (X1):
            print(' ', Jumlah[i], sep='', end = '')
            print(' x ', Troli[i], sep='', end = '')
            panjangTroli()
            print(' RP', Harga[i],  sep='', end = '')
            panjangHarga()
            print(' RP', Cash[i], sep='')
        print("____________________________________________________________________________+")
        print("Total                                                    : RP"+str(total))
        uang = int(input("Tunai                                                    : RP"))
        kembali = uang-total
        if kembali >= 0:
            kembali = str("Rp" + str(kembali))
        else:
            kembali = str("Transaksi tidak dapat dilakukan")
        print("Kembali                                                  : " + (kembali))
        break