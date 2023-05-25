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
    heading()
    print("\nUpdate Laporan Stock Barang PT. XYZ\n")
    for value in Dict.values():
        print(printFormat.format("", *value))

# Fungsi menjalankan menu nomor 1 Report Stock Gudang (Read)
def report():
    heading(inputPtgs)
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
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")
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
    heading(inputPtgs)
    while True:
        menuAdd = pypi.inputInt(prompt="""
----------Menu Menambahkan Stock Gudang----------
        
    Pilihan menu menambahkan stock gudang : 
    1. Tambah data stock di gudang
    2. Menampilkan semua data stock di gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """, lessThan=4)
        
        if menuAdd == 1:
            # show(dictStockGdg)
            addBarang = pypi.inputStr(prompt="Masukan nama barang yang ingin ditambahkan : ", applyFunc=lambda x: x.title(), blockRegexes="0123456789")
            for i, value in enumerate(dictStockGdg.copy().values()):
                if addBarang in value:
                    print(f"***{addBarang} sudah ada di dalam database***")
                    add()
                    break
                elif i == len(dictStockGdg) - 1:
                    print("Silahkan input barang yang ingin dimasukan")
                    while True:
                        kodeBarang = input("Kode Barang  : ").upper()
                        if kodeBarang[0:4] in listKodeBarang:
                            continue
                        else:
                            gotoSettings = pypi.inputYesNo(prompt="Kode barang yang anda masukan belum terdaftar di sistem kami\nApakah anda tetap ingin menambah barang? (YES/NO) : ")
                            if gotoSettings == "Y":
                                settings()
                            else:
                                add()
                        break
                    print(f"Nama Barang  : {addBarang}")
                    stockAdd   = input("Stock Barang : ")
                    yakin = input("Apakah anda yakin menambah data diatas? (Y/T) : ").upper()
                    if yakin == "Y":
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
                    elif yakin == "T":
                        add()
                    else :
                        print("Input yang anda masukan salah!!! Input (Y/T) ")
        elif menuAdd == 2 :
            show(dictStockGdg, printFormat)        
        elif menuAdd == 3 :
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")
            
# Fungsi menjalankan menu nomor 3 Transaksi stock gudang
def transaction():
    heading(inputPtgs)
    while True:
        menuTransaksi = int(input("""
----------Menu Transaksi Barang Stock Gudang----------
        
    Pilihan menu transaksi barang stock gudang : 
    1. Menambah jumlah barang di gudang
    2. Mengurangi jumlah barang di gudang
    3. Menampilkan semua data stock di gudang
    4. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-4) : """))
        
        if menuTransaksi == 1:
            barangTransaksiIn = input("\nMasukan nama barang yang ingin di ditambah stocknya : ").title()
            for i, value in enumerate(dictStockGdg.values()):
                if barangTransaksiIn in value:
                    print("----- Info Barang Yang Akan ditambah Stocknya -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinTransaksi = input("Apakah anda yakin ingin melakukan transaksi barang diatas? (Y/T) : ").upper()
                    if yakinTransaksi == "Y":
                        transaksiIn = int(input("Jumlah barang IN : "))
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
                    elif yakinTransaksi == "T":
                        transaction()
                    else:
                        print("***Input menu yang dipilih tidak sesuai***\n***Masukan pilihan (Y/T)!***")
                        break
                elif i == len(dictStockGdg) - 1:
                    print(f"***Barang tidak dapat ditemukan***")

        elif menuTransaksi == 2:
            barangTransaksiOut = input("\nMasukan nama barang yang ingin di dikurangi stocknya : ").title()
            for i, value in enumerate(dictStockGdg.values()):
                if barangTransaksiOut in value:
                    print("----- Info Barang Yang akan dikurangi Stocknya -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinTransaksi = input("Apakah anda yakin ingin melakukan transaksi barang diatas? (Y/T) : ").upper()
                    if yakinTransaksi == "Y":
                        transaksiOut = int(input("Jumlah barang out : "))
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
                    elif yakinTransaksi == "T":
                        transaction()
                    else:
                        print("***Input menu yang dipilih tidak sesuai***\n***Masukan pilihan (Y/T)!***")
                        break
                elif i == len(dictStockGdg) - 1:
                    print(f"***Barang tidak dapat ditemukan***")

        elif menuTransaksi == 3:
            show(dictStockGdg, printFormat)

        elif menuTransaksi == 4:
            main()

        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")

# Fungsi menjalankan menu nomor 4 Menghapus barang lama gudang
def delete():
    print("\n*** Menu ini akan satu data secara keseluruhan ***")
    while True:
        menuAdd = int(input("""
----------Menu Menambahkan Stock Gudang----------
        
    Pilihan menu menambahkan stock gudang : 
    1. Hapus data stock di gudang
    2. Menampilkan semua data stock di gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """))
        
        if menuAdd == 1:
            show(dictStockGdg)
            noDelete = int(input("\nMasukan nomor barang yang ingin dihapus satu baris : "))
            for i, value in enumerate(dictStockGdg.values()):
                if noDelete in value:
                    print("----- Info Barang Yang Akan dihapus -----")
                    print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
                    yakinDelete = input("Apakah anda yakin akan menghapus data diatas? (Y/T) : ").upper()
                    if yakinDelete == "Y":
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
                    elif yakinDelete == "T":
                        delete()
                    else :
                        print("Input yang anda masukan salah!!! Input (Y/T) ")
                        delete()
                    break
                elif i == len(dictStockGdg) - 1:
                    print(f"***{noDelete} tidak dapat ditemukan***")
                    delete()
        elif menuAdd == 2 :
            show(dictStockGdg, printFormat)        
        elif menuAdd == 3 :
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")

# Fungsi menjalankan menu nomor 5 Settings
def settings():
    print("Under Maintenance")

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
            prompt="Masukan Nomor Pilihan (1-5): ",
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

if __name__ == "__main__":
    # Dictionary stock Gudang
    dictStockGdg = {
        "column" : ["Index", "Kode Barang", "Nama Barang", "Stock Awal", "Stock In", "Stock Out", "Stock Akhir", "Date"],
        "item-0" : [0, "FRM-0", "Barang A", 10, 0, 0, 10, dt.date(2023,1,1).strftime("%d-%m-%Y")],
        "item-1" : [1, "FRM-1", "Barang B", 20, 0, 0, 20, dt.date(2023,1,2).strftime("%d-%m-%Y")],
        "item-2" : [2, "FRM-2", "Barang C", 15, 0, 0, 15, dt.date(2023,1,3).strftime("%d-%m-%Y")],
    }

    petugasGudang = [
        "Fathur Rizky Maulana", 
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

    printFormat = '{:<2}' + '{:<10}' * (len(dictStockGdg["column"]))

    while True:
        inputPtgs = pypi.inputStr(
            prompt="\nMasukan Nama Petugas Jaga : ",
            applyFunc=lambda x: x.title(),
            blockRegexes="0123456789")
       
        if inputPtgs in petugasGudang:
            print(f"\nLogin sukses\nNama petugas gudang : {inputPtgs}")
            main()
            break
        else:
            print(f"Nama anda ({inputPtgs}) tidak ada dalam database petugas gudang kami")
            print(f"Silahkan minta izin ke petugas gudang kami : \n{petugasGudang}")