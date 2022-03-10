import random

f = open("primjer1.txt", "w")
f2 = open("primjer2.txt", "w")
x_list = []
y_list = []

for i  in range(0, 5001):
        x_i = random.random() * 20 + 40
        y_i = random.random() * 10 + 15
        x_list.append(x_i)
        y_list.append(y_i)

for K in range(0, 5001):
    for i  in range(0, 5001):
        delta_x = random.random() - 0.5
        delta_y = random.random() * 3 - 1.5
        x_list[i] = x_list[i] + delta_x
        if (x_list[i] < 0):
            x_list[i] = x_list[i] * (-1)
        if (x_list[i] > 100):
            x_list[i] = 200 - x_list[i]
        x_list.append(x_list[i])
        y_list[i] = y_list[i] + delta_y
        if (y_list[i] < 0):
            y_list[i] = y_list[i] * (-1)
        if (y_list[i] > 100):
            y_list[i] = 200 - y_list[i]
        y_list.append(y_list[i])
    f.write(str(K) + " " + str(x_list[1]) + " " + str(y_list[1]) + " " + str(x_list[5]) + " " + str(y_list[5]) + " " + str(x_list[9]) + " " + str(y_list[9]) + "\n")
    if (K%10==0):
        for i in range(0, 5001):
            f2.write(str(x_list[i]) + " " + str(y_list[i]) + "\n")
        f2.write("\n\n")

    
