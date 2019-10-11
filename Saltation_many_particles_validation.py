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
d = 15.*_mm

rho_agua = 1000.*_kg/(_m**3)                   # diametro de la particula
rho_particula = 2650*_kg/(_m**3)      # densidad de la particula, considerando que sea arena 

dt = 0.001*_s    # paso de tiempo 
tmax = 0.5*_s    # tiempo maximo de simulacion
ti = 0.*_s     # tiempo actual

nparticulas = 5


x0 = 10*d*rand(nparticulas)
y0 = 3*d*rand(nparticulas) + d

vx0 = rand(nparticulas)/2
vy0 = rand(nparticulas)/2


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
def velocitiy_field(x):
	z = x[1] / d
	if z > 1./30:
		uf =ustar*log(30.*z)/0.41
	else:
		uf = 0
	return array([uf,0])


vfx = velocitiy_field([0,4*d])[0]
k_penal = 100.*0.5*Cd*rho_agua*A*norm(vfx)**2/(1*_mm) 


def particula(z,t):
	zp = zeros(4*nparticulas)

	for i in range(nparticulas):
		di = d
		xi = z[4*i:(4*i+2)]
		vi = z[4*i+2:(4*i+4)]

		vf = velocitiy_field(xi)
		vf_top = norm(velocitiy_field(xi + (di/2)*jhat))
		vf_bot = norm(velocitiy_field(xi - (di/2)*jhat))
		vrel = vf - vi
		fD = (0.5*Cd*alpha*rho_agua*norm(vrel)*A)*vrel 
		fL = (0.5*CL*alpha*rho_agua*(vf_top**2 -vf_bot**2)*A)*jhat # en esta linea falta codigo
		
		Fi = W + fD + fL

		if xi[1] < 0:
			Fi += -k_penal*xi[1]

		zp[4*i:(4*i+2)] = vi
		zp[4*i+2:(4*i+4)] = Fi/m

	for i in range(nparticulas):
		xi = z[4*i:(4*i+2)]
		for j in  range(nparticulas):
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


z0 = zeros(4*nparticulas)
z0[0::4] = x0
z0[1::4] = y0
z0[2::4] = vx0
z0[3::4] = vy0

print "integrando"
z = odeint(particula, z0, t)
print "Finalizado"


fig = figure()

ax = gca() # esto es para la linea de suelo

for i in range(nparticulas):
	xi = z[:,4*i]
	yi = z[:,4*i+1]
	col = rand(4)
	plot(xi,yi,"--.", color = col)


ax.axhline(d/2,color = "k", linestyle = "--")


d = 0.15e-3
x = linspace(0, 20*d,4000)
x_mod_d = (x % d) - d/2
y = sqrt((d/2)**2 - x_mod_d**2)

plot(x, y)
axis("equal")

tiempoFinal = time()

tiempoTotal = tiempoFinal - tiempoInicial
print tiempoTotal
show()

