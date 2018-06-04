#!/usr/bin/env python3

# Libraries and variables
# ------------------------

#import os
from os import listdir

basedir = input("Pfad angeben: (default: aktuelles Verzeichnis) ")
if not basedir:
    basedir = "."

counter = 0

filetypes_total = []
filetypes_knoten = []

# eine Datei auswerten
# --------------------

def filetype_liste(endung,liste):
    if not endung in liste:
        liste.append(endung)

def datei_lesen(datei):

        global counter

        endung = datei.split(".")[-1]
        filetype_liste(endung,filetypes_total)

        dateiobj = open(datei, "r", encoding="ANSI")

        for line in dateiobj:
            if "<entry" in line:
                counter += 1

                filetype_liste(endung,filetypes_knoten)

# Verzeichnis rekursiv auflisten
# ------------------------------

def rekurs_auflisten(datei):

    # wenn Verzeichnis, Inhalt auswerten
    try:
        #contents = os.listdir(datei)
        contents = listdir(datei)
    except: # wenn kein Verzeichnis, Datei einlesen
        datei_lesen(datei)
        return

    for item in contents:
        subdir = "{}\\{}".format(datei,item)
        rekurs_auflisten(subdir)
        
rekurs_auflisten(basedir)

print("\n*** gezählte <entry>-Tags:",counter, "***\n")
print("Diese Dateitypen wurden gefunden:")
print(filetypes_total)
print("in diesen Dateitypen wurden Knoten gefunden:")
print(filetypes_knoten)
fin = input("\nEnter drücken, um Programm zu beenden")
