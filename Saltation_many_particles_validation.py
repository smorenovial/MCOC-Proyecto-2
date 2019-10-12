from matplotlib.pylab import *
from scipy.integrate import odeint
import random
from time import time
tiempoInicial = time()
# Unidades base SI (m, kg, s)
_m = 1.
_kg = 1.
_s = 1.
_mm = 1e-3*_m
_cm = 1e-2*_m
_gr = 1e-3*_kg 
_in = 2.54*_cm

g = 9.81*_m/(_s**2)         # gravedad
d = 0.15e-3
x = linspace(0, 20*d,4000)
x_mod_d = (x % d) - d/2
y = sqrt((d/2)**2 - x_mod_d**2)

rho_agua = 1000.*_kg/(_m**3)                   # diametro de la particula
rho_particula = 2650*_kg/(_m**3)      # densidad de la particula, considerando que sea arena 

dt = 0.001*_s    # paso de tiempo 
tmax = 0.5*_s    # tiempo maximo de simulacion
ti = 0.*_s     # tiempo actual

data = load("initial_condition.npz")
x0 = data["x0"]
y0 = data["y0"]
vx0 = data["vx0"]
vy0 = data["vy0"]
Nparticulas = data["Nparticulas"]


A = pi*(d/2)**2
V = (4./3.)*pi*(d/2)**3
m = rho_particula*V # masa de la particula


W = array([0., -m*g])  #Fuerza de peso

t = arange(0,tmax,dt)
Nt = len(t)

norm = lambda v: sqrt(dot(v,v))

Cd = 0.47                   # coeficiente de Drag para particula esferica
CL = 0.2
Cm = 0.5
Rp = 73. #250
R = (rho_particula/rho_agua - 1)
alpha = 1/(1 + R + Cm)

ihat = array ([1,0])
jhat = array ([0,1])

ustar = 0.14 # en el paper sale que es entre 0.14 y 0.23 
tau_star = 0.067
tau_cr = 0.22*Rp**(-0.6)+0.06*10**(-7*Rp**(-0.6))
ustar = sqrt(tau_star*g*Rp*d)

print "tau_star = ", tau_star
print "tau_cr 0 ", tau_cr
print "tau_star/tau_cr = ", tau_star/tau_cr
print "ustar = ", ustar

def velocity_field(x):
	z = x[1] / d
	if z > 1./30:
		uf =ustar*log(30.*z)/0.41
	else:
		uf = 0
	return array([uf,0])


vfx = velocity_field([0,4*d])[0]
k_penal = 100.*0.5*Cd*rho_agua*A*norm(vfx)**2/(1*_mm)

def fuerzas_hidrodinamicas(x,v,d,area,masa):

	xtop = x + (d/2)*jhat
	xbot = x - (d/2)*jhat
	vf = velocity_field(x + 0*jhat)

	vrelf_top = abs(velocity_field(xtop)[0])
	vrelf_bot = abs(velocity_field(xbot)[0])

	vrel = vf - v

	Cd = 0.47
	fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*area)*vrel

	fL = (0.5*CL*alpha*rho_agua*(vrelf_top - vrelf_bot)*area)*vrel[0]*jhat
	fW = (-masa*g)*jhat

	Fh = fW + fD + fL

	return Fh


def particula(z,t):
	zp = zeros(4*Nparticulas)

	for i in range(Nparticulas):
		di = d
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]


		Fi = fuerzas_hidrodinamicas(xi,vi,di,A,m)
		x_mod_d = (xi[0] % d) - d/2
		y = sqrt((d/2)**2 - x_mod_d**2)

		
		if xi[1] < 0:
			Fi[1] += -k_penal*xi[1]

		elif xi[1] <= y:
			Fi[1] += k_penal*xi[1]

		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fi/m

		for i in range(Nparticulas):
			xi = z[4*i:(4*i+2)]
			for j in  range(Nparticulas):
				if i > j:
					xj = z[4*j:(4*j+2)]
					rij = xj -xi
					if norm(rij) < d:
						delta = d - norm(rij)
						nij = rij/norm(rij)
						Fj = k_penal*delta*nij
						Fi = -k_penal*delta*nij
						zp[4*i+2:(4*i+4)] += Fi/m
						zp[4*j+2:(4*j+4)] += Fj/m
	
	return zp


z0 = zeros(4*Nparticulas)
z0[0::4] = x0
z0[1::4] = y0
z0[2::4] = vx0
z0[3::4] = vy0

print "integrando"
z = odeint(particula, z0, t)
print "Finalizado"


fig = figure()

ax = gca() # esto es para la linea de suelo

for i in range(Nparticulas):
	xi = z[:,4*i]
	yi = z[:,4*i+1]
	col = rand(4)
	plot(xi,yi,"--.", color = col)


ax.axhline(d/2,color = "k", linestyle = "--")



#plot(x, y)

tiempoFinal = time()

tiempoTotal = tiempoFinal - tiempoInicial
print tiempoTotal
"numero particulas = ", Nparticulas
#axis("equal")
show()
