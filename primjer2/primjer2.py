import decimal

D = 10**(-2)
delta_x = 0.2
delta_t = 0.5
n=(20-0)/delta_x
alpha = (D * delta_t) / delta_x**2
ro_list = []
ro_k_list = []
ro_list.append(0)
ro_k_list.append(0)

f = open("primjer2.txt", "w")

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

for i in range(0, int(n)):
    x=0+delta_x*i
    if (x >= 2 and x <= 5 ):
        ro_list.append(5.5)
        ro_k_list.append(5.5)
    else:
        ro_list.append(0)
        ro_k_list.append(0)
    f.write(str(0) + " " + str(x) + " " + str(ro_list[i]) + "\n")
f.write("\n\n")

for j in float_range(0, 401, '0.5'):
    for i in range(1, int(n)):
        ro_k_list[i]=ro_list[i] + alpha*(ro_list[i-1] + ro_list[i+1] - 2*ro_list[i])
    for i in range(0, int(n)):
        ro_list[i]=ro_k_list[i]
        x = 0 + (i * delta_x)
        if (j==100 or j==200 or j==300 or j==400):
            f.write(str(j) + " " + str(x) + " " + str(ro_list[i]) + "\n")
    if (j==100 or j==200 or j==300 or j==400):
        f.write("\n\n")

    
