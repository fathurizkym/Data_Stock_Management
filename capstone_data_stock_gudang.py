# Nama : Fathur Rizky Maulana
# Capstone Project Modul 1 - Data Stock Gudang
# Data stock Gudang dengan features : Index, Kode Barang, Nama Barang, Stock Awal, Stock In, Stock Out, Stock Akhir, Transaction Date

import sys
import datetime as dt
import pyinputplus as pypi

# Fungsi menampilkan tanggal sekarang dan petugas gudang
def heading(nama):
    print("=" * 50)
    print(f"\nTanggal : {dt.date.today()} \nPetugas Gudang : {nama}")

# Fungsi menampilkan update stock gudang 
def show(Dict, printFormat):
    print("\nUpdate Laporan Stock Barang PT. XYZ\n")
    for value in Dict.values():
        print(printFormat.format("", *value))

# Fungsi menjalankan menu nomor 1 Report Stock Gudang (Read)
def report():
    while True:
        print("""
----------Menu Report Stock Gudang----------
        
    Pilihan menu report stock gudang : 
    1. Menampilkan semua data stock di gudang
    2. Menampilkan data tertentu di gudang
    3. Kembali ke menu utama
    """)

        menuReportGdg = pypi.inputInt(prompt="Masukan Nomor Pilihan (1-3) : ", lessThan=4)
        if menuReportGdg == 1:
            show(dictStockGdg, printFormat)
        elif menuReportGdg == 2:
            showDataUnique()
        elif menuReportGdg == 3:
            main()
            continue

# Fungsi menjalankan menu nomor 1.2 menampilkan data tertentu di gudang
def showDataUnique():
    inputNamaBarang = pypi.inputStr(prompt="Masukan Nama Barang Yang Dicari : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
    for i, value in enumerate(dictStockGdg.values()):
        if inputNamaBarang in value:
            print("-----Info Barang Yang Dicari-----")
            print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}\n""")
            break
        elif i == len(dictStockGdg) - 1:
            print(f"***Barang {inputNamaBarang} tidak dapat ditemukan***")
            report()
        
# Fungsi menjalankan menu nomor 2 Menambah barang baru di gudang
def add():
    while True:
        menuAdd = pypi.inputInt(prompt="""
----------Menu Menambah Barang Baru Di Data Stock Gudang----------
        
    Pilihan menu menambah barang baru di data stock gudang : 
    1. Tambah barang baru di data stock gudang
    2. Menampilkan semua data stock gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        if menuAdd == 1:
            addBarang = pypi.inputStr(prompt="Masukan nama barang yang ingin ditambahkan : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            for i, value in enumerate(dictStockGdg.copy().values()):
                if addBarang in value:
                    print(f"***{addBarang} sudah ada di dalam database***")
                    add()
                    break
                elif i == len(dictStockGdg) - 1:
                    print("=--- Silahkan input barang yang ingin dimasukan ---=")
                    while True:
                        print(f" -Basis kode barang yang tersedia : {listKodeBarang}")
                        print(f" -Format penulisan kode : BasisKode[UniqueNumber]")
                        kodeBarang = input("Kode Barang  : ").upper()
                        for i, value in enumerate(dictStockGdg.values()):
                            if kodeBarang in value:
                                print("*** Kode barang sudah ada dalam database gudang kami ***")
                                add()
                                break
                            elif i == len(dictStockGdg)-1:
                                if kodeBarang[0:4] in listKodeBarang and (kodeBarang[4]) in ["0","1","2","3","4","5","6","7","8","9"]:
                                    if kodeBarang[0:4] in listKodeBarang:
                                        print(f"Nama Barang  : {addBarang}")
                                        stockAdd = pypi.inputNum(prompt="Stock Barang : ")
                                        yakin = pypi.inputYesNo(prompt="Apakah anda yakin menambah data diatas? (YES/NO) : ")
                                        if yakin == "yes":
                                            stockIn  = 0
                                            stockOut = 0
                                            index = len(dictStockGdg) - 1
                                            dictStockGdg.update({
                                                f"item-{index}" : [
                                                    index,
                                                    kodeBarang,
                                                    addBarang,
                                                    stockAdd,
                                                    stockIn,
                                                    stockOut,
                                                    stockAdd,
                                                    dt.date.today().strftime("%d-%m-%Y")
                                                ]
                                            })
                                            add()
                                        elif yakin == "no":
                                            add()
                                else:
                                    print(f"  *** Kode barang ({kodeBarang[0:4]}) belum terdaftar di sistem kami ***\n  *** Basis kode yang tersedia : {listKodeBarang} ***")
                                    print(f"## Apakah anda tetap ingin menambah barang dengan kode tersebut?")
                                    gotoSettings = pypi.inputYesNo(prompt=f"""## Jika iya, maka anda akan diarahkan menuju menu "Settings Basis Kode Barang" (YES/NO) : """)
                                    if gotoSettings == "yes":
                                        settingBasisKodeBarang()
                                    elif gotoSettings == 'no':
                                        add()
                        break
        elif menuAdd == 2 :
            show(dictStockGdg, printFormat)        
        elif menuAdd == 3 :
            main()
            
# Fungsi menjalankan menu nomor 3 Transaksi stock gudang
def transaction():
    while True:
        menuTransaksi = pypi.inputInt("""
----------Menu Transaksi Barang Stock Gudang----------
        
    Pilihan menu transaksi barang stock gudang : 
    1. Menambah jumlah barang di gudang
    2. Mengurangi jumlah barang di gudang
    3. Menampilkan semua data stock di gudang
    4. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-4) : """, lessThan=5)
        
        if menuTransaksi == 1:
            barangTransaksiIn = pypi.inputStr(prompt="\nMasukan nama barang yang ingin di ditambah stocknya : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            for i, value in enumerate(dictStockGdg.values()):
                if barangTransaksiIn in value:
                    print("----- Info Barang Yang Akan ditambah Stocknya -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinTransaksi = pypi.inputYesNo(prompt="Apakah anda yakin ingin melakukan transaksi barang diatas? (YES/NO) : ")
                    if yakinTransaksi == "yes":
                        transaksiIn = pypi.inputNum(prompt="Jumlah barang IN : ")
                        dictStockGdg.update({
                            f"item-{value[0]}" : [
                                value[0],
                                value[1],
                                value[2],
                                value[3],
                                transaksiIn,
                                value[5],
                                value[3] + transaksiIn - value[5],
                                dt.date.today().strftime("%d-%m-%Y")
                            ]
                        })
                        transaction()
                    elif yakinTransaksi == "no":
                        transaction()
                        break
                elif i == len(dictStockGdg) - 1:
                    print(f"***({barangTransaksiIn}) tidak dapat ditemukan***")
            
        elif menuTransaksi == 2:
            barangTransaksiOut = pypi.inputStr(prompt="\nMasukan nama barang yang ingin di dikurangi stocknya : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            for i, value in enumerate(dictStockGdg.values()):
                if barangTransaksiOut in value:
                    print("----- Info Barang Yang akan dikurangi Stocknya -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinTransaksi = pypi.inputYesNo("Apakah anda yakin ingin melakukan transaksi barang diatas? (YES/NO) : ")
                    if yakinTransaksi == "yes":
                        transaksiOut = pypi.inputNum(prompt="Jumlah barang OUT : ")
                        if transaksiOut <= value[3] + value[4] :
                            dictStockGdg.update({
                                f"item-{value[0]}" : [
                                    value[0],
                                    value[1],
                                    value[2],
                                    value[3],
                                    value[4],
                                    transaksiOut,
                                    value[3] + value[4] - transaksiOut,
                                    dt.date.today().strftime("%d-%m-%Y")
                                ]
                            })
                            transaction()
                        else:
                            print(f"***Jumlah stock barang tidak mencukupi!***\n***Total stock {barangTransaksiOut} : {value[3]+value[4]}***")
                            transaction()
                    elif yakinTransaksi == "no":
                        transaction()
                        break
                elif i == len(dictStockGdg) - 1:
                    print(f"***({barangTransaksiOut}) tidak dapat ditemukan***")

        elif menuTransaksi == 3:
            show(dictStockGdg, printFormat)

        elif menuTransaksi == 4:
            main()

# Fungsi menjalankan menu nomor 4 Menghapus barang lama gudang
def delete():
    print("\n*** Menu ini akan satu data secara keseluruhan ***")
    while True:
        menuAdd = pypi.inputInt("""
----------Menu Menambahkan Stock Gudang----------
        
    Pilihan menu menambahkan stock gudang : 
    1. Hapus data stock di gudang
    2. Menampilkan semua data stock di gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        if menuAdd == 1:
            show(dictStockGdg, printFormat)
            noDelete = pypi.inputNum("\nMasukan nomor barang yang ingin dihapus satu baris : ")
            for i, value in enumerate(dictStockGdg.values()):
                if noDelete in value:
                    print("----- Info Barang Yang Akan dihapus -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinDelete = pypi.inputYesNo(prompt="Apakah anda yakin akan menghapus data diatas? (YES/NO) : ")
                    if yakinDelete == "yes":
                        del dictStockGdg[f"item-{noDelete}"]
                        for key, value in dictStockGdg.copy().items():
                            if key != "column" and value[0] > noDelete:
                                del dictStockGdg[key]
                                dictStockGdg.update({
                                    f"item-{value[0] - 1}" : [
                                        value[0]-1,
                                        value[1],
                                        value[2],
                                        value[3],
                                        value[4],
                                        value[5],
                                        value[6],
                                        value[7],
                                    ]
                                })
                        delete()
                    elif yakinDelete == "no":
                        delete()
                    break
                elif i == len(dictStockGdg) - 1:
                    print(f"***Index ({noDelete}) tidak dapat ditemukan***")
                    delete()
        elif menuAdd == 2 :
            show(dictStockGdg, printFormat)        
        elif menuAdd == 3 :
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")

# Fungsi menjalankan menu nomor 5 Settings
def settings():
    while True:
        menuSettings = pypi.inputInt("""
----------Menu Settings Stock Gudang----------
        
    Pilihan menu settings stock gudang : 
    1. Setting Petugas Gudang
    2. Setting Basis Kode Barang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        if menuSettings == 1:
            settingPetugasGudang()
        elif menuSettings == 2:
            settingBasisKodeBarang()
        elif menuSettings == 3:
            main()

# Fungsi menjalankan Setting Petugas Gudang
def settingPetugasGudang():
    while True:
        settingPetugas = pypi.inputInt("""
----------Menu Settings Stock Gudang----------
        
    Pilihan menu settings stock gudang : 
    1. Menampilkan Petugas Gudang
    2. Mengedit Nama Petugas Gudang
    3. Menambah Petugas Gudang Baru
    4. Menghapus Petugas Gudang Lama
    5. Kembali Ke Menu Settings
    6. Kembali Ke Menu Utama
    
    Masukan Nomor Pilihan (1-6) : """, lessThan=7)
        
        # Pilihan Menampilkan Petugas Gudang
        if settingPetugas == 1:
            print("\nNama Petugas Gudang Terdaftar : ")
            for i in range(len(petugasGudang)):
                print(f"Petugas-{i+1} : {petugasGudang[i]}")
            settingPetugasGudang()

        # Pilihan Mengedit Nama Petugas Gudang
        elif settingPetugas == 2:
            print("\nNama Petugas Gudang Terdaftar : ")
            for i in range(len(petugasGudang)):
                print(f"Petugas-{i+1} : {petugasGudang[i]}")
            noEditPetugas = pypi.inputInt(prompt="No petugas yang ingin diedit : ", lessThan=len(petugasGudang)+1)
            namaPetugasEdit = pypi.inputStr(prompt="Masukan nama petugas baru : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            yakinEditPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin merubah {petugasGudang[noEditPetugas-1]} menjadi {namaPetugasEdit} ? (YES/NO) : ")
            if yakinEditPetugas == "yes":
                petugasGudang[noEditPetugas-1] = namaPetugasEdit
                settingPetugasGudang()
            elif yakinEditPetugas == "no":
                settingPetugasGudang()

        # Pilihan Menambah Petugas Baru
        elif settingPetugas == 3:
            nambahPetugas = pypi.inputStr(prompt="Masukan nama petugas gudang baru : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            if nambahPetugas in petugasGudang:
                print(f"*** Nama petugas {nambahPetugas} sudah ada dalam database ***")
                settingPetugasGudang()
            elif nambahPetugas not in petugasGudang:
                yakinTambahPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin menambah {nambahPetugas} kedalam database gudang ? (YES/NO) : ")
                if yakinTambahPetugas == "yes":
                    petugasGudang.append(nambahPetugas)
                    settingPetugasGudang()
                elif yakinTambahPetugas == "no":
                    settingPetugasGudang()

        # Pilihan Menghapus Petugas Gudang Lama
        elif settingPetugas == 4:
            print("\nNama Petugas Gudang Terdaftar : ")
            for i in range(len(petugasGudang)):
                print(f"Petugas-{i+1} : {petugasGudang[i]}")
            hapusPetugas = pypi.inputStr(prompt="Masukan nama petugas yang ingin dihapus : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            if hapusPetugas in petugasGudang:
                yakinHapusPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin menghapus {hapusPetugas} dari database gudang ? (YES/NO) : ")
                if yakinHapusPetugas == "yes":
                    petugasGudang.remove(hapusPetugas)
                    settingPetugasGudang()
                elif yakinHapusPetugas == "no":
                    settingPetugasGudang()
            elif hapusPetugas not in petugasGudang:
                print(f"*** Nama petugas {hapusPetugas} tidak ada dalam database ***")

        # Pilihan Kembali Ke Menu Settings
        elif settingPetugas == 5:
            settings()
        
        # Pilihan Untuk Langsung Kembali Ke Menu Utama
        elif settingPetugas == 6:
            main()
    
# Fungsi menjalankan Setting Basis Kode Barang
def settingBasisKodeBarang():
    while True:
        settingKode = pypi.inputInt("""
----------Menu Settings Basis Kode Barang----------
        
    Pilihan menu settings Basis kode barang : 
    1. Menampilkan List Basis Kode Barang
    2. Mengedit Basis Kode Barang
    3. Menambah Basis Kode Barang
    4. Menghapus Basis Kode Barang Lama
    5. Kembali Ke Menu Settings
    6. Kembali Ke Menu Utama
    
    Masukan Nomor Pilihan (1-6) : """, lessThan=7)
        
        # Pilihan Menampilkan Basis Kode Barang Tersedia
        if settingKode == 1:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            settingBasisKodeBarang()

        # Pilihan Mengedit Basis Kode Barang Tersedia
        elif settingKode == 2:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            noEditBasisKode = pypi.inputInt(prompt="No basis kode yang ingin diedit : ", lessThan=len(listKodeBarang)+1)
            namaBasisKodeEdit = pypi.inputStr(prompt="Masukan nama basis kode baru : ", applyFunc=lambda x: x.upper(), blockRegexes="0123456789")
            yakinEditBasisKode = pypi.inputYesNo(prompt=f"Apakah anda yakin merubah basis kode {listKodeBarang[noEditBasisKode-1]} menjadi {namaBasisKodeEdit} ? (YES/NO) : ")
            if yakinEditBasisKode == "yes":
                listKodeBarang[noEditBasisKode-1] = namaBasisKodeEdit
                settingBasisKodeBarang()
            elif yakinEditBasisKode == "no":
                settingBasisKodeBarang()

        # Pilihan Menambah Basis Kode Barang Baru
        elif settingKode == 3:
            print("## Panjang karakter basis kode baru kurang dari 5 termasuk karakter strip (-)")
            nambahBasisKode= pypi.inputStr(prompt="Masukan nama basis kode baru : ", applyFunc=lambda x: x.upper(), blockRegexes="0123456789")
            if nambahBasisKode in listKodeBarang:
                print(f"*** Basis Kode {nambahBasisKode} sudah ada dalam database ***")
                settingBasisKodeBarang()
            elif len(nambahBasisKode) > 4:
                print("*** Jumlah karakter terlalu banyak! ***")
                settingBasisKodeBarang()
            elif nambahBasisKode not in listKodeBarang:
                yakinTambahBasisKode = pypi.inputYesNo(prompt=f"Apakah anda yakin menambah {nambahBasisKode} kedalam database gudang ? (YES/NO) : ")
                if yakinTambahBasisKode == "yes":
                    listKodeBarang.append(nambahBasisKode)
                    settingBasisKodeBarang()
                elif yakinTambahBasisKode == "no":
                    settingBasisKodeBarang()

        # Pilihan Menghapus Basis Kode Barang Lama
        elif settingKode == 4:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            hapusBasisKode = pypi.inputStr(prompt="Masukan nama basis kode yang ingin dihapus : ", applyFunc=lambda x: x.upper(), blockRegexes="0123456789")
            if hapusBasisKode in listKodeBarang:
                yakinHapusBasisKode = pypi.inputYesNo(prompt=f"Apakah anda yakin menghapus {hapusBasisKode} dari database gudang ? (YES/NO) : ")
                if yakinHapusBasisKode == "yes":
                    listKodeBarang.remove(hapusBasisKode)
                    settingBasisKodeBarang()
                elif yakinHapusBasisKode == "no":
                    settingBasisKodeBarang()
            elif hapusBasisKode not in listKodeBarang:
                print(f"*** Nama basis kode {hapusBasisKode} tidak ada dalam database ***")

        # Pilihan Kembali Ke Menu Settings
        elif settingKode == 5:
            settings()

        # Pilihan Untuk Langsung Kembali Ke Menu Utama
        elif settingKode == 6:
            main()

# Fungsi menampilkan menu utama
def main():
    while True:
        print(
            """
==================================================
-----Selamat Datang di Aplikasi Gudang PT.XYZ-----

        Pilihan Menu :
        1. Report Stock Gudang
        2. Menambah Barang Baru Gudang
        3. Transaksi Stock Gudang
        4. Menghapus Barang Lama Gudang
        5. Settings
        6. Exit
    """
    )
        menuNumber = pypi.inputInt(
            prompt="Masukan Nomor Pilihan (1-6): ",
            lessThan=7)
        if menuNumber == 1:
            report()
        elif menuNumber == 2:
            add()
        elif menuNumber == 3:
            transaction()
        elif menuNumber == 4:
            delete()
        elif menuNumber == 5:
            settings()
        elif menuNumber == 6:
            print("\n~~~~Terimakasih~~~~\nProgram made by : fathurizkym")
            sys.exit()
        else:
            print("Nomor menu yang dipilih tidak sesuai.\nMasukan nomor sesuai yang tertera diatas")

# Fungsi Start Program
def start():
    startProgram = pypi.inputYesNo(prompt="Jalankan program? (YES/NO) : ")
    if startProgram == "yes":
        if len(dictStockGdg) == 0:
            print("Tidak ada data untuk diproses")
        else:
            while True:
                inputPtgs = pypi.inputStr(
                    prompt="\nMasukan Nama Petugas Jaga : ",
                    applyFunc=lambda x: x.title(),
                    blockRegexes="0123456789")
                if inputPtgs in petugasGudang:
                    print(f"\nLogin sukses\nNama petugas gudang : {inputPtgs}")
                    heading(inputPtgs)
                    main()
                    break
                else:
                    print(f"Nama anda ({inputPtgs}) tidak ada dalam database petugas gudang kami")
                    print(f"Silahkan minta izin ke petugas gudang kami : \n{petugasGudang}")
    elif startProgram == "no":
        sys.exit()


if __name__ == "__main__":
    # Dictionary stock Gudang
    dictStockGdg = {
        "column" : ["Index", "Kode Barang", "Nama Barang", "Stock Awal", "Stock In", "Stock Out", "Stock Akhir", "Date"],
        "item-0" : [0, "FRM-0", "Barang A", 10, 0, 0, 10, dt.date(2023,1,1).strftime("%d-%m-%Y")],
        "item-1" : [1, "FRM-1", "Barang B", 20, 0, 0, 20, dt.date(2023,1,2).strftime("%d-%m-%Y")],
        "item-2" : [2, "FRM-2", "Barang C", 15, 0, 0, 15, dt.date(2023,1,3).strftime("%d-%m-%Y")],
    }

    petugasGudang = [
        "Fathur", 
        "Fitra Fauzan", 
        "Andi Nurmansyah", 
        "Harits Ramadhan", 
        "Rona Mardiana",
    ]

    listKodeBarang = [
        "FRM-",
        "RMF-",
        "MFR-",
    ]

    printFormat = '{:<1}' + '{:<15}' * (len(dictStockGdg["column"]))

    start()