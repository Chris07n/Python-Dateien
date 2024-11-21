import time
import webbrowser
import random

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

# Warm-Up
def warmUp():
    print("Hey, brauchst du ein kleines Warm-Up?")
    game = input("Tippe 'ja' oder 'nein': ")
    
    if game == "ja":
        # Zahlenratenspiel
        def piraten_spiel():
            print("Arrgghhhhh! Ich bin Käpt'n Hook. Wenn du meinen Schatz haben willst, musst du meine Zahl zwischen 1 und 100 erraten! Ha ha ha! Du hast nur 6 Versuche, meinen Schatz zu erhalten.")
            secret_number = random.randint(1, 100)
            attempts = 6

            while attempts > 0:
                guess = input(f"Du hast noch {attempts} Versuche. Rate die Zahl: ")

                if not guess.isdigit():
                    print("Bitte gib eine gültige Zahl ein.")
                    continue

                guess = int(guess)

                if guess < secret_number:
                    print("Zu niedrig, du Landratte!")
                elif guess > secret_number:
                    print("Zu hoch!")
                else:
                    print("Herzlichen Glückwunsch, du hast die Zahl erraten!")
                    print("Käpt'n Hook gibt dir seinen Schatz!")
                    break

                attempts -= 1

            if attempts == 0:
                print("Game over! Die geheime Zahl war:", secret_number)

        piraten_spiel()

    else:
        print("Na schön, weiter an die Arbeit!")

# Hauptfunktion für die Arbeitszeit
def arbeiten():
    pausen_counter = 0 # Zählt die Pausen
    startzeit = time.time()  # Startzeit für die Arbeitszeit
    while time.time() - startzeit < arbeitszeit:
        print("Arbeiten... Noch 90 Minuten bis zur nächsten Pause.")
        time.sleep(pausenintervall)  # 90 Minuten arbeiten
        pause_machen()
        pausen_counter += 1

        warmUp() # Nach jeder Pause wird ein Warm-Up angefragt

    vergangene_arbeitszeit = time.time()- startzeit # Zeigt die Arbeitszeit an
    print(f"Du arbeitest seit {vergangene_arbeitszeit // 60:.1f} Minuten.")
    print(f"Du hast {pausen_counter} Pausen eingelegt.")


    gesamt_zeit = time.time() - startzeit
    print(f"Wow toll gearbeitet! Du hast insgesamt {gesamt_zeit // 60:.1f} Minuten gearbeitet und {pausen_counter} Pausen eingelegt.")

# Das Programm starten
if __name__ == "__main__":  
    arbeiten()
