import random

f = open("primjer2.txt", "w")
f2 = open("Z2-2.txt", "w")
f3 = open("Z2-3.txt", "w")
f4 = open("Z2-6_hod.txt", "w")
x_list = []
Sx2 = 0
dx = 2
P = []
p=200/dx
poz = 0

for i in range(0, int(p) + 1):
    P.append(0)

for i  in range(0, 64001):
        x_i = 0
        x_list.append(x_i)

for K in range(0, 201):
    for i  in range(0, 64001):
        delta_x = random.random() * 6 - 3
        x_list[i] = x_list[i] + delta_x
        Sx2 += x_list[i] * x_list[i]
        x_list.append(x_list[i])
    Sx2 /= 64000
    f3.write(str(K) + " " + str(Sx2) +"\n")
    for i in range(0, 64001):
        f.write(str(x_list[i]) + " " + str(0) +"\n")
    f.write("\n\n")
    if (K==200):
        for i in range(0, 64001):
            f2.write(str(x_list[i]) + " " + str(0) +"\n")
        f2.write("\n\n")
    if (K==50 or K==100 or K==150 or K==200):
        for i in range(0, 64001):
            if((x_list[i] >=-100) and (x_list[i] <= 100)):
                d=(int)((x_list[i]+100)/dx)
                P[d] += 1
        for i in range(0, int(p) + 1):
            poz=-100+dx*i
            f4.write(str(poz) + " " + str(P[i]/(64000*dx)) +"\n")
        f4.write("\n\n")