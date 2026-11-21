"""Functies bij de opdracht Schat π met Monte Carlo."""
import random #Nodig om willekeurige getallen te genereren voor x en y

def is_in_unit_circle(x, y):
    """Geeft aan of het punt (x, y) in of op de eenheidscirkel ligt"""

    inUnitCircle = False

    if (x**2+y**2) <= 1:
        inUnitCircle = True
    
    return inUnitCircle

def estimate_pi(n, seed):
    """Geeft een herhaalbare schatting van π voor n punten en de gegeven seed."""
    counter = 0
    random.seed(seed) #Hier wordt de seed ingevoerd zodat de resultaten reproduceerbaar zijn

    i = n #Gezien ik n later nog gebruik (en anders deel ik door 0...)

    while i > 0:
        x = random.random()
        y = random.random()

        if is_in_unit_circle(x, y) == True:
            counter = counter + 1

        i = i - 1 

    return float(4*(counter/n)) #Voor de uitleg over de 4 zie de README

#Alle prints gebruikt voor de uitleg in de README
#"""
print("De volgende zijn tests op seed 42 van 4, 50 en 500000")
print(estimate_pi(4, 42))
print(estimate_pi(50, 42))
print(estimate_pi(500000, 42))
print("De volgende zijn tests van 5 punten met seeds 1, 2 en 3")
print(estimate_pi(5, 1))
print(estimate_pi(5, 2))
print(estimate_pi(5, 3))
print("De volgende zijn tests van 5000 punten met seeds 1, 2 en 3")
print(estimate_pi(5000, 1))
print(estimate_pi(5000, 2))
print(estimate_pi(5000, 3))
#"""