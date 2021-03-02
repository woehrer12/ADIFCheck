import adif_io

class ADIF:
    qsos = ""
    header = ""
    # http://www.arrl.org/files/file/dxcclist.txt


    def read_ADIF(self, filename):
        ADIF.qsos, ADIF.header = adif_io.read_from_file(filename)
        #print("Pfad gelesen")
        #print("QSOs: {}\nADIF Header: {}".format(ADIF.qsos, ADIF.header))

    def getStat(self):
        print("Anzahl QSOs: " , len(ADIF.qsos))
        print(ADIF.qsos[0])
        print(type(ADIF.qsos[0]['QSO_DATE']))
        print(ADIF.qsos[0]['QSO_DATE']) 
    
    def getAnzahl(self):
        return len(ADIF.qsos) #Int

    def getAnzahlMode(self,Mode):
        i = 0
        x = 0
        for i in range(0, len(ADIF.qsos)):
            if ADIF.qsos[i]['MODE'] == Mode:
                print(ADIF.qsos[i])
                x = x + 1
        return x

    def searchDXCC(self, code):
        i = 0
        x = 0
        for i in range(0, len(ADIF.qsos)):
            if ADIF.qsos[i]['DXCC'] == code:
                print(ADIF.qsos[i])
                x = x + 1
        return x        

    def getanzahlDXCC(self,code):
        i = 0
        x = 0
        for i in range(0,550):
            if ADIF.qso[i]['DXCC'] == code:
                