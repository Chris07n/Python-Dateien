def start_conversation():
    print("Hallo! Wie heißt du?")
    name = input("Dein Name: ")
    
    print(f"Hallo, {name}! Wie fühlst du dich heute?")
    mood = input("Antwort: ")
    
    print(f"Ah, du fühlst dich also {mood}. Interessant! Was ist dein Lieblingsessen?")
    food = input("Antwort: ")
    
    print(f"Lecker! {food} mag ich auch. Was machst du gerne in deiner Freizeit?")
    hobby = input("Antwort: ")
    
    print(f"{hobby} klingt nach Spaß! Hast du noch etwas, worüber du sprechen möchtest?")
    more_conversation = input("Ja oder Nein: ").lower()
    
    if more_conversation == "ja":
        print("Erzähle mir mehr!")
        additional_info = input("Antwort: ")
        print(f"Das ist wirklich interessant! Danke, dass du es mit mir geteilt hast.")
    else:
        print("Okay, es war schön mit dir zu reden! Bis bald.")

# Start der Konversation
start_conversation()
