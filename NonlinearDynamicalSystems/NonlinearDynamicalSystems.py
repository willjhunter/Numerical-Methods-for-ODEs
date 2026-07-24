import time
import matplotlib.pylab as plt 
import numpy as np 
from scipy.integrate import solve_ivp

plt.close('all')

mu = 10
x0 = 2
y0 = 2/3
initial_conditions = [x0, y0]


def VanDerPol_Equation(t,z):
    x,v = z
    xdot = v
    vdot = mu * (1 - x**2) * v - x
    
    return (xdot, vdot)

def VanDerPol_LienardsTransformation(t,z):
    x,y_L = z
    F = (1/3 * (x**3)) - x
    xdot = mu * (y_L - F)
    y_Ldot = (-1/mu) * x
    
    return (xdot, y_Ldot) 

sol1 = solve_ivp(
    VanDerPol_Equation,
    [0,40],
    initial_conditions,
    t_eval=np.linspace(0,40,3000),
    method='Radau'
)

sol2 = solve_ivp(
    VanDerPol_Equation, 
    [-2,2],
    initial_conditions,
    method='Radau',
    t_eval=np.linspace(-2,2,300),
    dense_output=True
)



x = sol2.t
nullcline = x / ( (mu) * (1-x**2) )

plt.plot(sol1.t, sol1.y[0], label='x(t)')
plt.plot(sol1.t, sol1.y[1], label='y(t)')
plt.xlabel('t')
plt.legend()
plt.show()

plt.plot(sol1.y[0], sol1.y[1])
plt.plot(x, nullcline, label='Nullcline')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"Mu = {mu}")
plt.legend()
plt.show()

sol3 = solve_ivp(
    VanDerPol_LienardsTransformation,
    [0, 40],
    initial_conditions,
    method='Radau',
    t_eval=np.linspace(0,40,300)
)

x = np.linspace(-5,5,300)
nullcline = (1/3 * (x**3)) - x

plt.plot(sol3.y[0], sol3.y[1])
plt.plot(x, nullcline, label='Nullcline')
plt.xlabel('x(t)')
plt.ylabel('y_L(t)')
plt.title(f"Phase Plane under the Lienard Transformation ")
plt.legend()
plt.show()
