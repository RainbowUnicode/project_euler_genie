"""
The smallest number evenly divisible by all integers between 1 and 10 is 2520.
What is the smallest number evenly divisible by all integers between 1 and 20?
"""

import math

def general_lcm(group):
    """
    Computes the least common multiple of all the integers in group.
    :param group: Must be a list of integers.
    :return: Returns the general least common multiple.
    """
    lcm_holder=group[0]*group[1]//math.gcd(group[0],group[1])
    for i in range(2,len(group)):
        a=group[i]
        lcm_holder=a*lcm_holder//math.gcd(a,lcm_holder)
    return lcm_holder


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(general_lcm(l))

