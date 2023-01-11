#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter4/IBVPWave.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # 4.3 Initial and Boundary Value Problem for Finite Strings
# 
# Consider the following IBVP: find $y(x,t)$ such that
# 
# $$
#  \frac{\partial^2 y}{\partial t^2} = c^2\frac{\partial^2 y}{\partial x^2}, \quad \text{for $0<x<L$ and $t>0$},
# $$
# 
# and $y$ satisfies the initial conditions 
# 
# $$
#  y(x,0) = f(x) \text{ and } \frac{\partial y}{\partial t}(x,0) = g(x) \text{ for } 0\leq x\leq L,
# $$ (waveICs3)
# 
# and the boundary conditions
# 
# $$
#  y(0,t) = 0 \text{ and } y(L,t) = 0 \text{ for } t>0,
# $$
# 
# where $f(x)$ and $g(x)$ are known functions. According to {eq}`waveICs3`, the initial tranverse displacement and the initial tranverse velocity are prescribed. If *e.g.*
# 
# $$
#  f(x) = \begin{cases}2hx/L&0\leq x\leq L/2,\\2h(L-x)/L& L/2\leq x\leq L,\end{cases}
# $$ (waveTriIC)
# 
# and $g(x)=0, 0\leq x\leq L$, the mid-point of the string is pulled aside a distance $h$ and the string is released from rest.
# 
# We know that the general solution can be written as in equation {eq}`waveGenSol`, and hence the boundary conditions must satisfy
# 
# $$
#  y(x,0) = \sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right), \quad \frac{\partial y}{\partial t}(x,0) = \sum_{n=1}^\infty \left(\frac{n\pi c}{L}\right)b_n\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# <br>
# 
# ```{prf:example} 
# :label: example26
# 
# Solve the IBVP for the case 
# 
# $$
#  f(x) = A\sin\left(\frac{\pi x}{L}\right)+B\sin\left(\frac{\pi x}{L}\right)\cos\left(\frac{\pi x}{L}\right),\quad g(x)=0.
# $$
# 
# Since
# 
# $$
#  f(x) = A\sin\left(\frac{\pi x}{L}\right)+\frac{1}{2}B\sin\left(\frac{2\pi x}{L}\right),
# $$
# 
# the solution is obtained by taking $a_1=A$, $a_2=B/2$, $a_n=0$ for $n\geq 3$ and $b_n=0$ $\forall n$ to give
# 
# $$
#  y(x,t) = A\sin\left(\frac{\pi x}{L}\right)\cos\left(\frac{\pi c t}{L}\right) + \frac{1}{2}B\sin\left(\frac{2\pi x}{L}\right)\cos\left(\frac{2\pi c t}{L}\right).
# $$
# 
# ```
# 
# ````{panels}
# 
# ```{figure} ../../../images/WaveExample41c1.png
# Solution for Example (4.3.1) with $c = 1$ and $L = \pi$
# ```
# 
# ---
# 
# ```{figure} ../../../images/WaveExample41c2.png
# Solution for Example (4.3.2) with $c = 2$ and $L = \pi$
# ```
# 
# ````
# 
# 
# 
# ```{prf:example} 
# :label: example27
# 
# Solve the IBVP for the case
# 
# $$
#  f(x)=0, \quad g(x) = \sin^3\left(\frac{\pi x}{L}\right).
# $$
# 
# Since (trig identity)
# 
# $$
#  g(x) = \frac{3}{4}\sin\left(\frac{\pi x}{L}\right) -\frac{1}{4}\sin\left(\frac{3\pi x}{L}\right),
# $$
# 
# we take $a_n=0$ $\forall n$ and identify 
# 
# $$
# \left(\frac{\pi c}{L}\right)b_1 = \frac{3}{4}, \quad \left(\frac{2\pi c}{L}\right)b_2=0,\quad \left(\frac{3\pi c}{L}\right)b_3=-\frac{1}{4}, \quad b_n=0 \text{ for } n\geq 4,
# $$
# 
# to arrive at 
# 
# $$
# y(x,t) = \frac{3L}{4\pi c}\sin\left(\frac{\pi x}{L}\right)\sin\left(\frac{\pi c t}{L}\right) - \frac{L}{12\pi c}\sin\left(\frac{3\pi x}{L}\right)\sin\left(\frac{3\pi c t}{L}\right).
# $$
# 
# ```
# 
# ````{panels}
# 
# ```{figure} ../../../images/WaveExample42c1.png
# Solution for Example (4.3.1) with $c = 1$ and $L = \pi$
# ```
# 
# ---
# 
# ```{figure} ../../../images/WaveExample42c2.png
# Solution for Example (4.3.2) with $c = 2$ and $L = \pi$
# ```
# 
# ````
# 

# In[1]:


# animation of solution of Example 4.3.2 with parameters L = pi and c = 1

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(figsize=(10, 7.5), dpi=80)
plt.close()

# labels
ax.set_xlim(( 0, np.pi))
ax.set_ylim((-1.1, 1.1))
ax.set_xlabel('$x$',size=16)
ax.set_ylabel('$y(x,t)$',size=16)
ax.set_title('Solution to the above vibrating string problem',weight='bold',size=24)


line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])    
    return (line,)

# animation function. This is called sequentially  
def animate(i):
    L = np.pi    
    c = 1
    x = np.linspace(0, np.pi, 1000)
    y = 3*L*np.sin(np.pi*x/L)*np.sin(np.pi*c*0.2*i/L)/(4*np.pi*c) - L*np.sin(3*np.pi*x/L)*np.sin(3*np.pi*c*0.2*i/L)/(12*np.pi*c)        
    line.set_data(x, y)
    return (line,)
  
anim = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=150, blit=True)

# to run animation remove comments below
#rc('animation', html='jshtml')
#anim


# In[2]:


# display video
from IPython.display import HTML

HTML("""
    <video width="700" height="600" controls>
        <source src="../../../../_static/videos/waveeqn432.mp4" type="video/mp4">
    </video>
""")


# ## Application of Fourier Series
# 
# To solve for more general initial conditions, we again look for a solution as a superposition of normal modes:
# 
# $$
#  y(x,t) = \sum_{n=1}^\infty \sin\left(\frac{n\pi x}{L}\right)\left[a_n\cos\left(\frac{n\pi ct}{L}\right) + b_n\sin\left(\frac{n\pi ct}{L}\right)\right],
# $$
# 
# so that we arrive at the problem: given $f(x)$ and $g(x)$ can they be expanded as a Fourier sine series
# 
# $$
# f(x)&=\sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right), \quad 0\leq x\leq L,\\
# g(x)&=\sum_{n=1}^\infty \left(\frac{n\pi c}{L}\right)b_n\sin\left(\frac{n\pi x}{L}\right)?
# $$
# 
# From the lectures on Fourier series we know that such expansions exist if *e.g.* $f$ and $g$ are piecewise continuously differentiable on $[0, L]$. The coefficients are determined by the orthogonality relations
# 
# $$
# \int_0^L \sin\left(\frac{m\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \begin{cases}0& m\neq n,\\\frac{1}{2}L& m=n.\end{cases}
# $$
# 
# Thus 
# 
# $$
#  a_n &= \frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x,\\
#  b_n &= \frac{2}{n\pi c}\int_0^L g(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x.
# $$
# 
# ```{prf:example} guitar
# :label: example28
# 
# For the special case {eq}`waveTriIC`,
# 
# $$
#  a_n &= \frac{2}{L}\cdot\frac{2h}{L}\int_0^{\frac{L}{2}}x\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x +\frac{2}{L}\cdot\frac{2h}{L}\int_{\frac{L}{2}}^L(L-x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x,\\
#  &=\frac{8h}{\pi^2n^2}\sin\left(\frac{n\pi}{2}\right),
# $$
# 
# and 
# 
# $$
#  b_n = \frac{2}{n\pi c}\int_0^L 0\cdot \sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x = 0.
# $$
# 
# Hence the solutions is
# 
# $$
# y(x,t) &= \frac{8h}{\pi^2}\sum_{n=1}^\infty \frac{1}{n^2}\sin\left(\frac{n\pi}{2}\right)\sin\left(\frac{n\pi x}{L}\right)\cos\left(\frac{n\pi c t}{L}\right),\\
# &= \frac{8h}{\pi^2}\left[\frac{1}{1^2}\sin\left(\frac{\pi x}{L}\right)\cos\left(\frac{\pi c t}{L}\right)-\frac{1}{3^2}\sin\left(\frac{3\pi x}{L}\right)\cos\left(\frac{3\pi c t}{L}\right)\right.\\
# &\left. \qquad\qquad +\frac{1}{5^2}\sin\left(\frac{5\pi x}{L}\right)\cos\left(\frac{5\pi c t}{L}\right) - \cdots\right].
# $$
# ```
# 
# ```{figure} ../../../images/GuitarWave.png
# Solution for Example (4.3.1) with $c = 1$ and $L = \pi$
# ```
# 
# 
# ```{prf:example} piano 
# :label: example29
# The initial tranverse displacement is zero and the section $[L_1,L_2]$ is given an initial tranverse velocity $v$. Here $f(x)=0$ for $0\leq x\leq L$, and
# 
# $$
# g(x) = \begin{cases}0& \text{for } 0\leq x< L_1 \text{ and } L_2< x \leq L,\\
# v& \text{for } L_1\leq x\leq L_2.\end{cases}
# $$
# 
# Thus $a_n=0$ and 
# 
# $$
# b_n = \frac{2}{n\pi c}\int_{L_1}^{L_2}v\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \frac{2vL}{n^2\pi^2c}\left[\cos\left(\frac{n\pi L_1}{L}\right)-\cos\left(\frac{n\pi L_2}{L}\right)\right].
# $$
# 
# The tranvserse displacement is 
# 
# $$
#  y(x,t) = \frac{2vL}{\pi^2c}\sum_{n=1}^\infty \frac{1}{n^2}\left[\cos\left(\frac{n\pi L_1}{L}\right)-\cos\left(\frac{n\pi L_2}{L}\right)\right]\sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{n\pi c t}{L}\right).
# $$
# 
# ```
# 
# ```{figure} ../../../images/PianoWave.png
# Solution for Example (4.3.1) with $c = 1$ and $L = \pi$
# ```
