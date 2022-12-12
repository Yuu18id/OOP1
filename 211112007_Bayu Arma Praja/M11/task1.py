class KelasA:
    
    def nama(self):
        print('Kelas A')
    
    def ruang(self):
        print('T1/L2')
    
    def dosen(self):
        print('Dosen yang mengajarkan mengenai perhitungan kalkulus beserta proses yang ada')
        
class KelasB:
    
    def nama(self):
        print('Kelas B')
    
    def ruang(self):
        print('T3/L2')
    
    def dosen(self):
        print('Dosen yang mengajarkan pemrograman beserta proses-proses dalam pemrograman')
        
class KelasC:
    
    def nama(self):
        print('Kelas C')
    
    def ruang(self):
        print('T5/L2')
    
    def dosen(self):
        print('Dosen yang mengajarkan Bahasa Inggris lengkap dengan formula-formula untuk pembuatan kata-kata')
        
class Resepsionis:
    
    def __init__(self):
        self.kelasA = KelasA()
        self.kelasB = KelasB()
        self.kelasC = KelasC()
        
    def prosesAbsensi(self):
        self.kelasA.nama()
        self.kelasA.ruang()
        self.kelasA.dosen()
        print('\n')
        self.kelasB.nama()
        self.kelasB.ruang()
        self.kelasB.dosen()
        print('\n')
        self.kelasC.nama()
        self.kelasC.ruang()
        self.kelasC.dosen()
        
if __name__ == "__main__":
    absen = Resepsionis()
    absen.prosesAbsensi()