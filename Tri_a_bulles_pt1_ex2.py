#partie 1 exercice 2
myTable = [5,9,6,7]
sauvegarde = myTable[0]
    
for i in range(len(myTable)):
    valeursup = myTable[i]
    if myTable[i] > myTable[i+1]:
        myTable[i] = myTable[i+1]


print(myTable)
