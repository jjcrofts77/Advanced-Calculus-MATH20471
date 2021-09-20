#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter3/DerivationHeat.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # 3.1 Derivation in One Space Dimension (optional)
# 
# Our derivation will build upon the following model assumptions:
# 
# 1. Heat flows in the direction of decreasing temperature.
# 2. Heat flow is proportional to the temperature gradient (*Fourier's law*).
# 3. No heat is generated or lost by chemical or electrical processes *energy conservation*).
#   
# 
# Under the above conditions we have that, given an arbitrary volume $V$, the heat crossing the boundary will equate to the change of heat within the solid, which results in the following equation
# 
# $$
#  \int_V{\rho d\frac{\partial\theta}{\partial t}\mathrm{d}V} = \int_S{k\nabla\theta\cdot\mathrm{d}\mathbf{S}}.
# $$
# 
# Here $\mathrm{d}\mathbf{S}=\mathbf{n}\mathrm{d}S$ were $\mathbf{n}$ is the unit outward normal to the surface $S$ of $V$ and $\mathrm{d}S$ is a surface element, $\theta$ is the temperature, $k$ the thermal conductivity, $\rho$ the density and $d$ the specific heat. Recall that given a scalar function $u(x,y,z)$
# 
# $$
#  \nabla u = \left[\frac{\partial u}{\partial x}, \frac{\partial u}{\partial y},
# \frac{\partial u}{\partial z}\right],
# $$
# 
# is the gradient vector.
# 
# The integral over the surface $S$ can be converted to a volume integral by the *divergence theorem* to give
# 
# $$
#   \int_V{\rho d\frac{\partial\theta}{\partial t}\mathrm{d}V} =
# \int_V{\nabla\cdot(k\nabla\theta) \mathrm{d}V}.
# $$
# 
# However, this equation is valid for an arbitrary volume $V$ and therefore the integrands themselves must be equal
# 
# $$
#  \rho d\frac{\partial\theta}{\partial t} = k\nabla^2\theta.
# $$
# 
# Note here we have assumed that $k$ is time-independent, i.e., a constant. Often we will group the constants together as $\kappa = k/\rho{d}$ as in the $1$-d example below
# 
# $$
#  \frac{\partial\theta}{\partial t} = \kappa\frac{\partial^2\theta}{\partial x^2}.
# $$
# 
# 

# In[ ]:




