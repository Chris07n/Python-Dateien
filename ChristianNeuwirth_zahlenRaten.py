import random

def piraten_spiel():
    print("Arrgghhhhh ich bin Käptn Hook. Wenn du meinen Schatz haben willst, musst du meine Zahl zwischen 1 und 100 erraten ha ha ha. Du hast nur 6 versuche meinen Schatz zu erhalten")

    secret_number = random.randint (1, 100)
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
