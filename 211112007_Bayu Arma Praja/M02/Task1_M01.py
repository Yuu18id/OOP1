class Mahasiswa:
    banyakMahasiswa = 0

    def __init__(self, nama, nim, prodi, kelamin, noHpMhs):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kelamin = kelamin
        self.noHpMhs = noHpMhs
        self.banyakMahasiswa += 1

    def cetakMhs(self):
        print(f"Nama : {self.nama}")
        print(f"NIM : {self.nim}")
        print(f"Prodi : {self.prodi}")
        print(f"Jenis Kelamin : {self.kelamin}")
        print(f"No HP : {self.noHpMhs}")

    def banyakMhs(self):
        print(f"Banyak Mahasiswa : {self.banyakMahasiswa}")

mhs = Mahasiswa("Bayu Arma Praja", "211112007", "Teknik Informatika", "Laki-Laki", "0895414329151")
mhs.cetakMhs()
mhs.banyakMhs()

print("\n")
class Dosen:
    banyakDosen1 = 0

    def __init__(self, nip, nama, jabatan, kelamin, noHp):
        self.nip = nip
        self.nama = nama
        self.jabatan = jabatan
        self.kelamin = kelamin
        self.noHp = noHp
        self.banyakDosen1 += 1

    def cetakDosen(self):
        print(f"NIP : {self.nip}")
        print(f"Nama : {self.nama}")
        print(f"Jabatan : {self.jabatan}")
        print(f"Jenis Kelamin : {self.kelamin}")
        print(f"No HP : {self.noHp}")

    def banyakDosen(self):
        print(f"Banyak Dosen : {self.banyakDosen1}")
    
dosen = Dosen("12345", "Budi", "Dosen", "Laki-Laki", "082361539864")
dosen.cetakDosen()
dosen.banyakDosen()
print("\n")
print(f"Total Pengunjung : {mhs.banyakMahasiswa + dosen.banyakDosen1}")
