#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter3/IBVPHeat.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # 3.3 Initial and Boundary Value Problem
# 
# We now consider finding the solution of the heat equation 
# 
# $$
#  \frac{\partial T}{\partial t} = \kappa\frac{\partial^2 T}{\partial x^2}, \quad 0<x<L, t>0,
# $$
# 
# subject to the initial condition 
# 
# $$
#  T(x,0) = f(x), \quad 0<x<L,
# $$
# 
# and the boundary conditions
# 
# $$
#  T(0,t) = 0 \text{ and } T(L,t)=0 \text{ for } t>0.
# $$
# 
# In view of our proceeding discussion we look for a solution as an infinite sum
# 
# $$
#  T(x,t) = \sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right)e^{-n^2\pi^2\kappa t/L^2}.
# $$ (heatsol)
# 
# <br>
# 
# ```{prf:example} 
# :label: example23
# 
# Solve the IBVP for the case
# 
# $$
#  T(x,0) = \sin\left(\frac{\pi x}{L}\right) + \frac{1}{2}\sin\left(\frac{2\pi x}{L}\right) = f(x), \quad 0 \leq x \leq L.
# $$
# 
# From equation {eq}`heatsol` we see that
# 
# $$
#  T(x,0) = \sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# Comparing terms we see that $a_1=1, a_2=1/2$ and $a_n=0$ $(n\geq 3)$ so that the solution is
# 
# $$
#  T(x,t) = \sin\left(\frac{\pi x}{L}\right)e^{-\pi^2\kappa t/L^2} +\frac{1}{2}\sin\left(\frac{2\pi x}{L}\right)e^{-4\pi^2 \kappa t/L^2}.
# $$
# ```
# 
# The initial condition and solution is shown in the figures below.
# 
# <br>
# 
# `````{grid}
# :gutter: 2
# 
# ````{grid-item-card}
# ```{figure} ../../../images/HeatICExample31.png
# Initial condition
# ```
# ````
# 
# ````{grid-item-card}
# ```{figure} ../../../images/HeatExample31.png
# Solution of Example 3.3.1 with $L = \pi$ and $\kappa = 1$
# ```
# ````
# 
# `````
# 
# Below we further illustrate how the tempertaure profile of the problem in {prf:ref}`example23` behaves as a function of time. Click on the tab to view the python code that creates the movie.

# In[1]:


# plot an animation of the solution T(x,t) with L = pi and kappa = 0.25
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()
plt.close()


ax.set_xlim(( 0, np.pi))
ax.set_ylim((0, 1.35))
ax.set_xlabel('x',size=12)
ax.set_ylabel('T(x,t)',size=12)
ax.set_title('Temp profile as a function of time for Ex 3.3.1',weight='bold',size=16)


line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])    
    return (line,)

# animation function. This is called sequentially  
def animate(i):
    L = np.pi
    kappa = 0.1
    x = np.linspace(0, np.pi, 1000)
    y = np.sin(np.pi*x/L)*np.exp(-np.pi**2*kappa*(0.1*i)/L**2)+0.5*np.sin(2*np.pi*x/L)*np.exp(-4*np.pi**2*kappa*(0.1*i)/L**2)
    line.set_data(x, y)
    return (line,)
  
anim = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=150, interval=50, blit=True)
#anim # uncomment to play animation


# In[2]:


# Note: below is the part which makes it work on Colab
#rc('animation', html='jshtml')
#anim # uncomment to play animation
#anim.save('heateqn.mp4') # uncomment to save animation 
# display video
from IPython.display import HTML

HTML("""
    <video width="700" height="600" controls>
        <source src="../../../../_static/videos/heateqn.mp4" type="video/mp4">
    </video>
""")


# ## Application of Fourier Series
# 
# To solve for general initial conditions, we can use Fourier series to determine the constants $a_n$:
# 
# $$
#  T(x,0) = \sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right),\quad 0\leq x \leq L.
# $$
# 
# The question is now, given $f(x)$, can it be expanded as a Fourier sine series
# 
# $$
#  f(x) = \sum_{n=1}^\infty a_n\sin\left(\frac{n\pi x}{L}\right), \quad 0\leq x\leq L?
# $$
# 
# From the lectures on Fourier series, we know that such an expansion exists if *e.g.* $f(x)$ is piecewise continuously differentiable on $[0, L]$. The coefficients $a_n$ are determined by the orthogonality relations:
# 
# $$
# \int_0^L \sin\left(\frac{n\pi x}{L}\right)\sin\left(\frac{m\pi x}{L}\right)\mathrm{d}x = \begin{cases}0&m\neq n,\\\frac{1}{2}L& m=n.\end{cases}
# $$
# 
# Thus
# 
# $$
#  a_n = \frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x.
# $$
# 
# <br>
# 
# ```{prf:example}  
# :label: example24
# Find the solution of the IBVP when
# 
# $$
#  f(x) = \begin{cases}0&\text{for $0\leq x\leq L_1$ and $L_2\leq x \leq L$,}\\1&\text{for $L_1<x<L_2$.}\end{cases}
# $$
# 
# Here $f(x)$ has the Fourier sine expansion (exercise)
# 
# $$
# f(x) = \frac{2}{\pi}\sum_{n=1}^\infty\frac{1}{n}\left[\cos\left(\frac{n\pi L_1}{L}\right)-\cos\left(\frac{n\pi L_2}{L}\right)\right]\sin\left(\frac{n\pi x}{L}\right),
# $$
# 
# and the solution to the IBVP is
# 
# $$
# T(x,t) = \frac{2}{\pi}\sum_{n=1}^\infty\frac{1}{n}\left[\cos\left(\frac{n\pi L_1}{L}\right)-\cos\left(\frac{n\pi L_2}{L}\right)\right]\sin\left(\frac{n\pi x}{L}\right)e^{-n^2\pi^2\kappa t/L^2}.
# $$
# ```
# 
# The initial condition and solution is shown in the figures below.
# 
# 
# `````{grid}
# :gutter: 2
# 
# ````{grid-item-card}
# ```{figure} ../../../images/HeatICExample32.png
# Initial condition (FS approximation with $n=1000$ terms)
# ```
# ````
# 
# ````{grid-item-card}
# ```{figure} ../../../images/HeatExample32.png
# Solution of Example 3.3.2 with $L = \pi$ and $\kappa = 1$ truncated to $n=1000$ terms
# ```
# ````
# 
# `````
# 
# Notice Gibb's phenomenon is present despite the large number of terms taken in the FS approximation.
