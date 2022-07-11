# PDE-solver-shallow-water-equations
Numerical algorithms that solve shallow water PDEs on a 2D plane. This program uses the finite difference method. Shallow water equations are PDEs that describe the dynamics of waves on the water surface.

https://user-images.githubusercontent.com/63879978/178305819-f8dfa42c-f4fb-4272-8cbd-c6d2550b7257.mp4

## Shallow water equations

The shallow water PDEs are the special cases of the Navier-Stokes equations, whose vertical depth is much smaller than the horizontal scales. The simplest linearized shallow water equations (ignoring the Coriolis force) read

$$
\frac{\partial h}{\partial t} + H (\nabla \cdot \mathbf v) = 0
$$

$$
\frac{\partial \mathbf v}{\partial t} = - g \nabla h - b\mathbf v
$$

## The finite difference method

