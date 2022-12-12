class Ecomm:


    def __init__(self, namaBarang, jenisBarang, hargaBarang, jumlahBarang):
        self.namaBarang = namaBarang
        self.jenisBarang = jenisBarang
        self.hargaBarang = hargaBarang
        self.jumlahBarang = jumlahBarang

    def cekBarang(self):
        if (self.jumlahBarang > 1):
            print(f"Stok {self.namaBarang} masih banyak")
        elif (self.jumlahBarang < 5):
            print(f"Stok {self.namaBarang} hampir habis!")
        else:
            print(f"Stok {self.namaBarang} habis!")

    def cetakBarang(self):
        print(f"Nama Barang : {self.namaBarang}")
        print(f"Jenis Barang : {self.jenisBarang}")
        print(f"Harga Barang : {self.hargaBarang}")
        print(f"Jumlah Barang : {self.jumlahBarang}")

    def pengeluaran(self):
        print(f"Pengeluaran: {self.hargaBarang * self.jumlahBarang}")
        

barang1 = Ecomm("Jeruk", "Buah-Buahan", 4000, 18)
barang2 = Ecomm("Satanizer", "Hand Sanitizer", 15000, 0)
barang3 = Ecomm("Semangka", "Buah-Buahan", 5000, 1)
barang1.cetakBarang()
barang1.cekBarang()
barang1.pengeluaran()
print("\n")
barang2.cetakBarang()
barang2.cekBarang()
barang2.pengeluaran()
print("\n")
barang3.cetakBarang()
barang3.cekBarang()
barang3.pengeluaran()