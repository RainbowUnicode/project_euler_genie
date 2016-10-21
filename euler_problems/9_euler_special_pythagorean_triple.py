"""
A pythagorean triple of integers satisfies
a^2+b^2=c^2
with a<b<c.

There exists exactly one pythagorean triple with a+b+c=1000.
Find the product abc of this pythagorean triple.
"""

for b in range(1,500):
    for a in range(1,b):
        for c in range(1,a+b):
            if a+b+c==1000:
                if a**2+b**2==c**2:
                    print(a,b,c,a*b*c)