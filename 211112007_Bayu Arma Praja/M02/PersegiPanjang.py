class persegiPanjang:
    def __init__(self, p , l):
        self.p = p
        self.l = l
    def luas(self):
        return self.p * self.l
    def keliling(self):
        print(f"Keliling = {2*(self.p+self.l)}")
    def hasil(self, p , l):
        print(f"Panjang = {p}")
        print(f"Lebar = {l}")
        print(f"Luas = {p*l}")
        print(f"Keliling = {2*(p+l)}")

a = persegiPanjang(10, 20)
print(f"Luas = {a.luas()}")
a.keliling()
a.hasil(15, 25)