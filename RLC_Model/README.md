# RLC Circuit Model
## Project Overview
This project models a circuit consisting of a resistor, inductor, and capacitor otherwise known as a RLC circuit. The goal of this project was to simulate a driven RLC circuit and compare the numerical frequency response with the theoretical response. 
## Mathematical Model 
The differential equation that governs this circuit is: 
Lq'' + Rq' + (1/C)q = V(t). Here R represents a fixed resistor value, L represents a fixed inductance value, and C represents a fixed capacitance value. V is the voltage source function and represents some externtal voltage source being applied to the circuit. q(t) and i(t) represent the charge and current, respectively, at any given time t. 
This model makes a couple of assumptions. The first being that we assume that each component behaves ideally. Secondly, we assume that the system exhibits lumped-circuit behavior meaning that each component can be represented by a single number. Next, we assume that there are no parasitic effects such as resistors having a tiny inductance, capacitors having small internal resistance and inducatance, and inductors having winding resistance and stray capacitance. Finally, the differential equation was derived assiming that Kirchoff's rule hold exactly. 
## Numerical Approach
In order to apply the solve_ivp solver to numerically approximate a solution to the differential equation, I had to convert the original differential equation into a system of differential equations. Using the fact that the charge and current through the system are enough to describe the system adequately, I rewrote the differential equation into the system of equations:
dq/dt = i 
didt = 1/L * (voltage_source_function - (R * i) - ((1/C) * q))
The steady-state amplitude was estimated using the fact that steady-state charge and current are approximately sinusoidal and so we can estimate the amplitude using the approximation: 
I_estimated = (i_max - i_min) / 2
where i_max and i_min represents the maximum and minimum current values, respectively, within a selected measurement window. In order to get an error between the theoretical and numerical solutions to the differential equation, I had to make sure that I only used values where the transient-state of the approximated solution died off. 
## Results
The resonant frequency was predicted theoretically by using the equation: 
I_theoretical = V0 / np.sqrt(R**2 + ((inductive_resistance - capacitive_reactance)**2))
Inductive resistance is represented by the quantity omega*L and the capacitive reactance is represented by the quanity 1/(omega*C). omega represents the frequency of the forcing function. Then the resonant frequency can be calculated by setting the inductive resistance and capacitive reactance equal to each other and solving for omega. Doing so, we see that the resonant frequency is 
1/sqrt(L*C)
The numerical frequency-response curve matched the analytical curve almost exactly, with a maximum error observed when omega is 20.33 rad/s which is associated to an error of 0.0213. Increasing the sampling density, reduced the error and visually, the numerical curve approached the theoretical curve significantly. Changing the values for the resistor, inductor, or capacitor changed the curve in various ways. The first being that the resonant frequency value changed, leading to different peak amplitude values being observed. Second, the point at which most of the transient values died off was shifted to the left or right.
The numerical and theoretical frequency-response curves where R = 6, L = 1, C = 0.005, V(t) = 8cos(omega*t) are shown below. 
![Numerical and theoretical frequency-response curves](images/Frequency_Response_Curves.png)
## Reflection & Limitations
The most important numerical challenges was making sure that when plotting the frequency-response curves, I had to make sure that I only included steady-state values. Meaning, the interval of time that I ran the solver for, had to start at a time where most of the transient activity died off. A limitiation of the current model is that if one wanted to simulate realistic circuit component values where capacitance and inductive are very small, the differential equation becomes stiff making the default RK45 method to approximate the solution an ineffective method and one needs to use a method that can handle stiff differential equations. 

