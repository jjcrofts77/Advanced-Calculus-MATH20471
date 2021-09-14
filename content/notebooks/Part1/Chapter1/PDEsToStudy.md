# 1.3 The equations we shall study

In general the solution of a partial differential equation is frequently difficult 
to find; however, the method of *separation of variables*, which we shall study in 
the chapters to come, provides a useful technique for determining solutions to a large 
class of linear partial differential equations. There are fundamentally three types of 
partial differential equations -- those that govern diffusion processes, those that 
govern wave propagation, and those that model equilibrium processes. These types are
called *parabolic*, *hyperbolic* and *elliptic*, respectively. In this 
course we we study prototypical examples of each of the three classes of linear 
second-order PDEs as well as considering their applications throughout the physical 
sciences. 


## The wave equation (hyperbolic)
Here we seek a function $y(x,t)$ such that

$$
 \frac{\partial^2 y}{\partial t^2} = c^2\frac{\partial^2 y}{\partial x^2},
$$

where, for example, $y(x,t)$ is the transverse displacement of a stretched string at position $x$ and time
$t$, and $c$ is a positive constant called the *wave speed*.

## The heat equation (parabolic)
Also known as the *diffusion equation*, we will find $T(x,t)$ such that

$$
 \frac{\partial T}{\partial t} = \kappa\frac{\partial^2T}{\partial x^2},
 \label{eqn:heat}
$$

where, for example, $T(x,t)$ is a temperature at position $x$ and time $t$, and $\kappa$ is a positive 
constant called the *thermal diffusivity*.

## Laplace's equation (elliptic)
In this case the problem is to find $T(x,y)$ such that

$$
 \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0,
$$

where, for example, $T(x,y)$ may be the temperature and $x$ and $y$ are Cartesian coordinates in the plane. In this case, *Laplace's equation* models a two-dimensional 
system at *steady state* in time: in three space-dimensions the temperature $T(x,y,z,t)$ satisfies the heat equation 

$$
 \frac{\partial T}{\partial t} =  \kappa\left(\frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2}\right).
 \label{eqn3Dheat}
$$

Note that the equation above reduces to heat equation if $T$ is independent of $y$ and $z$. If the temperature field is \emph{static}, $T$ is independent 
of time, and is a solution of Laplace's equation in $\mathbb{R}^3$,

$$
 \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} + \frac{\partial^2 T}{\partial z^2} = 0,
$$

and, in the special case in which $T$ is also independent of $z$, of Laplace's equation in $\mathbb{R}^2$

$$
 \frac{\partial^2 T}{\partial x^2} + \frac{\partial^2 T}{\partial y^2} = 0.
$$