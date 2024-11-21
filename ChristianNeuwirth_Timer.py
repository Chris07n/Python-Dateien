# -*- coding: utf-8 -*-
import time

#mood
print ("Hallo wie gehts dir?")
time.sleep(30)
mood = input ("gut oder schlecht?: ")

if mood == "gut":
    print("Schön, dass es dir gut geht")

else:
    print("Oh, wieso denn das?: ")
    time.sleep(30)
    badMood = input ("Wieso geht es dir schlecht?: ")
    print("Das tut mir leid, ich hoffe dein Tag entwickelt sich trotzdem zu etwas gutem.: ")

#Name
print("Wie heißt du?: ")
time.sleep(30)
name = input("Dein Name: ")
print(f"{name} ist ein schöner Name!: ")

#Lieblingsessen
print(f"Also {name} was ist dein Lieblingsessen?: ")
time.sleep(30)
food = input ("Tippe hier deine Leibspeise ein.: ")
print("Das ist mega Lecker!: ")

#Lieblingsfarbe
print(f" {name} welche Farbe ist dir am liebsten?: ")
time.sleep(30)
fav_color = input ("Lieblingsfarbe: ")
print("Schöne Farbe")

#Lieblingstier
print("Was ist dein Lieblingstier? ")
time.sleep(30)
fav_animal = input ("Lieblingstier: ")
print("Süßes Tier")

#Lieblingskünstler
print("Nenne mir deinen Lieblingskünstler")
time.sleep(30)
fav_artist = input ("Tippe hier deinen Künstler ein: ")
print("Diesen Künstler höre ich auch")

#Hobby
print("Was tust du gerne in deiner Freizeit?")
time.sleep(30)
hobby = input ("Hobby: ")
print("Schön")

#Traumberuf
print("Was möchtest du später mal werden?")
time.sleep(30)
job = input ("Traumberuf: ")
print(f"Viel glück {job} zu werden")

#Alter
print("Wie alt bist du?")
time.sleep(30)
age = input ("Alter eingeben: ")
print (f" {age} ist eine cooles Alter")

#Reise
print("Wohin würdest du gerne reisen?")
time.sleep(30)
travel = input ("Traumreise: ")
print(f"{travel} ist ein wundervoller Ort")

print("Also dann, Bye bye")










            
