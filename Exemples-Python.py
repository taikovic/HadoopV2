


a = int(input('Donner un nombre'))

if a > 0: # Positif
    print("a est positif.")
    if a > 10:
        print("a est supérieur a 10.")
elif a < 0: # Négatif
	print("a est négatif.")
else: # Nul
	print("a est nul.")

if (a > 0 and a < 5):
    print("a entre 0 et 5")
elif (a > 5 and a < 10):
    print("a entre 5 et 10")
elif a<0 or a>10:
    print("a est hors intervalle")
else:
    print("a est supérieur à 10")


# ------------------------------
nb = 7
i = 0

while i < 10:
    print(i + 1, "*", nb, "=", (i + 1) * nb)
    i += 1 # On incrémente i de 1 à chaque tour


chaine = "Bienvenu au cours Big Data"
for lettre in chaine:
    print(lettre)

for i in range(10):
    print(i)
   
# ------------------------------

def nomFonction(param1, param2, paramN):
    # Bloc d'instructions


def fonc(a=2, b=3):
    print("a + b = ", a+b, "a x b = ",a * b)

print('Fonction avec paramettres')
fonc(5,6)

print('Fonction sans paramettres')
fonc()


def carre(valeur):
    return valeur * valeur

val = 5
print('Le carré de',val, 'est', carre(val))

# ------------------------------------

import math

print(math.sqrt(16))

import math as mathematique

print(mathematique.sqrt(16))

from math import sqrt

print(sqrt(16))

from math import *

print(sqrt(16))

# ------------------------------------

liste1 = [1, 2, 3, 4, 5]
liste2 = ['a', 'b', 'd', 'e']
liste3 = [1, 3.5, 'a', "une chaine"]
liste4 = [3,4,[1,2,3],'a',4]

print(liste1)
liste1.append(56) # On ajoute 56 à la fin de la liste
print(liste1)

liste2.insert(2, 'c') # On insère 'c' à l'indice 2
print(liste2)

del liste3[2] # On supprime le troisième élément de la liste
print(liste3)

liste4.remove(4) # Supprime l'élément 4 de la liste
print(liste4)


# ------------------------------------

liste5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
i = 0 # Notre indice pour la boucle while

while i < len(liste5):
	print(liste5[i])
	i += 1

# Cette méthode est cependant préférable
for elt in liste5: 
	print(elt)

# ------------------------------------
	
tupleVide = ()
tupleNonVide = (1,) # est équivalent à ci dessous
tupleNonVide = 1,
tupleAvecPlusieursValeurs = (1, 2, 5)

# Fonction qui retourne plusieurs valeurs
def decomposer(entier, divisePar):
    pe = entier // divisePar
    rd = entier % divisePar
    return pe, rd

partieEntiere, resteDivision = decomposer(20, 3)
liste = [1,2,4,5,8]
print(type(liste))
resultat = decomposer(20, 3)
print(resultat)
print(type(resultat))
print(partieEntiere,resteDivision)

# ------------------------------------

set1 = {obj1, obj2, ...}
fruits = {"Pommes", "Bananes", "Cerises"}

for x in fruits:
  print(x)

# ------------------------------------

monDictionnaire = {}
monDictionnaire["pseudo"] = "dddd"
monDictionnaire["mot de passe"] = "***"


print(monDictionnaire["pseudo"])

print(monDictionnaire["mot de passe"])

print(monDictionnaire)

print('-'*10)
for key in monDictionnaire:
    print(monDictionnaire[key])

print('-'*10)
for (key,value) in monDictionnaire.items():
    print(key,value)

print('-'*10)
for value in monDictionnaire.values():
    print(value)
    

for cle in frigo:
	print(cle)

for valeur in frigo.values():
	print(valeur)


from mrjob.job import MRJob
class MRWordFrequencyCount(MRJob):
	def mapper(self, numLine, line):
		words = line.split()
		for word in words:
			yield word.lower(), 1
	
	def reducer(self, key, values):
		yield key, sum(values)

if __name__ == '__main__':
	MRWordFrequencyCount.run()





