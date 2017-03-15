import random

def fitness(x, y):
    z = x**2 + y**2;
    return z

populationx = random.sample(range(-500,500),10)
populationy = random.sample(range(-500,500),10)

for i in range(len(populationx)):
    populationx[i] = populationx[i]/100;
    populationy[i] = populationy[i]/100;
    
fvalue={};

for i in range(len(populationx)):
    fvalue[i] = fitness(populationx[i],populationy[i])

fvalue = list(fvalue.values())
