class Bayu:
    
    def __init__(self):
        self.dataMhs = {'nim' : ['211112007', '211115435', '3443224'], 'nama':['Bayu', 'Bagas', 'Budi'], 'jurusan' : ['TI', 'IF', 'AK'], 'semester' : ['3', '3', '5']}
        self.dataDosen = {'nip' : ['1234567', '22345678', '36653467'], 'nama':['Arya', 'Beti', 'Rizal'], 'jabatan' : ['Dosen Tetap', 'Dosen Honorer', 'Dekan'], 'jkelamin' : ['Laki-Laki', 'Perempuan', 'Laki-Laki'], 'noHp': ['0899', '0812', '0853']}
        
    def cetakMhs(self):
        for i in range(len(self.dataMhs['nim'])):
            print('NIM : ',self.dataMhs['nim'][i])
            print('Nama : ', self.dataMhs['nama'][i])
            print('Jurusan : ', self.dataMhs['jurusan'][i])
            print('Semester : ', self.dataMhs['semester'][i])
            print('\n')
        
    def cetakDosen(self):
        for i in range(len(self.dataDosen['nip'])):
            print('NIP : ',self.dataDosen['nip'][i])
            print('Nama : ', self.dataDosen['nama'][i])
            print('Jabatan : ', self.dataDosen['jabatan'][i])
            print('Jenis Kelamin : ', self.dataDosen['jkelamin'][i])
            print('No. HP : ', self.dataDosen['noHp'][i])
            print('\n')
        
    def banyak(self):
        print(len(self.dataMhs['nim']) + len(self.dataDosen['nip']))
        
    def pencarian(self):
        for i in range(len(self.dataMhs['nim'])):
            if(self.dataMhs['nim'][i] == self.nama):
                return i
        return -1
        
class Cari(Bayu):
    
    def __init__(self, nama):
        self.nama = nama
            
	
if __name__ == '__main__':
    kelas = Bayu()
    
    kelas.cetakMhs()
    kelas.cetakDosen()
    print('Banyak Pengunjung : ')
    kelas.banyak()
    
    
