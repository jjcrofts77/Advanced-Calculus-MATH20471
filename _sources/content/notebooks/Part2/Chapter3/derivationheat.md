# 3.1 Derivation in one space dimension (optional)

In this chapter we shall look at the heat equation in one space dimension, learning a method for its derivation, and 
some techniques for solving.

Our derivation will build upon the following model assumptions:

1. Heat flows in the direction of decreasing temperature.
2. Heat flow is proportional to the temperature gradient (\emph{Fourier's law}).
3. No heat is generated or lost by chemical or electrical processes (\emph{energy conservation}).

Under the above conditions we have that, given an arbitrary volume $V$, the heat crossing the boundary will equate to the change of heat within the solid, which results in the following equation

$$
 \int_V{\rho d\frac{\partial\theta}{\partial t}\mathrm{d}V} = \int_S{k\nabla\theta\cdot\mathrm{d}\mathbf{S}}.
$$

Here $\mathrm{d}\mathbf{S}=\mathbf{n}\mathrm{d}S$ were $\mathbf{n}$ is the unit outward normal to the surface $S$ of $V$ and $\mathrm{d}S$ is a surface element, $\theta$ is the
temperature, $k$ the thermal conductivity, $\rho$ the density and $d$ the
specific heat. Recall that given a scalar function $u(x,y,z)$

$$
 \nabla u = \left[\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y},
\frac{\partial u}{\partial z}\right],
$$

is the gradient vector.