#python igra-pogodi broj

import random

tajnibroj = random.randint(1,30)

while True:

    pogodi = int(input("Pogodi broj izmedu 1 i 30"))

    if pogodi == tajnibroj:
        print("Bravo pogodio si trazeni broj")
        break
else:
        print("Pogrješio si, probaj ponovo")
