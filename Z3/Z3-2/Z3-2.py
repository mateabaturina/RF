# GRAF 0: ucitavanje modula za crtanje grafova i dodjela imena plt
#import matplotlib.pyplot as plt

# 1. PARAMETRI MODELA I POCETNE VRIJEDNOSTI
# procijenjeno iz JHU CSSE baze za Hrvatsku nakon 07.05.2021.
g = 0.1874833555
b = 8.087E-07
s = 157513
i = 11265
r = 331222
t0 = 0
tn = 85
n = 8500
dt = (tn-t0)/n

f = open("S.txt", "w")
f2 = open("I.txt", "w")
f3 = open("R.txt", "w")

# GRAF 1: stvaranje listi vrijednosti t, S, I, R
t = [t0]
S = [s]
I = [i]
R = [r]

# 2. PETLJA PO VREMENSKIM KORACIMA I PROCJENA NOVIH VRIJEDNOSTI
for it in range(1, n):
    # brzine promjena
    vs = -b*s*i
    vi = b*i*s - g*i
    vr = g*i
    # promjena = brzina promjene * trajanje
    # novo = prethodno + promjena
    s = s + vs * dt
    i = i + vi * dt
    r = r + vr * dt
    # GRAF 2.A: dodavanje novih vrijednosi u liste
    t.append(t0 + it * dt)
    S.append(round(s))
    I.append(round(i))
    R.append(round(r))
    f.write(str(t0 + it * dt) + " " + str(round(s)) + "\n")
    f2.write(str(t0 + it * dt) + " " + str(round(i)) + "\n")
    f3.write(str(t0 + it * dt) + " " + str(round(r)) + "\n")
f.close()
f2.close()
f3.close()

# GRAF 2.B: UCITAVANJE PODATAKA BAZE JHU CSSE
# stvaranja listi za pohranu podataka
tp = []; Sp = []; Ip = []; Rp = [];
# otvaranje datoteke s podacima iz baze JHU CSSE  
dat = open("JHU-CSSE-CRO.txt", "r")
l = 1 # broj linije
# ucitava redom svaku liniju podataka
for linija in dat:
    # podaci su u svim linijama osim prve gdje je samo opis (zaglavlje)
    if l > 1:
        # razdvajanje linije u brojcane elemente liste podaci
        podaci = [float(x) for x in linija.split()]
        # doda elemente liste u odgovarajuca polja
        tp.append(podaci[0])
        Sp.append(podaci[1])
        Ip.append(podaci[2])
        Rp.append(podaci[3])
    l = l + 1

# 3. GRAFICKI PRIKAZ S(t), I(t), R(t)
# GRAF 3: stvaranje okoline za sliku
#fig = plt.figure(facecolor='#EEEEEE', figsize=(8, 5))
#plt.rcParams["font.size"] = "16"
# stvaranje jednog panela na slici za crtanje grafova
# graf = fig.add_subplot(1,1,1)
# crtanje podataka iz baze JHU CSSE djelomicno prozirnim (alpha=0.2) simbolima 
# graf.plot(tp, Sp, 'o', color= 'c', alpha=0.2, label='$S_\mathrm{web}$')
# graf.plot(tp, Ip, 'o', color= 'r', alpha=0.2, label='$I_\mathrm{web}$')
# graf.plot(tp, Rp, 'o', color= 'g', alpha=0.2, label='$R_\mathrm{web}$')
# crtanje procijenjenih vrijednosti linijama debljine lw
# graf.plot(t, S, 'b', lw=2, label='$S_\mathrm{sir}$')
# graf.plot(t, I, 'r', lw=2, label='$I_\mathrm{sir}$')
# graf.plot(t, R, 'g', lw=2, label='$R_\mathrm{sir}$')
# koordinatna mre??a i granice osi
# graf.grid(True)
# graf.set_xlim(t0, tn)
# graf.set_ylim(0,)
# naziv podataka na  x-osi
# graf.set_xlabel('t / dan')
# postavljanje legende
# graf.legend(loc='center right', shadow=True)
# prikaz slike
#plt.show()