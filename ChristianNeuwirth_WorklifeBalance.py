import time
import webbrowser

# Zeiten
arbeitszeit = 8 * 60 * 60  # 8 Stunden in Sekunden
pausenintervall = 90 * 60  # 90 Minuten in Sekunden
pausenzeit = 7.5 * 60  # 7.5 Minuten in Sekunden

# Lieblingslied
lieblingslied_url = "https://www.youtube.com/watch?v=V8EkSVxE0mo"  

# Funktion für die Pausen
def pause_machen():
    print("Gut gearbeitet. Gönn dir eine Pause!")
    webbrowser.open(lieblingslied_url)  # Öffnet den YouTube-Link im Standardbrowser
    time.sleep(pausenzeit)  # Warte, bis die Pause zu Ende ist
    print("Pause vorbei! Weiterarbeiten...")

# Hauptfunktion für den Lernzyklus
def arbeiten():
    startzeit = time.time()  # Startzeit für den Lernzyklus
    while time.time() - startzeit < arbeitszeit:
        print("Arbeiten... Noch 90 Minuten bis zur nächsten Pause.")
        time.sleep(pausenintervall)  # 90 Minuten arbeiten
        pause_machen()

# Das Programm starten
if __name__ == "__main__":
    arbeiten()
