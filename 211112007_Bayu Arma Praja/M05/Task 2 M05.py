class Ecomm:
    def __init__(self, nama, hargaBeli):
        self.nama = nama
        self.hargaBeli = hargaBeli

class Barang(Ecomm):
    def __init__(self, nama, jumlahAwal ,jumlahAkhir, hargaBeli, hargaJual, kategori):
        super().__init__(nama, hargaBeli)
        self.jumlahAwal = jumlahAwal
        self.jumlahAkhir = jumlahAkhir
        self.hargaJual = hargaJual
        self.kategori = kategori

    def cekBarang(self):
        if (self.jumlahAkhir > 1):
            print(f"Stok {self.nama} masih banyak")
            print('\n')
        elif (self.jumlahAkhir < 5):
            print(f"Stok {self.nama} hampir habis!")
            print('\n')
        else:
            print(f"Stok {self.nama} habis!")
            print('\n')

    def cetakInfo(self):
        print(f'Nama         : {self.nama}')
        print(f'Jumlah Awal  : {self.jumlahAwal}')
        print(f'Jumlah Akhir : {self.jumlahAkhir}')
        print(f'Harga Beli   : {self.hargaBeli}')
        print(f'Harga Jual   : {self.hargaJual}')
        print(f'Kategori     : {self.kategori}')
        print('\n')
        print('Laporan Bulanan')
        print(f'Keuntungan Bulan Ini  : {(self.jumlahAwal - self.jumlahAkhir) * self.hargaJual}')
        print(f'Pengeluaran Bulan Ini : {self.jumlahAwal * self.hargaBeli}')

barang1 = Barang('Hand Sanitizer', 100, 20, 9000, 10000, 'Kesehatan')
barang2 = Barang('Ban Mobil', 25, 4, 48000, 50000, 'Otomotif')
barang3 = Barang('Semangka', 50, 11, 4500, 5000, 'Buah-buahan')
barang4 = Barang('Botol Minuman Bayi', 15, 1, 19000, 20000, 'Peralatan Bayi')

barang1.cetakInfo()
barang1.cekBarang()
barang2.cetakInfo()
barang2.cekBarang()
barang3.cetakInfo()
barang3.cekBarang()
