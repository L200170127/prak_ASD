class manusia(object):
    """ clas manusia dengan inisiasi 'nama' """
    keadaan='lapar'
    def __init__(self,nama):
        self.nama=nama
    def ucap(self):
        print("Halo namaku: ",self.nama)
    def olah(self,k):
        print('Saya habis',k)
        self.keadaan='lapar'
    def makan(self,s):
        print("Saya baru saja makan ",s)
        self.keadaan='kenyang'
    def kali(self,n):
        return n*2
