"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

"""
Divide by n.  If n divides k, then consider k//n.
Check to see if k//n is prime.
If so, k//n is max.  Else, increment n.
"""

def factor_killer(big_number,divisor):
    """
    Eliminates all multiples of divisor from big_number
    :param big_number: integer
    :param divisor:
    :return: if divisor is greater than big_number, returns 0.
        If divisor divides big_number, returns big_number divided maximally by divisor.
        Otherwise, returns big_number unchanged.
    """
    if big_number<divisor:
        return 0
    while big_number%divisor==0:
        big_number=big_number//divisor
    return big_number

test=75135465813136584
tracker=1
i=2
while test >1:
    if test%i==0:
        tracker=i
        print(tracker) #remove this line to print only largest.
        test = factor_killer(test,i)
    i=i+1
print(tracker)
