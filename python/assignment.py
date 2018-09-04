# authors: oolosson, wvage

import monkdata as m
from dtree import *


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


def main():
    #calculate_entropy()
    calculate_average_gain()

main()
