from abc import ABC, abstractmethod

class Absensi(ABC):
    @abstractmethod
    def cetak():
        pass
    
    def banyak():
        pass

class Mahasiswa(Absensi):

    def __init__(self, nim, nama , prodi, kelamin, noHp, jabatan):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelamin = kelamin
        self.noHp = noHp
        self.jabatan = jabatan
        self.banyak = 1
    
    
    def cetak(self):
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print(f"Jenis Kelamin : {self.kelamin}")
        print(f"No HP : {self.noHp}")
        print(f"Status : {self.jabatan}")
        

    def banyak(self):
        print(f"Banyak Mahasiswa : {self.banyak}")
    
class Dosen(Absensi):

    def __init__(self, nim, nama, prodi, kelamin, noHp, jabatan):
        self.nim = nim
        self.nama = nama
        self.prodi = prodi
        self.kelamin = kelamin
        self.noHp = noHp
        self.jabatan = jabatan
        self.banyak = 1

    def cetak(self):
        print(f"NIP : {self.nim}")
        print(f"Nama : {self.nama}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Jenis Kelamin : {self.kelamin}")
        print(f"No HP : {self.noHp}")

    def banyak(self):
        print(f"Banyak Dosen : {self.banyak}")

if __name__ == "__main__":
    mhs = Mahasiswa("Bayu Arma Praja", "211112007", "Teknik Informatika", "Laki-Laki", "0895414329151", "Mahasiswa")
    for data in Absensi.__subclasses__():
        data.cetak(mhs)
        data.banyak(mhs)
        print("\n")
    dosen = Dosen("12345", "Budi", "Teknik Informatika", "Laki-Laki", "082361539864", "Dosen")
    for data in Absensi.__subclasses__():
        data.cetak(dosen)
        data.banyak(dosen)
        print("\n")
