####################################################################
########### Irfan Feroz ################### 13 March 2017 ##########
########### Genetic Algorithm for finding Global Maxima ############
####################################################################
# Intro to GA @ # https://www.iitg.ernet.in/rkbc/CE602/CE602/Genetic%20Algorithms.pdf
# Get updated code @ https://github.com/IrfanFeroz/Python/blob/master/GA.py

import random

# Define Fitness Function:
def fitness(x, y):
    z = -((x/100)**2 + (y/100)**2);
    return z

# Initialize Search Agents:
populationx = random.sample(range(-500,500),10);
populationy = random.sample(range(-500,500),10);
# print(populationx)
# print(populationy)

for k in range(0,100):               # Loop for iterations. Could try 'while' loop.

    fvalue=[];                       # Fitness Value
    for i in range(len(populationx)):
        fvalue.extend([fitness(populationx[i],populationy[i])])

    fvalueSorted = sorted(fvalue);

    indexes = []                      # Index of current maxima value among the agents
    for j in range(1,7):
        indexes.extend([i for i,x in enumerate(fvalue) if x == fvalueSorted[-j]])

## Processing the x coordinates
        
    parentx = [];                     # Selection 
    for j in range(0,6):              # Select best agents and Convert Decimal coordinates to Binary
        parentx.extend([bin(populationx[indexes[j]]+500)[2:]])      # Adding 500 because binary values of -ve numbers are tricky to handle
        
    subpopulationx = [];              # Cross-Over
    for j in range(0,3):              # Randomly choose a point in the parent chromosomes and swap the genes
        temp = random.sample(range(1,min(len(parentx[2*j]),len(parentx[2*j+1]))),1)
        subpopulationx.extend([parentx[j][0:temp[0]]+parentx[j+1][temp[0]:]])

    for i in range(0,3):              # Mutation, Randomly choose a gene and flip it
        temp = random.sample(range(0,len(subpopulationx[i])),1)
        subpopulationx[i] = list(subpopulationx[i])
        subpopulationx[i][temp[0]] = abs(int(subpopulationx[i][temp[0]],2)-1)
        temp2 = ''
        for j in range(0,len(subpopulationx[i])):
            temp2 = temp2 + str(subpopulationx[i][j])
        subpopulationx[i] = temp2

    subpopulationx[0] = int(subpopulationx[0],2)-500            # Convert back to Decimal and substract the extra 500
    subpopulationx[1] = int(subpopulationx[1],2)-500
    subpopulationx[2] = int(subpopulationx[2],2)-500
    
    indexess = []                       # Update. Find the indexes of worst performing agents (Minimum values) 
    for j in range(0,3):
        indexess.extend([i for i,x in enumerate(fvalue) if x == fvalueSorted[j]])

    for i in range(0,3):                # Update agents (population) with the new agents (subpopulation) 
        populationx[indexess[i]] = subpopulationx[i];

## Do the above routine with the y coordinates
        
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

    print(k,max(fvalue)/100)            # Printing iteration with the maxima at that iteration

print('After',k+1,'iterations, Maxima occurs at (x,y) = (',round(populationx[indexes[0]]/100,3),round(populationy[indexes[0]]/100,3),')')
print('The maxima value is: ', max(fvalue)/100)
