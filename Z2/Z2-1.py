import random

f = open("primjer2.txt", "w")
f2 = open("Z2-2.txt", "w")
f3 = open("Z2-3.txt", "w")
x_list = []
Sx2 = 0

for i  in range(0, 64001):
        x_i = 0
        x_list.append(x_i)

for K in range(0, 201):
    for i  in range(0, 64001):
        delta_x = random.random() * 6 - 3
        x_list[i] = x_list[i] + delta_x
        Sx2 += x_list[i] * x_list[i]
        x_list.append(x_list[i])
    Sx2 /= 64001
    f3.write(K + " " + Sx2 +"\n")
    for i in range(0, 64001):
        f.write(str(x_list[i]) + " " + str(0) +"\n")
    f.write("\n\n")
    if (K==200):
        for i in range(0, 64001):
            f2.write(str(x_list[i]) + " " + str(0) +"\n")
        f2.write("\n\n")