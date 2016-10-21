threes=0
fives=0
fifteens=0
for i in range(0,1000,3):
    threes = threes + i
for i in range(0,1000,5):
    fives = fives+i
for i in range(0,1000,15):
    fifteens=fifteens+i
print(fives,threes,fifteens,fives+threes-fifteens)
