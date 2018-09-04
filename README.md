## Decision trees, Machine Learning DD2421 Lab 1

_authors: wvage@kth.se, oskarolo@kth.se_.


### Assignment 0
_**Assignment 0**: Each one of the datasets has properties which makes
them hard to learn. Motivate which of the three problems is most
difficult for a decision tree algorithm to learn_.

The MONK-2 dataset would be the hardest to learn because every variable is independent from each other.  
The MONK-1 dataset could also be hard to learn because it could take time to realise that a1 and a2 has to be equal.  
It would be easiest to learn the MONK-3 dataset because it would be easier to see that every time a5 and a4 is 1 or every time a5 is not 4 and a2 is not 3 it would evaluate to true. 

### Assignment 1
_**Assignment 1**: The file dtree.py defines a function entropy which
calculates the entropy of a dataset. Import this file along with the
monks datasets and use it to calculate the entropy of the training
datasets_.


Dataset                | Entropy
----------------------------|-----------------------------
MONK-1        | 1.0
MONK-2 | 0.957117428264771
MONK-3 | 0.9998061328047111

Code is in assingnment.py, the function calculate_entropy.  

### Assignment 2
_**Assignment 2**: Explain entropy for a uniform distribution and a
non-uniform distribution, present some example distributions with
high and low entropy_.

Example for a uniform distrubtion: Rolling a dice has entropy 2.58 which is higher than tossing a coin which has entropy 1. This is because when tossing a coin we have a larger possibility of producing an certain outcome, which leads to lower unpredictability/entropy.

Example for a non-uniform distribution: A non-uniform distribution would be a fake coin that had 0.7 probability of showing tails and a 0.3 probability of showing heads. If we calculate the entropy for that we get that  
Entropy = -0.3log2(0.3) -0.7log2(0.7) = 0.881291

### Assignment 3
_**Assignment 3**: Use the function averageGain (defined in dtree.py)
to calculate the expected information gain corresponding to each of
the six attributes. Note that the attributes are represented as in-
stances of the class Attribute (defined in monkdata.py) which you
can access via m.attributes[0], ..., m.attributes[5]. Based on
the results, which attribute should be used for splitting the examples
at the root node?_

### Assignment 4

### Assignment 5

### Assignment 6

### Assignment 7
