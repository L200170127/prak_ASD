from tugas2 import manusia
class mahasiswa(manusia):
    """ class mahsiswa yang dibangun dari class manusia """
    def __init__(self,nama,nim,kota,us):
        self.nama=nama
        self.nim=nim
        self.kota=kota
        self.us=us
    def __str__(self):
        s=self.nama+',NIM '+str(self.nim)\
           +'. tinggal di '+self.kota\
           +'. uang saku Rp '+str(self.uang)\
           +'. tiap bulan'
        return s
    def ambilin(self):
        return self.nama
    def ambilnim(self):
        return self.nim
    def ambiluang(self):
        return self.uang
    def makan(self,s):
        print ("Saya makan",s)
        self.keadaan='kenyang'
    def pkota(self):
        return self.kota
    def perbarui(self,x):
        self.kota=x
    def tambah(self,x):
        self.uang=self.uang+x
