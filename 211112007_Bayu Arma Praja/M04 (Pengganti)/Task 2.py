class Ecomm:

    def __init__(self, kode, nama, jumlah, jenis):
        self.kode = kode
        self.nama = nama
        self.jumlah = jumlah
        self.jenis = jenis
        self.data = [{'kode' : '001', 'nama' : 'Jeruk', 'jumlah' : '4', 'jenis' : 'Buah'}, 
        {'kode' : '018', 'nama' : 'Dot Bayi Dodo', 'jumlah' : '0', 'jenis' : 'Botol Minuman Bayi'}, 
        {'kode' : '086', 'nama' : 'Dettol', 'jumlah' : '27', 'jenis' : 'Hand Sanitizer'}, 
        {'kode' : '020', 'nama' : 'Ban Mobil', 'jumlah' : '15', 'jenis' : 'Ban Mobil'},]

    def cekBarang(self):
        for i in range(len(self.data)):
            if (self.data[i]['jumlah'] < 1):
                print(f'Stok barang {self.data[i]} hampir habis')
            else:
                print(f'Stok barang {self.data[i]} masih banyak')

    def cetakBarang(self):
        for i in range(len(self.data)):
            print(f"Barang ke-{i+1}")
            print(f"Kode Barang : {self.data[i]['kode']}")
            print(f"Nama Barang : {self.data[i]['nama']}")
            print(f"Jumlah Barang : {self.data[i]['jumlah']}")
            print(f"Jenis Barang : {self.data[i]['jenis']}")
            print()

    def urutBarang(self):
        self.data = sorted(self.data, key=lambda d: d['jenis'])
        for i in range(len(self.data)):
            print(f"Barang ke-{i+1}")
            print(f"Kode Barang : {self.data[i]['kode']}")
            print(f"Nama Barang : {self.data[i]['nama']}")
            print(f"Jumlah Barang : {self.data[i]['jumlah']}")
            print(f"Jenis Barang : {self.data[i]['jenis']}")
            print()

    def inputData(self, kode, nama, jumlah, jenis):
        tmp = {'kode' : kode, 'nama' : nama, 'jumlah' : jumlah, 'jenis' : jenis}
        self.data.append(tmp)

    def cariData(self, kode):
        
        for i in range(1)):
            print(f"Kode Barang : {self.data[i]['kode']}")
            print(f"Nama Barang : {self.data[i]['nama']}")
            print(f"Jumlah Barang : {self.data[i]['jumlah']}")
            print(f"Jenis Barang : {self.data[i]['jenis']}")
            print()


a = Ecomm('', '', '', '')

while True:
    print('ECOMMERCE')
    print('1. Cetak Barang')
    print('2. Urut Barang')
    print('3. Input Data')
    print('4. Cari Data')
    masuk = int(input())
    try:
        if (masuk == 1):
            a.cetakBarang()
        elif (masuk == 2):
            a.urutBarang()
        elif (masuk == 3):
            kode = input('Masukkan Kode Barang : ')
            nama = input('Masukkan Nama Barang : ')
            jumlah = input('Masukkan Jumlah Barang : ')
            jenis = input('Masukkan Jenis Barang : ')
            a.inputData(kode, nama, jumlah, jenis)
            print('Data Berhasil Ditambahkan!')
        elif (masuk == 4):
            cari = input('Masukkan Kode Barang yang Dicari : ')

        input()
    except:
        print('error')

    