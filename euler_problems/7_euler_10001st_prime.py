"""
By listing the first six prime numbers: 2,3,5,7,11, and 13,
we can see that the 6th prime number is 13.
What is the 10,001st prime number?
"""
i=3
truth=0
prime_list = [2]
while len(prime_list)<10001:
    for p in prime_list:
        if i%p!=0:
            truth=truth+1
    if truth==len(prime_list):
        prime_list=prime_list+[i]
        #print(prime_list) testing purposes
    i=i+1
    truth=0
print(prime_list[10000])

"""
FIX ME: Slow runtime.  Takes about 5 minutes to run, despite the result being 104743.
"""