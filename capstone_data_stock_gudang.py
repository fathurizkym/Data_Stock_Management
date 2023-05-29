# Nama : Fathur Rizky Maulana
# Capstone Project Modul 1 - Data Stock Gudang

import sys
import datetime as dt
import pyinputplus as pypi
import csv
import tabulate

# Fungsi menampilkan tanggal sekarang dan petugas gudang 
def heading(nama):
    print("=" * 50)
    print(f"\nTanggal : {dt.date.today()} \nPetugas Gudang : {nama}")

# Fungsi menampilkan update stock gudang 

def show(dbStockGudang):
    if len(dbStockGudang) <= 1 or "column" not in dbStockGudang.keys():
        print("*** Data Stock Gudang Kosong/ Tidak Ada ***")
    else:
        print("\n===== Update Laporan Stock Barang PT. XYZ =====\n")
        data = list(dbStockGudang.values())[1:]
        header = dbStockGudang['column']
        print(tabulate.tabulate(data, header, tablefmt="outline"))


# Fungsi menjalankan menu nomor 1 Report Stock Gudang (Read)
def report():
    while True:
        print("""\n
---------- Menu Report Stock Gudang ----------
        
    Pilihan menu report stock gudang : 
    1. Menampilkan data stock gudang
    2. Menampilkan informasi item 
    3. Kembali ke menu utama
    """)

        menuReportGdg = pypi.inputInt(prompt="Masukan Nomor Pilihan (1-3) : ", lessThan=4)
        if menuReportGdg == 1:
            show(dbStockGudang)
        elif menuReportGdg == 2:
            showDataUnique()
        elif menuReportGdg == 3:
            main()

# Fungsi menjalankan menu nomor 1.2 Menampilkan Data Tertentu Di Gudang (Read)
def showDataUnique():
    inputNamaBarang = pypi.inputStr(prompt="Masukan Nama Barang Yang Dicari : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
    for i, value in enumerate(dbStockGudang.values()):
        if inputNamaBarang in value:
            print("----- Info Barang Yang Dicari -----")
            print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTanggal\t\t : {value[7]}""")
            print("-" * 35)
            break
        elif i == len(dbStockGudang) - 1:
            print(f"*** Barang {inputNamaBarang} tidak dapat ditemukan ***")
            report()
        

# Fungsi menjalankan menu nomor 2 Menambah Barang Baru Di Gudang (Create, Read)
def add():
    while True:
        menuAdd = pypi.inputInt(prompt="""\n
---------- Menu Menambah Barang Baru Di Data Stock Gudang ----------
         
    Pilihan menu menambah barang baru di data stock gudang : 
    1. Menambah barang baru di data stock gudang
    2. Menampilkan semua data stock gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        # Pilihan Menjalankan Menu Tambah barang baru di data stock gudang (Create)
        if menuAdd == 1:
            addBarang = pypi.inputStr(prompt="Masukan nama barang yang ingin ditambahkan : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            for i, value in enumerate(dbStockGudang.copy().values()):
                if addBarang in value:
                    print(f"***{addBarang} sudah ada di dalam database***")
                    add()
                    break
                elif i == len(dbStockGudang) - 1:
                    print("=--- Silahkan input barang yang ingin dimasukan ---=")
                    while True:
                        print(f" -Basis kode barang yang tersedia : {listKodeBarang}")
                        print(f" -Format penulisan kode : BasisKode[UniqueNumber]")
                        kodeBarang = input("Kode Barang  : ").upper()
                        for i, value in enumerate(dbStockGudang.values()):
                            if kodeBarang in value:
                                print(f"*** Kode barang ({kodeBarang}) sudah ada dalam database gudang kami ***")
                                add()
                                break
                            elif i == len(dbStockGudang)-1:
                                if kodeBarang[0:4] in listKodeBarang and (kodeBarang[4]) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                                    print(f"Nama Barang  : {addBarang}")
                                    stockAdd = pypi.inputNum(prompt="Stock Barang : ")
                                    yakin = pypi.inputYesNo(prompt="Apakah anda yakin menambah data diatas? (YES/NO) : ")
                                    if yakin == "yes":
                                        stockIn  = 0
                                        stockOut = 0
                                        index = len(dbStockGudang) - 1
                                        dbStockGudang.update({
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
                                    print(f"  *** Kode barang tidak sesuai/ belum terdaftar di sistem kami ***\n  *** Basis kode yang tersedia : {listKodeBarang} ***")
                                    print(f"## Apakah anda tetap ingin menambah barang dengan kode tersebut?")
                                    gotoSettings = pypi.inputYesNo(prompt=f"""## Jika iya, maka anda akan diarahkan menuju menu "Settings Basis Kode Barang" (YES/NO) : """)
                                    if gotoSettings == "yes":
                                        settingBasisKodeBarang()
                                    elif gotoSettings == 'no':
                                        add()
                        break

        # Pilihan Menjalankan Menu Menampilkan semua data stock gudang (Read)
        elif menuAdd == 2 :
            show(dbStockGudang)   

        # Pilihan Menjalankan Menu Kembali ke menu utama
        elif menuAdd == 3 :
            main()


# Fungsi menjalankan menu nomor 3 Transaksi Stock Gudang (Update, Read)
def transaksi():
    while True:
        menuTransaksi = pypi.inputInt("""\n
---------- Menu Transaksi Barang Stock Gudang ----------
        
    Pilihan menu transaksi barang stock gudang : 
    1. Menambah jumlah barang di gudang
    2. Mengurangi jumlah barang di gudang
    3. Menampilkan semua data stock di gudang
    4. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-4) : """, lessThan=5)
        
        # Pilihan Menjalankan Menu Menambah jumlah barang di gudang (Update)
        if menuTransaksi == 1:
            barangTransaksiIn = pypi.inputStr(prompt="\nMasukan nama barang yang ingin di ditambah stocknya : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            for i, value in enumerate(dbStockGudang.values()):
                if barangTransaksiIn in value:
                    print("----- Informasi Barang Yang Akan Dilakukan Transaksi (Stock IN) -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTanggal\t\t : {value[7]}""")
                    print("-" * 70)
                    yakinTransaksi = pypi.inputYesNo(prompt="Apakah anda yakin ingin melakukan transaksi barang diatas? (YES/NO) : ")
                    if yakinTransaksi == "yes":
                        transaksiIn = pypi.inputNum(prompt="Jumlah barang masuk (Stock IN) : ", blockRegexes="-")
                        dbStockGudang.update({
                            f"item-{value[0]}" : [
                                value[0],
                                value[1],
                                value[2],
                                value[3],
                                value[4] + transaksiIn,
                                value[5],
                                value[3] + transaksiIn + value[4] - value[5],
                                dt.date.today().strftime("%d-%m-%Y")
                            ]
                        })
                        transaksi()
                    elif yakinTransaksi == "no":
                        transaksi()
                        break
                elif i == len(dbStockGudang) - 1:
                    print(f"*** ({barangTransaksiIn}) tidak dapat ditemukan ***")

        # Pilihan Menjalankan Menu Mengurangi jumlah barang di gudang (Update)
        elif menuTransaksi == 2:
            barangTransaksiOut = pypi.inputStr(prompt="\nMasukan nama barang yang ingin di dikurangi stocknya : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            for i, value in enumerate(dbStockGudang.values()):
                if barangTransaksiOut in value:
                    print("----- Informasi Barang Yang Akan Dilakukan Transaksi (Stock OUT) -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTanggal\t\t : {value[7]}""")
                    print("-" * 70)
                    yakinTransaksi = pypi.inputYesNo("Apakah anda yakin ingin melakukan transaksi barang diatas? (YES/NO) : ")
                    if yakinTransaksi == "yes":
                        transaksiOut = pypi.inputNum(prompt="Jumlah barang keluar (Stock OUT) : ", blockRegexes="-")
                        if transaksiOut + value[5] <= value[3] + value[4] :
                            dbStockGudang.update({
                                f"item-{value[0]}" : [
                                    value[0],
                                    value[1],
                                    value[2],
                                    value[3],
                                    value[4],
                                    value[5] + transaksiOut,
                                    value[3] + value[4] - transaksiOut - value[5],
                                    dt.date.today().strftime("%d-%m-%Y")
                                ]
                            })
                            transaksi()
                        else:
                            print(f"*** Jumlah stock barang tidak mencukupi ***\n*** Total stock {barangTransaksiOut} : {value[6]} ***")
                            transaksi()
                    elif yakinTransaksi == "no":
                        transaksi()
                        break
                elif i == len(dbStockGudang) - 1:
                    print(f"*** ({barangTransaksiOut}) tidak dapat ditemukan ***")

        # Pilihan Menjalankan Menu Menampilkan semua data stock di gudang (Read)
        elif menuTransaksi == 3:
            show(dbStockGudang)

        # Pilihan Menu Menjalankan Kembali ke menu utama
        elif menuTransaksi == 4:
            main()


# Fungsi menjalankan menu nomor 4 Menghapus Barang Lama Gudang (Delete, Read)
def delete():
    print("\n*** Menu ini akan satu data secara keseluruhan ***")
    while True:
        menuDelete = pypi.inputInt("""\n
----------Menu Menambahkan Stock Gudang----------
        
    Pilihan menu menambahkan stock gudang : 
    1. Hapus data stock di gudang
    2. Menampilkan semua data stock di gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        # Pilihan Menjalankan Menu Hapus Data Stock Gudang 
        if menuDelete == 1:
            show(dbStockGudang)
            noDelete = pypi.inputNum("\nMasukan nomor barang yang ingin dihapus keseluruhan : ")
            for i, value in enumerate(dbStockGudang.values()):
                if noDelete in value:
                    print("----- Info Barang Yang Akan dihapus -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTanggal\t\t : {value[7]}""")
                    print("-" * 35)
                    yakinDelete = pypi.inputYesNo(prompt="Apakah anda yakin akan menghapus data diatas? (YES/NO) : ")
                    if yakinDelete == "yes":
                        del dbStockGudang[f"item-{noDelete}"]
                        for key, value in dbStockGudang.copy().items():
                            if key != "column" and value[0] > noDelete:
                                del dbStockGudang[key]
                                dbStockGudang.update({
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
                elif i == len(dbStockGudang) - 1:
                    print(f"***Index ({noDelete}) tidak dapat ditemukan***")
                    delete()
        
        # Pilihan Menjalankan Menu Menampilkan semua data stock di gudang
        elif menuDelete == 2 :
            show(dbStockGudang) 

        # Pilihan Menjalankan Menu Kembali Ke Menu Utama       
        elif menuDelete == 3 :
            main()


# Fungsi menjalankan menu nomor 5 Settings (Create, Read, Update, Delete)
def settings():
    while True:
        menuSettings = pypi.inputInt("""\n
---------- Menu Settings Data Stock Gudang ----------
        
    Pilihan menu settings data stock gudang : 
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

# Fungsi menjalankan menu nomor 5.1 Setting Petugas Gudang (Create, Read, Update, Delete)
def settingPetugasGudang():
    while True:
        settingPetugas = pypi.inputInt("""\n
---------- Menu Settings Petugas Gudang ----------
        
    Pilihan menu settings petugas gudang : 
    1. Menampilkan Daftar Nama Petugas Gudang
    2. Mengedit Nama Petugas Gudang
    3. Menambah Petugas Gudang Baru
    4. Menghapus Petugas Gudang Lama
    5. Kembali Ke Menu Settings
    6. Kembali Ke Menu Utama
    
    Masukan Nomor Pilihan (1-6) : """, lessThan=7)
        
        # Pilihan Menampilkan Petugas Gudang (Read)
        if settingPetugas == 1:
            print("\nDaftar nama Petugas Gudang Terdaftar : ")
            for i in range(len(listPetugasGudang)):
                print(f"Petugas-{i+1} : {listPetugasGudang[i]}")
            settingPetugasGudang()

        # Pilihan Mengedit Nama Petugas Gudang (Update)
        elif settingPetugas == 2:
            print("\nNama Petugas Gudang Terdaftar : ")
            for i in range(len(listPetugasGudang)):
                print(f"Petugas-{i+1} : {listPetugasGudang[i]}")
            noEditPetugas = pypi.inputInt(prompt="No petugas yang ingin diedit : ", lessThan=len(listPetugasGudang)+1)
            namaPetugasEdit = pypi.inputStr(prompt="Masukan nama petugas baru : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            yakinEditPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin merubah {listPetugasGudang[noEditPetugas-1]} menjadi {namaPetugasEdit} ? (YES/NO) : ")
            if yakinEditPetugas == "yes":
                listPetugasGudang[noEditPetugas-1] = namaPetugasEdit
                settingPetugasGudang()
            elif yakinEditPetugas == "no":
                settingPetugasGudang()

        # Pilihan Menambah Petugas Baru (Create)
        elif settingPetugas == 3:
            nambahPetugas = pypi.inputStr(prompt="Masukan nama petugas gudang baru : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            if nambahPetugas in listPetugasGudang:
                print(f"*** Nama petugas {nambahPetugas} sudah ada dalam database ***")
                settingPetugasGudang()
            elif nambahPetugas not in listPetugasGudang:
                yakinTambahPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin menambah {nambahPetugas} kedalam database gudang ? (YES/NO) : ")
                if yakinTambahPetugas == "yes":
                    listPetugasGudang.append(nambahPetugas)
                    settingPetugasGudang()
                elif yakinTambahPetugas == "no":
                    settingPetugasGudang()

        # Pilihan Menghapus Petugas Gudang Lama (Delete)
        elif settingPetugas == 4:
            print("\nNama Petugas Gudang Terdaftar : ")
            for i in range(len(listPetugasGudang)):
                print(f"Petugas-{i+1} : {listPetugasGudang[i]}")
            hapusPetugas = pypi.inputStr(prompt="Masukan nama petugas yang ingin dihapus : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
            if hapusPetugas in listPetugasGudang:
                yakinHapusPetugas = pypi.inputYesNo(prompt=f"Apakah anda yakin menghapus {hapusPetugas} dari database gudang ? (YES/NO) : ")
                if yakinHapusPetugas == "yes":
                    listPetugasGudang.remove(hapusPetugas)
                    settingPetugasGudang()
                elif yakinHapusPetugas == "no":
                    settingPetugasGudang()
            elif hapusPetugas not in listPetugasGudang:
                print(f"*** Nama petugas {hapusPetugas} tidak ada dalam database ***")

        # Pilihan Kembali Ke Menu Settings
        elif settingPetugas == 5:
            settings()
        
        # Pilihan Untuk Langsung Kembali Ke Menu Utama
        elif settingPetugas == 6:
            main()
    
# Fungsi menjalankan menu nomor 5.2 Setting Basis Kode Barang (Create, Read, Update, Delete)
def settingBasisKodeBarang():
    while True:
        settingKode = pypi.inputInt("""\n
---------- Menu Settings Basis Kode Barang ----------
        
    Pilihan menu settings basis kode barang : 
    1. Menampilkan List Basis Kode Barang
    2. Mengedit Basis Kode Barang
    3. Menambah Basis Kode Barang
    4. Menghapus Basis Kode Barang Lama
    5. Kembali Ke Menu Settings
    6. Kembali Ke Menu Utama
    
    Masukan Nomor Pilihan (1-6) : """, lessThan=7)
        
        # Pilihan Menampilkan Basis Kode Barang Tersedia (Read)
        if settingKode == 1:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            settingBasisKodeBarang()

        # Pilihan Mengedit Basis Kode Barang Tersedia (Update)
        elif settingKode == 2:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            noEditBasisKode = pypi.inputInt(prompt="No basis kode yang ingin diedit : ", lessThan=len(listKodeBarang)+1)
            print(f"""- Format basis kode berjumlah 4 karakter dengan diakhiri dengan tanda strip "-"\n   Contoh : {listKodeBarang}""")
            namaBasisKodeEdit = pypi.inputStr(prompt="Masukan nama basis kode baru : ", applyFunc=lambda x: x.upper(), blockRegexes=[r"[0-9]"])
            if len(namaBasisKodeEdit) == 4 and namaBasisKodeEdit[3] == "-":
                yakinEditBasisKode = pypi.inputYesNo(prompt=f"Apakah anda yakin merubah basis kode {listKodeBarang[noEditBasisKode-1]} menjadi {namaBasisKodeEdit} ? (YES/NO) : ")
                if yakinEditBasisKode == "yes":
                    listKodeBarang[noEditBasisKode-1] = namaBasisKodeEdit
                    settingBasisKodeBarang()
                elif yakinEditBasisKode == "no":
                    settingBasisKodeBarang()
            else:
                print(f"*** Basis kode ({namaBasisKodeEdit}) tidak sesuai dengan format ***")

        # Pilihan Menambah Basis Kode Barang Baru (Create)
        elif settingKode == 3:
            print(f"""- Format basis kode berjumlah 4 karakter dengan diakhiri dengan tanda strip "-"\n   Contoh : {listKodeBarang}""")
            nambahBasisKode= pypi.inputStr(prompt="Masukan nama basis kode baru : ", applyFunc=lambda x: x.upper(), blockRegexes=[r"[0-9]"])
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

        # Pilihan Menghapus Basis Kode Barang Lama (Delete)
        elif settingKode == 4:
            print("\nNama Basis Kode Barang Terdaftar : ")
            for i in range(len(listKodeBarang)):
                print(f"KodeBarang-{i+1} : {listKodeBarang[i]}")
            hapusBasisKode = pypi.inputStr(prompt="Masukan nama basis kode yang ingin dihapus : ", applyFunc=lambda x: x.upper(), blockRegexes=[r"[0-9]"])
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


# Fungsi menampilkan Menu Utama
def main():
    while True:
        print(
            """
==================================================
-----Selamat Datang di Aplikasi Gudang PT.XYZ-----

        Pilihan Menu :
        1. Report Stock Gudang
        2. Menambah Barang Baru Di Data Stock Gudang
        3. Transaksi Stock Gudang
        4. Menghapus Barang Lama Di Data Stock Gudang
        5. Settings
        6. Exit
    """
    )
        menuNumber = pypi.inputInt(prompt="Masukan Nomor Pilihan (1-6): ",lessThan=7)

        # Pilihan Menjalankan menu Report Stock Gudang
        if menuNumber == 1:
            report()
        
        # Pilihan Menjalankan menu Menambah Barang Baru Di Data Stock Gudang
        elif menuNumber == 2:
            add()
        
        # Pilihan Menjalankan menu Transaksi Stock Gudang
        elif menuNumber == 3:
            transaksi()
        
        # Pilihan Menjalankan menu Menghapus Barang Lama Di Data Stock Gudang
        elif menuNumber == 4:
            delete()
        
        # Pilihan Mennjalankan Menu Settings
        elif menuNumber == 5:
            settings()
        
        # Pilihan Exit Dari Program
        elif menuNumber == 6:
            print("\n~~~~Terimakasih~~~~\nProgram made by : fathurizkym")

            for key, value in dbStockGudang.copy().items():
                if key != "column":    
                    dbStockGudang.update({
                        f"item-{value[0]}" : [
                            value[0],
                            value[1],
                            value[2],
                            value[6],
                            0,
                            0,
                            value[6],
                            value[7],
                        ]
                    })

            # Export Database Stock Gudang Ke File CSV
            fileStockGudang = open(pathStockGudang, "w", newline="")
            writerStockGudang = csv.writer(fileStockGudang, delimiter=";")
            writerStockGudang.writerows(dbStockGudang.values())
            fileStockGudang.close()

            # Export Database Petugas Gudang Ke File CSV
            with open("D:\Purwadhika JCDS\Capstone Project\Modul 1\data_petugas_gudang.csv", "w", newline="") as exportPetugasGudang:
                writerPetugasGudang = csv.writer(exportPetugasGudang)
                writerPetugasGudang.writerow(listPetugasGudang)
            
            # Export Database Petugas Gudang Ke File CSV
            with open("D:\Purwadhika JCDS\Capstone Project\Modul 1\data_basis_kode_barang.csv", "w", newline="") as exportBasisKode:
                writerBasisKode = csv.writer(exportBasisKode)
                writerBasisKode.writerow(listKodeBarang)
            
            sys.exit()

if __name__ == "__main__":
    # Import Database Stock Gudang Dari File CSV
    pathStockGudang = "D:\Purwadhika JCDS\Capstone Project\Modul 1\data_stock_gudang.csv"

    fileStockGudang = open(pathStockGudang)
    readerStockGudang = csv.reader(fileStockGudang, delimiter=";")
    headingsStockGudang = next(readerStockGudang)

    dbStockGudang = {"column": headingsStockGudang}
    for row in readerStockGudang:
        dbStockGudang.update(
            {
                str(f"item-{row[0]}") : [
                    int(row[0]),
                    str(row[1]),
                    str(row[2]),
                    int(row[3]),
                    int(row[4]),
                    int(row[5]),
                    int(row[6]),
                    str(row[7]),
                ]
            }
        )

    # Import Database Petugas Gudang Dari File CSV
    with open("D:\Purwadhika JCDS\Capstone Project\Modul 1\data_petugas_gudang.csv", "r") as importPetugasGudang:
        readerPetugasGudang = csv.reader(importPetugasGudang, delimiter=",")
        for listPetugasGudang in readerPetugasGudang:
            listPetugasGudang

    # Import Database Basis Kode Barang Dari File CSV
    with open("D:\Purwadhika JCDS\Capstone Project\Modul 1\data_basis_kode_barang.csv", "r") as importBasisKode:
        readerBasisKode = csv.reader(importBasisKode, delimiter=",")
        for listKodeBarang in readerBasisKode:
            listKodeBarang

    # Menjalankan Program
    while True:
        inputPtgs = pypi.inputStr(prompt="\nMasukan Nama Petugas Jaga : ", applyFunc=lambda x: x.title(), blockRegexes=[r"[0-9]"])
        if inputPtgs in listPetugasGudang:
            print(f"\nLogin sukses\nNama petugas gudang : {inputPtgs}")
            heading(inputPtgs)
            main()
            break
        else:
            print(f"*** Nama anda ({inputPtgs}) tidak ada dalam database petugas gudang kami ***")
            print(f"*** Silahkan minta izin ke pengawas gudang kami ***")