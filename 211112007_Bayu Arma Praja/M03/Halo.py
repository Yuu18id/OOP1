class Halo:
    def __init__(self, angka):
        self.a = 123
        self._b = 20
        self.__c = 40

halo = Halo("angka")
print(halo.a)
print(halo._b)
print(halo._Halo__c)