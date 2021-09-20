#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter2/Chapter2Intro.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Chapter 2 Fourier Series
# 
# In the following chapters, we will look at methods for solving the PDEs described in Chapter 1. In order to incorporate general initial or boundary conditions into our solutions, it will be necessary to have some understanding of *Fourier series*.
# 
# For example, we can see that the series 
# 
# $$
#   y(x,t) = \sum_{n=1}^\infty \sin\left(\frac{n\pi x}{L}\right)\left[A_n\cos\left(\frac{n\pi c t}{L}\right) +B_n\sin\left(\frac{n\pi ct}{L}\right)\right], 
# $$ (wavesol)
# 
# is a solution of the wave equation
# 
# $$
#  \frac{\partial^2 y}{\partial t^2} = c^2\frac{\partial^2 y}{\partial x^2},\quad x\in[0, L], ~t\geq 0,
# $$
# 
# which satisfies the boundary conditions
# 
# $$
# y(0,t) = 0 = y(L,t).
# $$
# 
# We may view $y(x,t)$ as the solution of the problem of modelling a vibrating string of length $L$ pinned at both ends, *e.g.* a guitar string.
# 
# We would like to find a solution with initial conditions 
# 
# $$
#  y(x,0) = \alpha\sin\left(\frac{\pi x}{L}\right), \quad \frac{\partial y}{\partial t}(x,0)=0,
# $$
# 
# and we do this by calculating $A_n$ and $B_n$ as follows: from {eq}`wavesol` we have 
# 
# $$
#  y(x,0) = \sum_{n=1}^\infty A_n\sin\left(\frac{n \pi x}{L}\right),
# $$
# 
# and
# 
# $$
#  \frac{\partial y}{\partial t}(x,0) = \sum_{n=1}^\infty B_n \left(\frac{n\pi c}{L}\right)\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# Hence, we want $A_n, B_n$ such that
# 
# $$
#  \alpha\sin\left(\frac{\pi x}{L}\right) = \sum_{n=1}^\infty A_n\sin\left(\frac{n \pi x}{L}\right), \qquad 0 = \sum_{n=1}^\infty B_n \left(\frac{n\pi c}{L}\right)\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# By inspection we see that $A_1=\alpha$, $A_n = 0$ for $n\neq 1$ and $B_n=0 ~\forall n$. Thus, for these initial conditions, the solution is 
# 
# $$
#  y(x,t) = \alpha\sin\left(\frac{\pi x}{L}\right)\cos\left(\frac{\pi c t}{L}\right).
# $$
# 
# If we would like to take more general initial conditions
# 
# $$
#  y(x,0) = f(x), \quad \frac{\partial y}{\partial t}(x,0) = g(x),
# $$
# 
# we need to find $\{A_n, B_n\}$ such that
# 
# $$
# f(x) = \sum_{n=1}^\infty A_n\sin\left(\frac{n \pi x}{L}\right), \qquad g(x) = \sum_{n=1}^\infty B_n \left(\frac{n\pi c}{L}\right)\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# These are known as the *Fourier sine series* of the functions $f, g$.

# In[ ]:




