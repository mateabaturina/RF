import random

f = open("tree.txt", "w")

x_k = 0
y_k = 0

for k in range(0, 2*10**5 + 1):    
    f.write(str(k) + " " + str(x_k) + " " + str(y_k) + "\n")
    n = random.random()
    x_p = x_k
    if (n < 0.1):
        x_k = x_k * 0.05
        y_k = y_k * 0.6
    if ((0.1 <= n) and (n< 0.2)):
        x_k = x_k * 0.05 
        y_k = -0.5 * y_k + 1.0
    if ((0.2 <= n) and (n < 0.4)):
        x_k = 0.46 * x_k - 0.15 * y_k
        y_k = 0.39 * x_p + 0.38 * y_k + 0.6
    if ((0.4 <= n) and (n< 0.6)):
        x_k = 0.47 * x_k - 0.15 * y_k
        y_k = 0.17 * x_p + 0.42 * y_k + 1.1
    if ((0.6 <= n) and (n< 0.8)):
        x_k = 0.43 * x_k + 0.28 * y_k
        y_k = -0.25 * x_p +  0.45 * y_k + 1.0
    if ((0.8 <= n) and (n< 1.0)):
        x_k = 0.42 * x_k + 0.26 * y_k
        y_k = -0.35 * x_p + 0.31 * y_k 
    f.write(str(k+1) + " " + str(x_k) + " " + str(y_k) + "\n")
    f.write("\n\n")
    
