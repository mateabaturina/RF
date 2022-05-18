import Z4 as gr 
import matplotlib.pyplot as plt
 
dt = (60*60*24)/10
t = 60*60*24*365.242*15

p1 = gr.Gravity(1.989*10**30, 5.9742*10**24, 1898*10**24, 6.67408*10**(-11), 0, 0, 1.486*10**11, 0, 7.785*10**11, 0, 0, 0, 0, 29783, 0, 13100, dt, t)

lista1, lista2, lista3, lista4, lista5, lista6 = p1.RK4_metoda()

plt.style.use("dark_background")
plt.plot(lista1, lista2, "gold", linewidth = 4, label = "Sun")
plt.plot(lista1[-1], lista2[-1], 'o', color = "gold")
plt.plot(lista3, lista4, "b", label = "Earth")
plt.plot(lista3[-1], lista4[-1], 'o', color = "b")
plt.plot(lista5, lista6, "orange", label = "Jupiter")
plt.plot(lista5[-1], lista6[-1], 'o', color = "orange")
plt.legend(loc='best')
plt.title("x-y graf")
plt.savefig("solar_system")
plt.show()