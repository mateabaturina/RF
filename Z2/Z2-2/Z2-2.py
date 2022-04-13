import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter

f=open("Z2-2.txt","r")
lines=f.readlines()
x_ = np.array([])
y = np.array([])

for i in lines:
    x_ = np.append(x_, i.split(' ')[0])

f.close()

x_ = np.delete(x_, np.where(x_ == '\n'))
x = x_.astype(float)

for i in range(0, 64001):
    y = np.append(y, 0.0)

nullfmt = NullFormatter()  #bez brojeva

# definicija sirina i visina
x0, sirina = 0.1, 0.65 
y0, visina = 0.1, 0.65
pomak_x = pomak_y = x0+sirina+0.02
sirina2 = visina2 = 0.2
# dfinicija podrucja za crtanje
graf_cestice = [x0, y0, sirina, visina]
histogram_x = [x0, pomak_x, sirina, visina2]
histogram_y = [pomak_y, y0, sirina2, visina]
plt.figure(1, figsize=(8,8))

# koordinatne osi
axCestice = plt.axes(graf_cestice)
axHistx = plt.axes(histogram_x)
axHisty = plt.axes(histogram_y)
# izbjegavanje zajednickih brojeva 
axHistx.xaxis.set_major_formatter(nullfmt)
axHisty.yaxis.set_major_formatter(nullfmt)

# polozaji cestica
axCestice.scatter(x, y, s=1)
# prikaz podrucja unutar kojeg brojimo cestice 
dx = 5.0
#y1=0.0
#x1=0.0
#axCestice.axhline(y=y1,    color='b')
#axCestice.axhline(y=y1+dx, color='b')
#axCestice.axvline(x=x1,    color='r')
#axCestice.axvline(x=x1+dx, color='r')
# nazivi koordinatnih osi
axCestice.set_xlabel("x / cm")
axCestice.set_ylabel("y / cm")

# gnanice podrucja unutar kojeg su cestice
xymax = np.max( [np.max(np.fabs(x)), np.max(np.fabs(y))] )
lim = ( int(xymax/dx) + 1) * dx
axCestice.set_xlim( (-lim, lim) )
axCestice.set_ylim( (-lim, lim) )
# brojanje cestica po koordinatama
bins = np.arange(-lim, lim + dx, dx)
axHistx.hist(x, bins=bins, color='r', edgecolor='black', linewidth=1.0)
axHistx.set_ylabel("N(x)", color='r')
axHisty.hist(y, bins=bins, color='b', orientation='horizontal', edgecolor='black', linewidth=1.2)
axHisty.set_xlabel("N(y)", color='b')

# max broj cestica unutar koordinanog intervala
axHistx.set_xlim( axCestice.get_xlim() )
axHisty.set_ylim( axCestice.get_ylim() )

plt.savefig('Z2-2.png')
plt.show() #prikaz grafa
