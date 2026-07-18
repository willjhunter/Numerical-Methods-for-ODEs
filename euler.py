import numpy as np 
import math 
import matplotlib.pyplot as plt 

plt.close('all')

def exponential_decay(t, y):
    return -k * y

def euler(f, y0, t0, h, num_steps):
    y_approx = [y0]
    t_approx = [t0]
    
    for j in range(num_steps):
        slope = f(t0, y0)
        y1 = y0 + h * slope
        t1 = t0 + h
        t0 = t1
        y0 = y1
        
        y_approx.append(y0)
        t_approx.append(t0)
        
    y_approx = np.array(y_approx)
    t_approx = np.array(t_approx)
    
    return t_approx, y_approx

# Initial values 
k = 1
y0 = 1
t0 = 0
t_end = 1

# Setting up the h values to see the convergence rate
h = 1 
h_values = [h]
for j in range(10):
    h = h/2
    h_values.append(h)


errors = []
for h in h_values:
    num_steps = round((t_end - t0) / h)
    t_approx, y_approx = euler(
        exponential_decay,
        y0,
        t0,
        h,
        num_steps
        )
    y_exact = y0 * np.exp(-k * t_approx)
    error = np.abs((y_exact - y_approx))
    error = np.max(error)
    h = round(float(h), 3)
    errors.append((h,error))

E_h = []

for m in errors:
    E_h.append(m[1])

for e in range(len(E_h) - 1):
    error_ratio = E_h[e] / E_h[e+1]
    p_obs = math.log(error_ratio, 2)
    print((f'Error Ratio: {error_ratio:.5f}', f"p observed: {p_obs:.5f}"))

# plt.plot(t_approx, y_approx, label='Approximated Function')
# plt.plot(t_approx, y_exact, label='Exact solution')
# plt.xlabel('time')
# plt.ylabel('y')
# plt.title('Approximated and Exact Solution to a differential equation')
# plt.legend()
# plt.show()
