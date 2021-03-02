from tkinter import *
#import tkinter as tk
from tkinter import messagebox, filedialog
import time
from time import gmtime, strftime
from ADIF_Class import ADIF
import configparser
import os

config = configparser.ConfigParser()
adif = ADIF()

# Config Datei anlegen und auslesen
if os.path.isfile("config.ini"):
    ("Config File gefunden")
else:
    print("Config File angelegt")
    config['DEFAULT'] = {'lastPfad': '',
                      'Reserve1': 'yes',
                      'Reserve2': '9'}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

config.read('config.ini')
conf = config['DEFAULT']



def tick(  ):
    global utczeit
    global localzeit
    utczeit = time.strftime('%H:%M:%S',gmtime())
    localzeit = time.strftime('%H:%M:%S')
    utcuhr.config(text = utczeit)
    localuhr.config(text = localzeit) 
    utcuhr.after(200, tick) 

def adif_action():
    global name
    adif.read_ADIF(name)
    qso_anzahl_label.config(text = "Anzahl QSOs: " + str(adif.getAnzahl()))

def statistik_action():
    newWindow = Toplevel(fenster)
    labelFM = Label(newWindow, text = "FM: " + str(adif.getAnzahlMode('FM')))
    labelCW = Label(newWindow, text = "CW: " + str(adif.getAnzahlMode('CW')))
    labelSSB = Label(newWindow, text = "SSB: " + str(adif.getAnzahlMode('SSB')))
    labelFT8 = Label(newWindow, text = "FT8: " + str(adif.getAnzahlMode('FT8')))

    labelFM.pack()
    labelCW.pack()
    labelSSB.pack()
    labelFT8.pack()

def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Julian Wöhrer\n\
Date: 02.03.2021\n\
Version: 0.01\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
        
name = conf['lastpfad']
def openfile():
    global name
    name = filedialog.askopenfilename()
    #Label anpassen 
    pfad_label.config(text = name)
    #Config ändern
    config.set('DEFAULT','lastpfad',name)
    #Config überschreiben
    with open('config.ini', 'w') as configfile:
        config.write(configfile)




# Ein Fenster erstellen
fenster = Tk()
# Den Fenstertitle erstellen
fenster.title("ADIF Auswertung")


# Menü

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei und Help erstellen
datei_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# Beim Klick auf Datei oder auf Help sollen nun weitere Einträge erscheinen.
# Diese werden also zu "datei_menu" und "help_menu" hinzugefügt
datei_menu.add_command(label="ADIF einlesen", command=adif_action)
datei_menu.add_separator() # Fügt eine Trennlinie hinzu
datei_menu.add_command(label="Exit", command=fenster.quit)

help_menu.add_command(label="Info!", command=action_get_info_dialog)

# Nun fügen wir die Menüs (Datei und Help) der Menüleiste als
# "Drop-Down-Menü" hinzu
menuleiste.add_cascade(label="Datei", menu=datei_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

# Die Menüleiste mit den Menüeinrägen noch dem Fenster übergeben und fertig.
fenster.config(menu=menuleiste)   



#Labels erstellen

utc_label = Label(fenster, 
                text = "UTC",
                font=('Arial',30),
                fg='black',
                width = 10,
                height = 1)

local_label = Label(fenster, 
                text = "Lokal",
                font=('Arial',30),
                fg='black',
                width = 10,
                height = 1)

pfad_label = Label(fenster, text = name)
qso_anzahl_label = Label(fenster, text = "0")            


# Buttons erstellen

openfile_Button = Button(fenster, text = "File wählen", command=openfile, height = 2)
adif_button = Button(fenster, text="ADIF einlesen", command=adif_action, height = 2)
stats_button = Button(fenster, text="Statistik", command=statistik_action, height = 2)

# Uhrzeit wird über ein Label angezeigt und mit pack im fenster gezeigt

utcuhr = Label(master=fenster,
            font=('Arial',30),
            fg='black',
            width = 10,
            height = 1)

localuhr = Label(master=fenster,
            font=('Arial',30),
            fg='black',
            width = 10,
            height = 1)


utc_label.pack()
utcuhr.pack()
local_label.pack()
localuhr.pack() 
openfile_Button.pack()
pfad_label.pack()
adif_button.pack()
qso_anzahl_label.pack()
stats_button.pack()


utczeit = ''
localzeit = ''
 
tick()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
fenster.mainloop()


# Setup mit pyinstaller main.spec