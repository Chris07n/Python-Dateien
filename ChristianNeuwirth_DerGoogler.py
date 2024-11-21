# -*- coding: utf-8 -*-

import webbrowser

# Eingabe vom Benutzer
eingabe = input("Gib 'suche' ein, um eine URL zu öffnen: ")

# Überprüfung
if eingabe.lower() == "suche":
    # URL, die geöffnet werden soll
    url = "https://www.google.de/?hl=de"
    webbrowser.open(url)
else:
    print("Ungültige Eingabe. Bitte gib 'suche' ein.")

