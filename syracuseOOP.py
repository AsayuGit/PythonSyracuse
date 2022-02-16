# Killian RAIMBAUD

class syracuse:
    def __init__(self, n):
        self.__n = n;
        self.__suite = list()
        self.__flightTime = self.__compute(n)
        
    def __compute(self, n):
        self.__suite.append(n)
        if (n == 1):
            return 0
        if (n % 2):
            return self.__compute(3 * n + 1) + 1
        else:
            return self.__compute(n // 2) + 1
    
    def __str__(self):
        return "The flightTime for {} is {}\n\tThe history is {}".format(self.__n, self.__flightTime, self.__suite)

class syracuseFactory:
    def load(filepath):
        syracuseList = list()
        with open(filepath, 'r') as file:
            for number in file:
                syracuseList.append(syracuse(int(number)))
        return syracuseList
    
    def save(syracuseList, filepath):
        with open(filepath, 'w') as file:
            for item in syracuseList:
                file.write("{}\n".format(item, '\n'))

print("Veuillez entrer le nom du fichier a charger :")
syracuseList = syracuseFactory.load(input())

for item in syracuseList:
    print(item)

print("Veuillez entrer le nom du fichier a sauvegarder :")
syracuseFactory.save(syracuseList, input())