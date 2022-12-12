class Mahasiswa:
    def __init__(self, nim, nama, nohp):
        self.nim = nim
        self.nama = nama
        self.nohp = nohp
        self.mhs = {}

    def inputData(self):
        ni = ''
        nm = ''
        hp = ''
        cek = True
        while cek:
            nim = yield ni
            if (self.mhs < 1):
                cek = False
            else:
                cek = False
                for i in range(len(self.mhs)):
                    if(self.mhs[i]['nim'] == nim):
                        cek = True
                    if(cek):
                        print('Nim sudah terdaftar !')
                        print('Masukkan Nim lagi !')
        nama = yield nm
        nohp = yield hp
        tmp = {'nim' : nim, 'nama' : nama, 'noHp' : nohp}
        self.mhs.append(tmp)

    def inputtt(self):
        tmp = {'nim' : self.nim, 'nama' : self.nama, 'noHp' : self.nohp}
        self.mhs.append(tmp)
        print(self.mhs)

a = Mahasiswa('1', 'bayu', '0899')
a.inputtt

