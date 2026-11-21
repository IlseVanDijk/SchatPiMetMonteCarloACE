# Schat π met Monte Carlo

Kopieer deze bestanden naar de hoofdmap van je eigen openbare GitHub-repository, ook de map `.github`. Gebruik Python 3 en de standaardbibliotheek.

## Uitvoeren

Open een terminal in de map met de drie bestanden en voer dit commando uit.

```text
python -m unittest -v
```

GitHub Actions voert hetzelfde commando uit bij elke push (zie `.github/workflows/tests.yml`). Het portaal laat zien of die run geslaagd is.

De meegeleverde voorbeeldtest geeft in de starterversie een `NotImplementedError`. Vul beide functies in en schrijf minstens één eigen test voor een punt op de rand van de eenheidscirkel.

## Uitleg

Factor 4: 
Gezien de eenheidscirkel tussen de punten [1,0], [0,1], [-1,0] en [0,-1] (zie cosinus en sinus op pi) loopt maar de punten alleen maar door .random() tussen 0 en 1 gegenereerd worden word maar voor een 4e van de cirkel gecheckt. Daarom doen we de uiteindelijke verhouding x4 om daarvoor de corrigeren.

n en seeds:
Als je maar weinig punten controleert, dan is er een veel grotere kans dat deze niet echt even verdeeld zijn waardoor het een stuk minder accuraat is. Zie bijvoorbeeld 4, 50 en 500000 punten op seed 42: 3.0, 2.8, 3.141776. Wiskundig bewijs: triviaal.
De seed zelf maakt een beetje uit, zeker met lage getallen. 
Zie seeds 1,2 en 3 bij n = 5:
3.2
2.4
4.0
En zie seeds 1,2 en 3 bij n = 5000:
3.1592
3.1592
3.1528
Bij hoge getallen maakt de seed veel minder uit omdat de punten veel meer verdeeld zijn..

## Bronnen en licenties

Python Software Foundation, Python Software Foundation License Version 2
W3Schools, Copyright 1999-2026 by W3Schools. All Rights Reserved

## AI-assistenten

Geen
