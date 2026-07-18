import numpy as np 
import math
import matplotlib.pyplot as plt 

plt.close('all')
# This initial y value is assuming(which we do) that we know the exact solution to the diffential equation
y0 = np.exp(-5) / (1 + np.exp(-5))
t0 = -5
h = 1
t_end = 5
C = (y0 * np.exp(-t0)) / (1-y0)


def function(t,y):
    return y * (1 - y)

def euler_midpoint(f, y0, t0, h, num_steps):
    y_approx = [y0]
    t_approx = [t0]
    
    for j in range(num_steps):
        midpoint_slope = f((t0 + h/2), (y0 + (h/2) * f(t0,y0)))
        y1 = y0 + h * midpoint_slope
        t1 = t0 + h
        t0 = t1
        y0 = y1
        
        y_approx.append(y0)
        t_approx.append(t0)
        
    y_approx = np.array(y_approx)
    t_approx = np.array(t_approx)
    
    return t_approx, y_approx

h_values = [h]
for j in range(8):
    h = h/2
    h_values.append(h)

def runge_kutta(f, y0, t0, h, num_steps):
    t = [t0]
    y = [y0]
    
    for j in range(num_steps):
        k1 = h * f(t0,y0)
        k2 = h * f((t0 + h/2), (y0 + k1/2))
        k3 = h * f((t0 + h/2), (y0 + k2/2))
        k4 = h * f((t0 + h), (y0 + k3))
        
        y1 = y0 + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t1 = t0 + h
        
        t0 = t1
        y0 = y1
        
        t.append(t0)
        y.append(y0)
    
    t = np.array(t)
    y = np.array(y)
    
    return t, y

errors_RK4 = []
errors_midpoint_euler = []
for h in h_values:
    num_steps = round((t_end - t0) / h)
    t_approx1, y_approx1 = euler_midpoint(
        function,
        y0,
        t0,
        h,
        num_steps
        )
    y_exact = (C * np.exp(t_approx1)) / (1 + C * np.exp(t_approx1))
    error1 = np.abs((y_exact - y_approx1))
    error1 = np.max(error1)
    # h = round(float(h), 3)
    errors_midpoint_euler.append((h,error1))
    
    t_approx2, y_approx2 = runge_kutta(
        function, 
        y0,
        t0,
        h,
        num_steps
    )
    y_exact = (C * np.exp(t_approx2)) / (1 + C * np.exp(t_approx2))
    error2 = np.abs(y_exact - y_approx2)
    error2 = np.max(error2)
    errors_RK4.append((h,error2))

# Error analysis 
E_h_RK4 = []

for m in errors_RK4:
    E_h_RK4.append(m[1])

print('Convergence rate and observed p value for Runge-Kutta method: ')

for r in range(len(E_h_RK4) - 1):
    error_ratio = E_h_RK4[r] / E_h_RK4[r+1]
    p_obs = math.log(error_ratio, 2)
    print((f'Error Ratio: {error_ratio:.5f}', f"p observed: {p_obs:.5f}"))

E_h_midpoint = []

print('')
print('Convergence rate and observed p value for midpoint Euler method: ')

for m in errors_midpoint_euler:
    E_h_midpoint.append(m[1])

for e in range(len(E_h_midpoint) - 1):
    error_ratio = E_h_midpoint[e] / E_h_midpoint[e+1]
    p_obs = math.log(error_ratio, 2)
    print((f'Error Ratio: {error_ratio:.5f}', f"p observed: {p_obs:.5f}"))


log_h = []
for q in h_values:
    logh = math.log(q)
    log_h.append(logh)

log_error_RK4 = []
for l in errors_RK4:
    logError = math.log(l[1])
    log_error_RK4.append(logError)

log_error_midpoint = []
for q in E_h_midpoint:
    logErrorMidpoint = math.log(q)
    log_error_midpoint.append(logErrorMidpoint)

x = np.linspace(np.min(log_h),np.max(log_h),15)
b_rk4 = math.log(E_h_RK4[2]) - 4 * math.log(h_values[2])
y_rk4 = 4*x + b_rk4


b_midpoint = math.log(E_h_midpoint[2]) - 2 * math.log(h_values[2])
y_midpoint = 2*x + b_midpoint

plt.plot(log_h, log_error_midpoint, label='Explicit Midpoint Error')
plt.plot(log_h,log_error_RK4, label='RK4 Error')
plt.plot(x,y_rk4, label='Reference Line 1: m = 4')
plt.plot(x, y_midpoint, label='Reference Line 2: m = 2')
plt.xlabel('log(h)')
plt.ylabel('log(E(h))')
plt.title('Log-Log Error Plot for RK4 and Explicit Midpoint Error')
plt.legend()
plt.show()

