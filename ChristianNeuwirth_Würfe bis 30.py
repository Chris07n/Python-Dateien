import random

counter = 0
max_würfe = 30

while counter < max_würfe:
    Würfelwurf = random.randint(1, 6)
    
    print(f"Wurf {counter + 1}: {Würfelwurf}")
    
    counter += 1
