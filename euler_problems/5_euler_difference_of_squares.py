"""
The sum of the squares of the first ten integers is 385,
while the square of the sum is 3025 for a difference of 2640.
What is the difference between the sum of the squares and the
square of the sum for the first 100 integers?
"""
a=0
b=0
for i in range(101):
    a=a+i

a=a**2

for i in range(101):
    b=b+i**2

print(a-b)

