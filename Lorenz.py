import numpy as np 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

plt.close('all')


def LorenzFunction(t,z):
    x,y,w = z

    P = 10
    b = 8/3
    r = 28
    
    xdot = -P*x + P*y
    ydot = -y + r*x - x*w
    wdot = -b*w + x*y

    return (xdot,ydot,wdot)

sol = solve_ivp(
    LorenzFunction,
    [0,110],
    [1,1,1],
    method='Radau',
    t_eval=np.linspace(100,110,1000)
)

# plt.plot(sol.t, sol.y[0], label='x(t)')
# plt.legend()
# plt.show()

# plt.plot(sol.t, sol.y[1], label='y(t)')
# plt.legend()
# plt.show()

plt.plot(sol.t, sol.y[2], label='z(t)')
plt.legend()
plt.show()
