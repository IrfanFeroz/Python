import random
import operator

def fitness(x, y):
    z = -((x/100)**2 + (y/100)**2);
    return z

populationx = random.sample(range(-500,500),10);
populationy = random.sample(range(-500,500),10);

print(populationx)
print(populationy)
#for i in range(len(populationx)):
#    populationx[i] = populationx[i]/100;
#    populationy[i] = populationy[i]/100;

for k in range(0,100):    
    fvalue={};
    for i in range(len(populationx)):
        fvalue[i] = fitness(populationx[i],populationy[i])

    fvalue = list(fvalue.values());
    fvalueSorted = sorted(fvalue);

    indexes = []
    for j in range(1,7):
        indexes.extend([i for i,x in enumerate(fvalue) if x == fvalueSorted[-j]])

    parentx = [];
    for j in range(0,6):
        parentx.extend([bin(populationx[indexes[j]]+500)[2:]])
        
    subpopulationx = [];
    for j in range(0,3):
        temp = random.sample(range(1,min(len(parentx[2*j]),len(parentx[2*j+1]))),1)
        subpopulationx.extend([parentx[j][0:temp[0]]+parentx[j+1][temp[0]:]])

    for i in range(0,3):
        temp = random.sample(range(0,len(subpopulationx[i])),1)
        subpopulationx[i] = list(subpopulationx[i])
        subpopulationx[i][temp[0]] = abs(int(subpopulationx[i][temp[0]],2)-1)
        temp2 = ''
        for j in range(0,len(subpopulationx[i])):
            temp2 = temp2 + str(subpopulationx[i][j])
        subpopulationx[i] = temp2

    subpopulationx[0] = int(subpopulationx[0],2)-500
    subpopulationx[1] = int(subpopulationx[1],2)-500
    subpopulationx[2] = int(subpopulationx[2],2)-500
    
    indexess = []
    for j in range(0,3):
        indexess.extend([i for i,x in enumerate(fvalue) if x == fvalueSorted[j]])

    for i in range(0,3):
        populationx[indexess[i]] = subpopulationx[i];

    parenty = [];
    for j in range(0,6):
        parenty.extend([bin(populationy[indexes[j]]+500)[2:]])
        
    subpopulationy = [];
    for j in range(0,3):
        temp = random.sample(range(1,min(len(parenty[2*j]),len(parenty[2*j+1]))),1)
        subpopulationy.extend([parenty[j][0:temp[0]]+parenty[j+1][temp[0]:]])

    for i in range(0,3):
        temp = random.sample(range(0,len(subpopulationy[i])),1)
        subpopulationy[i] = list(subpopulationy[i])
        subpopulationy[i][temp[0]] = abs(int(subpopulationy[i][temp[0]],2)-1)
        temp2 = ''
        for j in range(0,len(subpopulationy[i])):
            temp2 = temp2 + str(subpopulationy[i][j])
        subpopulationy[i] = temp2

    subpopulationy[0] = int(subpopulationy[0],2)-500
    subpopulationy[1] = int(subpopulationy[1],2)-500
    subpopulationy[2] = int(subpopulationy[2],2)-500

    for i in range(0,3):
        populationy[indexess[i]] = subpopulationy[i]; 

    print(k,min(fvalue)/100)

print(populationx)
print(populationy)
print(min(fvalue)/100)
