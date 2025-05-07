import math
import numpy as np

#Analiza istotnosci
def estimate_information_gain_for_value(true_amount, false_amount):
    if true_amount == 0:
        print(f"Value Gain: 0")
        return 0
    sum = true_amount+false_amount
    i = -((false_amount/sum)*math.log((false_amount/sum), 2)+(true_amount/sum)*math.log((true_amount/sum), 2))
    print(f"Value Gain: {i:.4f}")
    return i
            
def value_probability(current_value_count, attribute_count):
    w = current_value_count/attribute_count
    print(f"W: {w:.4f}")
    return w

def estimate_entropy_for_atribute(table):
    '''
    Attribute entropy (Example Experience)
    Values ( Example High, Medium, Low)
    Input table:
            value_1 value_2  value_3
    true      1     2        3
    false     4     5        6
    '''
    attribute_count = np.sum(table)
    entropy = 0
    for value_index in range(len(table[0])):
        true_amount = table[0][value_index]
        false_amount = table[1][value_index]
        current_value_count =  true_amount + false_amount
        entropy += value_probability(current_value_count,attribute_count) * estimate_information_gain_for_value(true_amount, false_amount)
    print(f"Entropy: {entropy:.4f}")
    return entropy

def estimate_information_gain_for_attribute(table):
    '''
    Example usage:
    table = np.array([[3,0,2],
                  [2,4,3]])

    estimate_information_gain_for_attribute(table)

    '''
    true_amount = np.sum(table[0])
    false_amount = np.sum(table[1])

    gain = estimate_information_gain_for_value(true_amount,false_amount) - estimate_entropy_for_atribute(table)
    print(f"Attribute gain: {gain:.4f}")
    return gain


table = np.array([[3,0,2],
                  [2,4,3]])


estimate_information_gain_for_attribute(table)

