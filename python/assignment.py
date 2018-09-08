# authors: oolofsson, wvage, erikco

import monkdata as m
from dtree import *
import random
import matplotlib.pyplot as plotta
from statistics import *

def calculate_entropy():
    print("entropy of monk1:", entropy(m.monk1))
    print("entropy of monk2:", entropy(m.monk2))
    print("entropy of monk3:", entropy(m.monk3))

def calculate_average_gain():
    #monk1
    print("average gain of a1 in monk1", averageGain(m.monk1, m.attributes[0]))
    print("average gain of a2 in monk1", averageGain(m.monk1, m.attributes[1]))
    print("average gain of a3 in monk1", averageGain(m.monk1, m.attributes[2]))
    print("average gain of a4 in monk1", averageGain(m.monk1, m.attributes[3]))
    print("average gain of a5 in monk1", averageGain(m.monk1, m.attributes[4]))
    print("average gain of a6 in monk1", averageGain(m.monk1, m.attributes[5]))
    print("")

    #monk2
    print("average gain of a1 in monk2", averageGain(m.monk2, m.attributes[0]))
    print("average gain of a2 in monk2", averageGain(m.monk2, m.attributes[1]))
    print("average gain of a3 in monk2", averageGain(m.monk2, m.attributes[2]))
    print("average gain of a4 in monk2", averageGain(m.monk2, m.attributes[3]))
    print("average gain of a5 in monk2", averageGain(m.monk2, m.attributes[4]))
    print("average gain of a6 in monk2", averageGain(m.monk2, m.attributes[5]))
    print("")

    #monk3
    print("average gain of a1 in monk3", averageGain(m.monk3, m.attributes[0]))
    print("average gain of a2 in monk3", averageGain(m.monk3, m.attributes[1]))
    print("average gain of a3 in monk3", averageGain(m.monk3, m.attributes[2]))
    print("average gain of a4 in monk3", averageGain(m.monk3, m.attributes[3]))
    print("average gain of a5 in monk3", averageGain(m.monk3, m.attributes[4]))
    print("average gain of a6 in monk3", averageGain(m.monk3, m.attributes[5]))

def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def prune(dataset, fraction):
    training_set, validation_set = partition(dataset, fraction)
    newtree = buildTree(training_set, m.attributes);
    bestVal = 10000;
    while  True:
        alternativeTrees = allPruned(newtree)
        minVal = 10000;
        bestTree = 10000;
        if len(alternativeTrees) == 1:
            break
        for i in range (1, len(alternativeTrees)):
            tempVal = (1 - check(alternativeTrees[i], validation_set))
            if tempVal < minVal:
                minVal = tempVal
                bestTree = i;
        if (minVal <= bestVal):
            bestVal = minVal
        else:
            break
        newtree = alternativeTrees[bestTree]
    return newtree, 1 - check(newtree, validation_set) # returns the new tree and the error rate for it

def main():
    calculate_entropy() # assignment 1
    calculate_average_gain() # assignment 3

    monk1_error_rates = [] # all the error rates from the 100 iterations for monk1
    monk2_error_rates = [] # all the error rates from the 100 iterations for monk2
    monk3_error_rates = [] # all the error rates from the 100 iterations for monk3
    stdev_monk1 = [0, 0, 0, 0, 0, 0] # standard deviation for monk1 per fraction
    stdev_monk2 = [0, 0, 0, 0, 0, 0] # standard deviation for monk2 per fraction
    stdev_monk3 = [0, 0, 0, 0, 0, 0] # standard deviation for monk3 per fraction

    fractions = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8] # different fractions to be used
    N = 100
    monk1_mean_error_rates = [0, 0, 0, 0, 0, 0] # array with the mean of error rates for monk1
    monk2_mean_error_rates = [0, 0, 0, 0, 0, 0] # array with the mean of error rates for monk2
    monk3_mean_error_rates = [0, 0, 0, 0, 0, 0] # array with the mean of error rates for monk3
    for i in range(0, len(fractions)):
        total_error_monk1 = 0
        total_error_monk2 = 0
        total_error_monk3 = 0
        for x in range (0, N):
            t=buildTree(m.monk1, m.attributes)
            original_error_monk1 = 1 - check(t, m.monk1test)
            tree, error = prune(m.monk1, fractions[i])
            monk1_error_rates.append(error)
            total_error_monk1 = total_error_monk1 + error

            t=buildTree(m.monk2, m.attributes)
            original_error_monk2 = 1 - check(t, m.monk2test)
            tree, error = prune(m.monk2, fractions[i])
            total_error_monk2 = total_error_monk2 + error
            monk2_error_rates.append(error)

            t=buildTree(m.monk3, m.attributes)
            original_error_monk3 = 1 - check(t, m.monk3test)
            tree, error = prune(m.monk3, fractions[i])
            total_error_monk3 = total_error_monk3 + error
            monk3_error_rates.append(error)


        monk1_mean_error_rates[i] = total_error_monk1 / N
        monk2_mean_error_rates[i] = total_error_monk2 / N
        monk3_mean_error_rates[i] = total_error_monk3 / N
        stdev_monk1[i] = stdev(monk1_error_rates)
        stdev_monk2[i] = stdev(monk2_error_rates)
        stdev_monk3[i] = stdev(monk3_error_rates)
        monk1_error_rates.clear()
        monk2_error_rates.clear()
        monk3_error_rates.clear()

    
    print("\n monk1")
    for i in range(0,6):
        print(monk1_mean_error_rates[i], " with fraction = ", fractions[i])
        print("standard deviation = ", stdev_monk1[i])

    print("\nmonk2")
    for i in range(0,6):
        print(monk2_mean_error_rates[i], " with fraction = ", fractions[i])
        print("standard deviation = ", stdev_monk2[i])

    print("\nmonk3")
    for i in range(0,6):
        print(monk3_mean_error_rates[i], " with fraction = ", fractions[i])
        print("standard deviation = ", stdev_monk3[i])


    # PLOTTING THE GRAPHS
    plotta.plot(fractions, monk1_mean_error_rates, color='#000000', marker='o', label = "Mean of errors")
    plotta.title("MONK-1 Fractions vs Error rate")
    plotta.xlabel("fractions")
    plotta.ylabel("errors")
    plotta.legend(loc='upper right', frameon=False)
    plotta.show()

    plotta.plot(fractions, monk2_mean_error_rates, color='#000000', marker='o', label = "Means of errors")
    plotta.title("MONK-2 Fractions vs Error rate")
    plotta.xlabel("fractions")
    plotta.ylabel("errors")
    plotta.legend(loc='upper right', frameon=False)
    plotta.show()

    plotta.plot(fractions, monk3_mean_error_rates, color='#000000', marker='o', label = "Means of errors")
    plotta.title("MONK-3 Fractions vs Error rate")
    plotta.xlabel("fractions")
    plotta.ylabel("errors")
    plotta.legend(loc='upper right', frameon=False)
    plotta.show()
main()
