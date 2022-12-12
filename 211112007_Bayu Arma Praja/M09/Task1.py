class Mahasiswa:
    banyakmhs = 0

    def __init__(self, nama, nim, prodi):
        self._nama = nama
        self._nim = nim
        self._prodi = prodi
        self.banyakmhs += 1
        #self._data = [{'nama':'Bayu Arma Praja', 'nim':'211112007', 'prodi':'Teknik Informatika'}, 
        #             {'nama':'Bayu Arma Praja', 'nim':'211112007', 'prodi':'Teknik Informatika'}, 
        #             {'nama':'Bayu Arma Praja', 'nim':'211112007', 'prodi':'Teknik Informatika'}]

    def cetakAbsen(self):
        #print('Banyak Pengunjung : ' , i+1)
        hasil = (f"Nama : {self._nama}\n")
        hasil += (f"NIM : {self._nim}\n")
        hasil += (f"Prodi : {self._prodi}\n")
        return hasil



class Absensi(Mahasiswa):

    def __init__(self, proses):
        self._proses = proses
        
    def cetakAbsen(self):
        hasil = self._proses.cetak()
        hasil += f'Jumlah Pengunjung : {self.banyakmhs}'
        
if __name__ == '__main__':
    mhs1 = Mahasiswa('Bayu','211112007', 'Teknik Informatika')
    cekJumlah = Absensi(mhs1)
    
    print(mhs1.cetakAbsen())
    print('Jumlah Pengunjung : ', cekJumlah.cetakAbsen())
    
#a = Mahasiswa('','','')
#a.cetakAbsen()