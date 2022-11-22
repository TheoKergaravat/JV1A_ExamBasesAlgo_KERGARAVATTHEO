#partie 1 exercice 3
myTable = [5,9,6,7]
for j in range(len(myTable)):

    plusPetitElement = myTable[j]
    numeroCasePlusPetit=j

    for i in range(j,len(myTable)):
        if(plusPetitElement > myTable[i]):
            plusPetitElement = myTable[i]
            numeroCasePlusPetit = i

    sauvegarde = myTable[j]
    myTable[j] = myTable[numeroCasePlusPetit]
    myTable[numeroCasePlusPetit] = sauvegarde
print(myTable)

#partie 1 exercice 4: le tri a bulle est considéré comme lent car il est répétitif et vérifie plusieurs fois chaque élément un par un et prend le temps d'intervertir les éléments chacuns a leur tour. Le temps nécessaire à son execution est tout de même rapide.