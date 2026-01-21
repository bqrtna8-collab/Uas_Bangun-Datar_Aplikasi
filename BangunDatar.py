#Daftar Nama Bangun Datar 
Daftar_Bangun_Datar = ["Segitiga","Lingkaran","Persegi","Persegi panjang","Jajar genjang","Belah ketupat"]

#Bagian Rumus
def rumus_segitiga():
    a = float(input("alas:"))
    t = float(input("tinggi:"))
    sm = float(input("sisi miring:"))
    print("Luasnya adalah =", (a * t) / 2)
    print("Kelilingnya adalah =", a + t + sm)
def rumus_lingkaran():
    r = float(input("jari-jari:"))
    print("Luasnya adalah =", 3.14 * r * r)
    print("Kelilingnya adalah =", 2 * 3.14 * r)
def rumus_persegi():
    s = float(input("sisi:"))
    print("Luasnya adalah =", s * s)
    print("Kelilingnya adalah =", 4 * s)
def rumus_persegi_panjang():
    p = float(input("panjang:"))
    l = float(input("lebar:"))
    print("Luasnya adalah =", p * l)
    print("Kelilingnya adalah =", 2 * (p + l))
def rumus_jajar_genjang():
    a = float(input("alas:"))
    t = float(input("tinggi:"))
    sm = float(input("sisi miring"))
    print("Luasnya adalah =", a * t)
    print("Kelilingnya adalah =", 2 * ( a + sm))
def rumus_belah_ketupat():
    d1 = int(input("Diagonal 1:"))
    d2 = int(input("diagonal 2:"))
    s = float(input("sisi:"))
    print("Luasnya adalah =", (d1 * d2) / 2)
    print("Kelilingnya adalah =", 4 * s)

#Program Mulai
nama = input("nama :")
ulang = "ya"

while ulang == "ya":
    print("\n--- Pilih bangun datar ---")
    print("1.", Daftar_Bangun_Datar[0])
    print("2.", Daftar_Bangun_Datar[1])
    print("3.", Daftar_Bangun_Datar[2])
    print("4.", Daftar_Bangun_Datar[3])
    print("5.", Daftar_Bangun_Datar[4])
    print("6.", Daftar_Bangun_Datar[5])

    pilih = input ("pilih nomor (1-6):")

    if pilih == "1":
        rumus_segitiga()
    elif pilih == "2":
        rumus_lingkaran()
    elif pilih == "3":
        rumus_persegi()
    elif pilih == "4":
        rumus_persegi_panjang()
    elif pilih == "5":
        rumus_jajar_genjang()
    elif pilih == "6":
        rumus_belah_ketupat()
    else:
        print("pilihan salah")

    ulang = input("mau dihitung lanjut yang lain? (ya/tidak):")
    print("selesai, terimakasihya" + nama)

