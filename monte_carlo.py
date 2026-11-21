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

    return float(4*(counter/n))

"""
print("De volgende zijn tests op seed 42 van 4, 50 en 500000")
print(estimate_pi(4, 42))
print(estimate_pi(50, 42))
print(estimate_pi(500000, 42))

print("De volgende zijn tests op de rand, negatief binnen de rand en negatief buiten de rand")
print(is_in_unit_circle(0,1))
print(is_in_unit_circle(-1,0))
print(is_in_unit_circle(-1,-1))
"""