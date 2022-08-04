#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter2/Chapter2Intro.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Chapter 2 Fourier Series
# 
# In the following chapters, we will look at methods for solving the PDEs described in Chapter 1. In order to incorporate general initial or boundary conditions into our solutions, it will be necessary to have some understanding of *Fourier series* (FS).
# 
# To motivate the use of FS we note that the following (pretty horrible looking!) function 
# 
# $$
#   y(x,t) = \sum_{n=1}^\infty \sin\left(\frac{n\pi x}{L}\right)\left[A_n\cos\left(\frac{n\pi c t}{L}\right) +B_n\sin\left(\frac{n\pi ct}{L}\right)\right], 
# $$ (wavesol)
# 
# 
# ````{margin}
# ```{note}
# We shall derive this solution explicitly later on in the course
# ```
# ````
# 
# can be shown to be a solution of the wave equation
# 
# $$
#  \frac{\partial^2 y}{\partial t^2} = c^2\frac{\partial^2 y}{\partial x^2},\quad x\in[0, L], ~t\geq 0,
# $$
# 
# satisfying the boundary conditions
# 
# $$
# y(0,t) = 0 = y(L,t).
# $$
# 
# We may view $y(x,t)$ as the solution of the problem of modelling a vibrating string of length $L$ pinned at both ends, *e.g.* a guitar string.
# 
# Keeping the guitar analogy in mind, suppose that we initially pluck the string into a sinusoidal shape and release it from a fixed position, then we would have initial conditions of the form
# 
# $$
#  y(x,0) = \alpha\sin\left(\frac{\pi x}{L}\right), \quad \frac{\partial y}{\partial t}(x,0)=0.
# $$
# 
# ````{margin}
# ```{note}
# Here $y(x,0)$ gives the initial shape of the string whilst $y_t(x,0)$ the initial velocity
# ```
# ````
# 
# We can use this initial data to work out the $A_n$ and $B_n$ in {eq}`wavesol` as follows
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

# In[1]:


# code to produce the animation of the solution y(x,t) shown below 
# with parameters L = pi, alpha = 1 and c = 1

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
    alpha = 1
    c = 1
    x = np.linspace(0, np.pi, 1000)
    y = alpha*np.sin(np.pi*x/L)*np.cos(np.pi*c*i*0.05/L)
    #y = np.sin(np.pi*x/L)*np.exp(-np.pi**2*kappa*(0.1*i)/L**2)+0.5*np.sin(2*np.pi*x/L)*np.exp(-4*np.pi**2*kappa*(0.1*i)/L**2)
    line.set_data(x, y)
    return (line,)
  
anim = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=150, blit=True)


# In[2]:


# (commands to be appended to the animation code above to run it in colab and save)
# Note: below is the part which makes it work on Colab 
#rc('animation', html='jshtml')
# anim # uncomment to play animation
# anim.save('waveeqn.mp4') # uncomment to save animation 

from IPython.display import HTML

HTML("""
    <video width="700" height="600" controls>
        <source src="../../../../_static/videos/waveeqn.mp4" type="video/mp4">
    </video>
""")


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
# 
# We shall spend the remainder of this chapter learning how to derive these very special function representations as they will prove crucial (as alluded to above) in our quest to solve the type of differential equations introduced in the previous chapter (Wave, Heat,... *etc.*).
