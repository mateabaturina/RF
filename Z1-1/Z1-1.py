import random
import math

i_0 = 0
f = open("Z1-1.txt", "w")

for i in range(1, 10**7):
    x = random.random()
    y = random.random()
    if (x**2 + y**2) < 1:
        i_0 += 1
    Pi = (4*i_0)/i
    if i % 10000 == 0:
        greska = (Pi - math.pi)
        f.write(str(i)+ " " + str(greska*math.sqrt(i))+"\n")


    



    


    
