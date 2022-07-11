# PDE-solver-shallow-water-equations
Numerical algorithms that solve shallow water PDEs on a 2D plane. This program uses the finite difference method. Shallow water equations are PDEs that describe the dynamics of waves on the water surface.

https://user-images.githubusercontent.com/63879978/178305819-f8dfa42c-f4fb-4272-8cbd-c6d2550b7257.mp4

## Shallow water equations

The shallow water PDEs are the special cases of the Navier-Stokes equations, whose vertical depth is much smaller than the horizontal scales. The simplest linearized shallow water equations (ignoring the Coriolis force and dissipative forces) read

$$
\frac{\partial h}{\partial t} + H (\nabla \cdot \mathbf v) = 0
$$

$$
\frac{\partial \mathbf v}{\partial t} = - g \nabla h - b\mathbf v
$$

where $g$ is the acceleration due to gravity, and $b$ is the friction coefficient.

## Finite difference method

The finite difference method discretizes the solution into a (in this case) 2D meshgrid $h(x, y) = h_{i,j}$. The spatial differential operations are approximated by local neighboring points

$$
\frac{\partial h}{\partial x} \approx \frac{h_{i+1, j} - h_{i-1, j}}{2\Delta x}
$$

$$
\frac{\partial^2 h}{\partial x^2} \approx \frac{h_{i+1, j} + h_{i-1, j} - 2h_{i, j}}{\Delta x^2}
$$

In time, the solution is evolved using Euler's method:

$$
h(x, y, t+\Delta t) \approx h(x, y, t) + \frac{\partial h}{\partial t} \Delta t
$$
