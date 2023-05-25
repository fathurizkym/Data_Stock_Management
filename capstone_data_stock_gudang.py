# Nama : Fathur Rizky Maulana
# Capstone Project Modul 1 - Data Stock Gudang
# Data stock Gudang dengan features : Kode Barang, Nama Barang, Stock Awal, Stock In, Stock Out, Stock Akhir, Transaction Date

import sys
import datetime as dt

# Fungsi menampilkan tanggal sekarang dan petugas gudang
def heading(nama):
    print("=" * 50)
    print(f"\nTanggal : {dt.date.today()} \nPetugas Gudang : {nama}")

# Fungsi untuk merapihkan format tabel dictStockGdg
def printFormat(dictFormat):
    for key, value in dictFormat.items():
        if key == "column":
            print(f"| {dictFormat[key][0]}\t | {dictFormat[key][1]} \t | {dictFormat[key][2]} \t | {dictFormat[key][3]}\t | {dictFormat[key][4]}\t | {dictFormat[key][5]}\t | {dictFormat[key][6]}\t | {dictFormat[key][7]} | ")
        else:
            print(f"| {dictFormat[key][0]}\t | {dictFormat[key][1]} \t | {dictFormat[key][2]} \t | {dictFormat[key][3]}\t\t | {dictFormat[key][4]}\t\t | {dictFormat[key][5]}\t\t | {dictFormat[key][6]}\t\t | {dictFormat[key][7]}\t    | ")

# Fungsi menampilkan update stock gudang 
def show(Dict):
    heading(inputPtgs)
    print("\nUpdate Laporan Stock Barang PT. XYZ\n")
    printFormat(Dict)

# Fungsi menampilkan menu nomor 1 Report Stock Gudang (Read)
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

        menuReportGdg = int(input("Masukan Nomor Pilihan (1-3) : "))
        if menuReportGdg == 1:
            show(dictStockGdg)
        elif menuReportGdg == 2:
            showDataUnique()
        elif menuReportGdg == 3:
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")
            continue

# Fungsi menampilkan menu nomor 1.2 menampilkan data tertentu di gudang
def showDataUnique():
    inputNamaBarang = input("Masukan Nama Barang Yang Dicari : ").title()
    for i, value in enumerate(dictStockGdg.values()):
        if inputNamaBarang in value:
            print("-----Info Barang Yang Dicari-----")
            print(f"""Index\t\t : {value[0]}\nKode Barang\t : {value[1]}\nNama Barang\t : {value[2]}\nStock Awal\t : {value[3]}\nStock In\t : {value[4]}\nStock Out\t : {value[5]}\nStock Akhir\t : {value[6]}\nTransaction Date : {value[7]}""")
            break
        elif i == len(dictStockGdg) - 1:
            print(f"***Barang {inputNamaBarang} tidak dapat ditemukan***")
            report()
        
# Fungsi menampilkan menu nomor 2
def add():
    heading(inputPtgs)
    while True:
        menuAdd = int(input("""
----------Menu Menambahkan Stock Gudang----------
        
    Pilihan menu menambahkan stock gudang : 
    1. Tambah data stock di gudang
    2. Menampilkan semua data stock di gudang
    3. Kembali ke menu utama
    
    Masukan Nomor Pilihan (1-3) : """))
        
        if menuAdd == 1:
            # show(dictStockGdg)
            addBarang = input("Masukan nama barang yang ingin ditambahkan : ").title()
            for i, value in enumerate(dictStockGdg.copy().values()):
                if addBarang in value:
                    print(f"***{addBarang} sudah ada di dalam database***")
                    add()
                    break
                elif i == len(dictStockGdg) - 1:
                    print("Silahkan input barang yang ingin dimasukan")
                    kodeBarang = input("Kode Barang  : ").upper()
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
            show(dictStockGdg)        
        elif menuAdd == 3 :
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")
            
# Fungsi menampilkan menu nomor 3
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
            show(dictStockGdg)

        elif menuTransaksi == 4:
            main()

        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")

# Fungsi Menampilkan menu nomor 4
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
            show(dictStockGdg)        
        elif menuAdd == 3 :
            main()
        else:
            print("***Nomor menu yang dipilih tidak sesuai***\n***Masukan nomor sesuai yang tertera diatas***")

# Fungsi menampilkan menu utama
def main():
    while True:
        print(
            """
==================================================
-----Selamat Datang di Aplikasi Gudang PT.XYZ-----

        Pilihan Menu :
        1. Report stock gudang
        2. Menambah Stock Baru Gudang
        3. Transaksi Stock Gudang
        4. Menghapus stock Gudang
        5. Exit
    """
    )
        menuNumber = int(input("Masukan Nomor Pilihan (1-5): "))
        if menuNumber == 1:
            report()
        elif menuNumber == 2:
            add()
        elif menuNumber == 3:
            transaction()
        elif menuNumber == 4:
            delete()
        elif menuNumber == 5:
            print("\n~~~Terimakasih~~~\nProgram made by : fathurizkym")
            sys.exit()
        else:
            print("Nomor menu yang dipilih tidak sesuai.\nMasukan nomor sesuai yang tertera diatas")

if __name__ == "__main__":
    # Dictionary stock Gudang
    dictStockGdg = {
        "column" : ["Index", "Kode Barang", "Nama Barang", "Stock Awal", "Stock In", "Stock Out", "Stock Akhir", "Transaction Date"],
        "item-0" : [0, "FRM-0", "Barang A", 10, 0, 0, 10, dt.date(2023,1,1).strftime("%d-%m-%Y")],
        "item-1" : [1, "FRM-1", "Barang B", 20, 0, 0, 20, dt.date(2023,1,2).strftime("%d-%m-%Y")],
        "item-2" : [2, "FRM-2", "Barang C", 15, 0, 0, 15, dt.date(2023,1,3).strftime("%d-%m-%Y")],
    }
 
    inputPtgs = input("Masukan Nama Petugas Jaga : ").title()

    # Menjalankan Program Data Stock Gudang
    main()
