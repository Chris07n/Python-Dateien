
print("Hallo! Wie heißt du?")
name = input ("Dein Name: ")

print (f"Hallo {name}, möchtest du wissen wie ich heiße?")
more_conversation = input("Ja oder Nein: ")
    
if more_conversation == "ja":
    print("Mein Name lautet Ada.")
else:
    print("Na gut.")
    
print (f"Wie alt bist du {name}?")
age = input ("Antwort: ")

print (f"Aha, {age} Jahre alt bist du also {name}!")


