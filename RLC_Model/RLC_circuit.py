import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp

np.set_printoptions(precision=4, suppress=True)

# Fixed values 
R = 6
L = 1
C = 0.005
V0 = 8
initial_charge = 1
initial_current = 0

# Setting up parameters for the solve_ivp solver
y0 = np.array([initial_charge, initial_current])
t_span = [0,30]
t_eval = np.linspace(0, 4, 400)
t_steady = np.linspace(3, 30, 700)

# Defining the model 
def RLC_function(t,z):
    current_q, current_i = z
    
    voltage_source_function = V0 * np.cos(omega * t)
    
    dqdt = current_i
    didt = 1/L * (voltage_source_function - (R * current_i) - ((1/C) * current_q))
    
    return [dqdt, didt]

freq_response_numerical = []
freq_response_theoretical = []
omega_list = np.linspace(1, 30, 700)
errors = []


for omega in omega_list:
    sol1 = solve_ivp(
        RLC_function,
        t_span,
        y0,
        t_eval=t_steady,
        dense_output=True
    )
    inductive_resistance = omega * L
    capacitive_reactance = 1 / (omega * C)
    I_theoretical = V0 / np.sqrt(R**2 + ((inductive_resistance - capacitive_reactance)**2))
    
    i_max = np.max(sol1.y[1])
    i_min = np.min(sol1.y[1])
    I_numerical = (i_max - i_min) / 2
    error = np.abs(I_theoretical - I_numerical)
    
    errors.append((omega, error))
    freq_response_numerical.append((omega, I_numerical))
    freq_response_theoretical.append((omega, I_theoretical))

omega0, max_amplitude = max(freq_response_numerical, key=lambda pair: pair[1])
print(f'Approximate resonant frequency: {omega0}')
print(f'Approximate peak amplitude: {max_amplitude}')

# Seperating the tuple components when plotting 
omega_numerical = [pair[0] for pair in freq_response_numerical]
amplitude_numerical = [pair[1] for pair in freq_response_numerical]

omega_theoretical = [pair[0] for pair in freq_response_theoretical]
amplitude_theoretical = [pair[1] for pair in freq_response_theoretical]

plt.plot(omega_numerical, amplitude_numerical, label='Numerical')
plt.plot(omega_theoretical, amplitude_theoretical, label='Theoretical')
plt.scatter(omega0, max_amplitude)
plt.annotate(
    f"Resonant Frequency: {omega0:.3f}\nPeak Amplitude: {max_amplitude:.3f}",
    xy=(omega0, max_amplitude),
    xytext=(20, -35),
    textcoords='offset points',
    arrowprops={'arrowstyle': '->'},
    ha='left',
    bbox={'boxstyle': 'round', "facecolor": "white", "alpha": 0.8}
)
plt.xlabel('Forcing Frequency')
plt.ylabel('Amplitude')
plt.title('Frequency Response Curves: Theoretical and Numerical')
plt.legend()
plt.show()


omega = omega0
sol2 = solve_ivp(
    RLC_function,
    [0,4],
    y0,
    t_eval=np.linspace(0,4,300)
)

plt.plot(sol2.t, sol2.y[0], label = 'q(t)')
plt.plot(sol2.t, sol2.y[1], label='i(t)')
plt.xlabel('time')
plt.ylabel('q(t) & i(t)')
plt.title(f'RLC Circuit at Resonant Frequency: {omega:.4f}')
plt.legend()
plt.show()

print(max(errors, key=lambda pair: pair[1]))