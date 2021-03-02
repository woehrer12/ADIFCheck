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
                x = x + 1
        return x

    def searchDXCC(self, code): # Zählt die Anzahl eines bestimmten DXCC
        i = 0
        x = 0
        for i in range(0, len(ADIF.qsos)):
            if ADIF.qsos[i]['DXCC'] == code:
                x = x + 1
        return x        

    def getDXCCs(self): # Gibt alle DXCC Nummern zurück
        i = 0
        l = []
        for i in range(0, len(ADIF.qsos)):
            l.append (ADIF.qsos[i]['DXCC'])
        ln = (set(l))
        return ln

    def anzahlDXCCs(self): # Gibt die Anzahl der DXCCs zurück
        i = 0
        l = []
        for i in range(0, len(ADIF.qsos)):
            l.append (ADIF.qsos[i]['DXCC'])
        ln = (set(l))
        return len(ln)
                