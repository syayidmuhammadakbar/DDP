class gempa:
    keadaan='info gempa terkini'

#konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi=lokasi
        self.skala=skala
#method
    def dampak(self,skala_dampak):
       
       self.skala=skala_dampak 
       if skala_dampak < 2:
           print("tidak terasa gempa")
       elif skala_dampak >2 :
           print("dampak gempa bangunan roboh")
       elif skala_dampak >4 :
           print("dampak gempa bangunan roboh")
       elif skala_dampak >6 :
           print("dampak gempa bangunan roboh dan berpotensi tsunami")
       else:
           print("masukan skala dengan format yang benar")
       
    
    def cetak(self,):
        print(gempa.keadaan,
            "\n====================",
            '\n lokasi\t:',self.lokasi,
            '\n kekuatan gempa\t:',self.skala,
            '\n Dampak yang dihasilkan\t:',self.skala,
            )
        
