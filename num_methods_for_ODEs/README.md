# Explicit Midpoint Euler vs fourth-order Runge-Kutta method 

## Project Overview
The differential equation that this project studies is the equation: dy/dt = y(1-y).
The goal of this project was to develop a better understanding of numerical methods for solving ordinary differential equations as well as understanding the global error associated with both methods. 

The two numerical methods I decided to study were the explicit midpoint Euler method and the fourth-order Runge-Kutta method. 

In order to compare their convergence rates, I looked at the error ratio produced by both methods and noticed that these values seem to converge to a specific value. For explicit Euler, that value was 2 and for Runge-Kutta, that value was 4. 

## Mathematical Model 
The initial value problem is the ordinary differential equation 
dy/dt = y(1-y) with t_0 = -5 and y_0 = y(-5). The exact solution to this differential equation has a general form of: 
y = (Ce^t) / (1 + Ce^t) where C is an arbitary constant found by solving for C using the exact solution and initial values. 

I chose the intial time value t_0 to be -5 because the exact solution does take on values when negative values are used as inputs. The function quickly approaches 0 as t approaches -inf and as a result when t = -5, y is a very small number. That being said, it is important to note that I chose the intial value already knowing what the exact solution to the differential equation was so that the function can behave 'nicely'. In a situation where the exact function is unknown or impossible to derive analytically, it is possible to test different values of t0 and y0 to observe behavior consistent with what I found. 

I decided to work on the interval [-5,5] for this problem.  

## Numerical Methods
The explicit midpoint Euler method is defined as:
y_(n+1) = y_n + hf( (t_n + h/2) , (y_n + h/2f(t_n,y_n)) )
This numerical approximation method approximates slope of a function at the midpoint between t_n and t_(n+1)





