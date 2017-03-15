import random
import operator

def fitness(x, y):
    z = (x/100)**2 + (y/100)**2;
    return z

populationx = random.sample(range(-500,500),10);
populationy = random.sample(range(-500,500),10);

#for i in range(len(populationx)):
#    populationx[i] = populationx[i]/100;
#    populationy[i] = populationy[i]/100;
    
fvalue={};

for i in range(len(populationx)):
    fvalue[i] = fitness(populationx[i],populationy[i])

fvalue = list(fvalue.values());
fvalueSorted = sorted(fvalue);

indexes = []
for j in range(1,5):
    indexes.extend([i for i,x in enumerate(fvalue) if x == fvalueSorted[-j]])

subPopulationx = bin(populationx[indexes[0]])[2:]


