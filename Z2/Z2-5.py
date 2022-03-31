import decimal

D = 1.51018
delta_x = 0.5
delta_t = 0.0001
n=(200-0)/delta_x
alpha = (D * delta_t) / delta_x**2
ro_list = []
ro_k_list = [] 
ro_list.append(0)
ro_k_list.append(0)

f = open("Z2-5.txt", "w")

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(delta_x * delta_x - 2*D * delta_t)

for i in range(0, int(n+1)):
    x=-100+delta_x*i
    if (x == 0):
        ro_list.append(0.01)
        ro_k_list.append(0.01)
    else:
        ro_list.append(0.0)
        ro_k_list.append(0.0)
    f.write(str(0) + " " + str(x) + " " + str(ro_list[i]) + "\n")
f.write("\n\n")

for j in float_range(0, 201, '0.01'):
    for i in range(1, int(n)):
        ro_k_list[i]=ro_list[i] + alpha*(ro_list[i-1] + ro_list[i+1] - 2*ro_list[i])
    for i in range(0, int(n+1)):
        ro_list[i]=ro_k_list[i]
        x = -100 + (i * delta_x)
        if (j==50 or j==100 or j==150 or j==200):
            f.write(str(j) + " " + str(x) + " " + str(ro_list[i]) + "\n")
    if (j==50 or j==100 or j==150 or j==200):
        f.write("\n\n")