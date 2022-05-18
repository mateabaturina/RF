import numpy as np
import math

f = open("Z4.txt", "w")

class Gravity:
    def __init__(self, Ms, Mz, Mj, G, xs, ys, xz, yz, xj, yj, vxs, vys, vxz, vyz, vxj, vyj, dt, t):
        self.Ms = Ms
        self.Mz = Mz
        self.Mj = Mj
        self.G = G
        self.rs = np.array([xs, ys])
        self.rz = np.array([xz, yz])
        self.rj = np.array([xj, yj])
        self.vs = np.array([vxs, vys])
        self.vz = np.array([vxz, vyz])
        self.vj = np.array([vxj, vyj])
        self.dt = dt
        self.t = t
    
    def acs(self, rs, rz, rj):
        a = np.power(np.subtract(rs,rz),2)
        b = math.sqrt(a[0] + a[1])
        F1 = -self.G * self.Mz/(b**3) * np.subtract(rs,rz)
        c = np.power(np.subtract(rs,rj),2)
        d = math.sqrt(c[0] + c[1])
        F2 = -self.G * self.Mj/(d**3) * np.subtract(rs,rj)
        return F1 + F2

    def acz(self, rs, rz, rj):
        a = np.power(np.subtract(rz,rs),2)
        b = math.sqrt(a[0] + a[1])
        F1 = -self.G * self.Ms/(b**3) * np.subtract(rz,rs)
        c = np.power(np.subtract(rz,rj),2)
        d = math.sqrt(c[0] + c[1])
        F2 = -self.G * self.Mj/(d**3) * np.subtract(rz,rj)
        return F1 + F2

    def acj(self, rs, rz, rj):
        a = np.power(np.subtract(rj,rs),2)
        b = math.sqrt(a[0] + a[1])
        F1 = -self.G * self.Ms/(b**3) * np.subtract(rj,rs)
        c = np.power(np.subtract(rj,rz),2)
        d = math.sqrt(c[0] + c[1])
        F2 = -self.G * self.Mz/(d**3) * np.subtract(rj,rz)
        return F1 + F2
        
    def RK4_metoda(self):
        self.xslista = []
        self.yslista = []
        self.xzlista = []
        self.yzlista = []
        self.xjlista = []
        self.yjlista = []
        T = 0
        while T <= self.t:
            T += self.dt
            
            k1vs = self.acs(self.rs, self.rz, self.rj) * self.dt
            k1rs = self.vs * self.dt
            k1vz = self.acz(self.rs, self.rz, self.rj) * self.dt
            k1rz = self.vz * self.dt
            k1vj = self.acj(self.rs, self.rz, self.rj) * self.dt
            k1rj = self.vj * self.dt

            k2vs = self.acs((self.rs + k1rs/2), (self.rz + k1rz/2), (self.rj + k1rj/2)) * self.dt
            k2rs = (self.vs + k1vs/2) * self.dt
            k2vz = self.acz((self.rs + k1rs/2), (self.rz + k1rz/2), (self.rj + k1rj/2)) * self.dt
            k2rz = (self.vz + k1vz/2) * self.dt
            k2vj = self.acj((self.rs + k1rs/2), (self.rz + k1rz/2), (self.rj + k1rj/2)) * self.dt
            k2rj = (self.vj + k1vj/2) * self.dt

            k3vs = self.acs((self.rs + k2rs/2), (self.rz + k2rz/2), (self.rj + k2rj/2)) * self.dt
            k3rs = (self.vs + k2vs/2) * self.dt
            k3vz = self.acz((self.rs + k2rs/2), (self.rz + k2rz/2), (self.rj + k2rj/2)) * self.dt
            k3rz = (self.vz + k2vz/2) * self.dt
            k3vj = self.acj((self.rs + k2rs/2), (self.rz + k2rz/2), (self.rj + k2rj/2)) * self.dt
            k3rj = (self.vj + k2vj/2) * self.dt

            k4vs = self.acs((self.rs + k3rs), (self.rz + k3rz), (self.rj + k3rj)) * self.dt
            k4rs = (self.vs + k3vs) * self.dt
            k4vz = self.acz((self.rs + k3rs), (self.rz + k3rz), (self.rj + k3rj)) * self.dt
            k4rz = (self.vz + k3vz) * self.dt
            k4vj = self.acj((self.rs + k3rs), (self.rz + k3rz), (self.rj + k3rj)) * self.dt
            k4rj = (self.vj + k3vj) * self.dt

            self.vs = np.add(self.vs, ((1/6) * (k1vs + 2*k2vs + 2*k3vs + k4vs)))
            self.rs = np.add(self.rs, ((1/6) * (k1rs + 2*k2rs + 2*k3rs + k4rs)))
            self.vz = np.add(self.vz, ((1/6) * (k1vz + 2*k2vz + 2*k3vz + k4vz)))
            self.rz = np.add(self.rz, ((1/6) * (k1rz + 2*k2rz + 2*k3rz + k4rz)))
            self.vj = np.add(self.vj, ((1/6) * (k1vj + 2*k2vj + 2*k3vj + k4vj)))
            self.rj = np.add(self.rj, ((1/6) * (k1rj + 2*k2rj + 2*k3rj + k4rj)))
            
            self.xslista.append(self.rs[0])
            self.yslista.append(self.rs[1])
            self.xzlista.append(self.rz[0])
            self.yzlista.append(self.rz[1])
            self.xjlista.append(self.rj[0])
            self.yjlista.append(self.rj[1])
                
            f.write(str(T) + " " + str(self.rs[0]) + " " + str(self.rs[1]) + " " + str(self.rz[0]) + " " + str(self.rz[1]) + " " + str(self.rj[0]) + " " + str(self.rj[1]) + "\n")
            f.write("\n\n")

        return (self.xslista, self.yslista, self.xzlista , self.yzlista, self.xjlista , self.yjlista)