class Dosen:
    def __init__(self, nomorInduk, nama, jenisKelamin, noHp):
        self.nomorInduk = nomorInduk
        self.nama = nama
        self.jenisKelamin = jenisKelamin
        self.noHp = noHp
        
    def perkenalan(self):
        print('Perkenalan Dosen')
        print(f'Nama   : {self.nama}')
        print(f'No. HP : {self.noHp}')
        print('\n')
    

class Mahasiswa(Dosen):
    def __init__(self, nomorInduk, nama, jenisKelamin, noHp, kelas):
        super().__init__(nomorInduk, nama, jenisKelamin, noHp)
        self.kelas = kelas

    def cekAbsensi(self):
        print('Absensi Mahasiswa')
        print(f'Nomor Induk : {self.nomorInduk}')
        print(f'Nama        : {self.nama}')
        print('\n')

mhs1 = Mahasiswa('211112007', 'Bayu Arma Praja', 'Laki-Laki', '0895414329151', 'IF-C Pagi')
dsn1 = Dosen('098761223', 'Budi Setiawan', 'Laki-Laki', '086969696969')

mhs1.cekAbsensi()
dsn1.perkenalan()
