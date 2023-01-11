#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part2/Chapter1/ComplexNumbers.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:





# # 1.1 Revision of complex numbers
# 
# <br>
# 
# ## Notation/definitions
# 
# - It is conventional to denote complex numbers by $z$;
# 
# - $z\in \mathbb{C}$ means $z$ is complex;
# 
# - $x\in \mathbb{R}$ means $x$ is real;
# 
# - the imaginary unit is defined: $i=\sqrt{-1}$; $i^2=-1$;
# 
# - $i^{-1}=-i$.
# 
# <br>
# 
# ## Algebraic form
# 
# A complex number $z$ can be written:
# 
# $$
# 	z=x+iy,\ x,y\in\mathbb{R};
# $$
# 
# $x$ is known as the real part of $z$: $\mathrm{Re}(z)=x$, while $y$ is termed the imaginary part of $z$: $\mathrm{Im}(z)=y$.
# 
# Adopting $z_1=x_1+iy_1$ and $z_2=x_2+iy_2$ where necessary, the following results hold
# 
# 1. Equality: $z_1=z_2$ iff $x_1=x_2$ and $y_1=y_2$
# 2. Addition/subtraction: $z_1\pm z_2 = (x_1\pm x_2) + i(y_1\pm y_2)$
# 3. Multiplication:
# 	- $k\in \mathbb{R}$: $kz = kx+iky$
# 	- $z_1z_2 = (x_1+iy_1)(x_2+iy_2) = (x_1x_2-y_1y_2)+i(x_1y_2+x_2y_1)$
# 4. Modulus: $|z| = |x+iy|=\sqrt{x^2+y^2}$
# 5. Conjugation: The conjugate of a complex number $z$ is denoted $\bar{z}$:  
# 	- $\overline{z}=x-iy$
# 	- $z\overline{z}=x^2+y^2$. **This is REAL.**
# 	- $\overline{z_1 + z_2} = \overline{z_1} + \overline{z_2}$
# 	- $\overline{z_1 z_2} = \overline{z_1} \cdot \overline{z_2}$
# 	- $|\overline{z}|=|{z}|$
# 6. Inverse: $\displaystyle z^{-1} = \frac{1}{x+iy} = \frac{x-iy}{x^2+y^2}$
# 7. Division: $\displaystyle\frac{z_1}{z_2}=z_1z_2^{-1}$, so using the previous result, 
#  
# $$
# \frac{z_1}{z_2}=\frac{(x_1+iy_1)(x_2-iy_2)}{x_2^2+y_2^2}=\frac{x_1x_2 + y_1y_2 + i(x_2y_1-x_1y_2)}{x_2^2+y_2^2}
# $$
# 
# <br>
# 
# **Method for inversion and division: multiply numerator and denominator by the conjugate of the denominator. This ensures that the denominator is real and the result can be written in the standard form $\mathbf{x+iy}$**
# 
# <br>
# 
# ```{note}
# Complex numbers cannot be ordered in the same way as real numbers: $z_1>z_2$ has no meaning (*cf.* vectors); however, $|z_1|>|z_2|$,  $\mathrm{Re}(z_1)>\mathrm{Re}(z_2)$,  $\mathrm{Im}(z_1)>\mathrm{Im}(z_2)$ do. 
# ```
# 
# <br>
# 
# ## Argand diagram
# 
# <br>
# 
# The complex number $z=x+iy$ can be understood in terms of a plot in Cartesian space: the real part of $z$ is plotted on the $x$-axis, the imaginary part on the $y$-axis. Simple trigonometry then gives us a series of important results.
# 
# ```{figure} ../../../images/ArgandDiagram.png
# ---
# height: 350px
# ---
# Argand diagram for the complex number $z = x+ iy$, indicating Cartesian and Polar coordinates
# ```
# <br>
# 
# The position of $z$ in the Argand diagram may be expressed in Polar coordinates via:
# 
# $$
# 	\mathbf{r}=(x,y);\ x=r\cos(\theta),\ y=r\sin(\theta);\ r=\sqrt{x^2+y^2}=|z|,\ \theta=\tan^{-1}(\tfrac{y}{x}).
# $$
# 
# There are a few important things to note about this representation:
# 
# 1. $\theta$ is known as the argument of $z$, denoted $\mbox{arg}(z)$.
# 
# 2. Clearly $z$ is unchanged for $\theta\pm 2n\pi$ for integer $n$. For uniqueness, the angle is typically restricted to $-\pi<\theta\leqslant\pi$.
# 
# 3. Although one can calculate it via $\theta=\tan^{-1}(\tfrac{y}{x})$, care must be taken that you choose the correct solution to this equation: $\theta\pm\pi$ is also a solution. The simplest way is to check which quadrant you require from the Argand diagram.
# 
# 4. $z$ can be written $z=r\cos\theta + i r \sin\theta$
# 
# <br>
# 
# ## Exponential form
# 
# Using the above results, one can easily derive another way of expressing a complex number.
# 
# Employing the above notation, we have
# 
# $$
# z = |z|\left(\cos\theta + i\sin\theta\right).
# $$
# 
# Now, expressing $\cos$ and $\sin$ in exponential notation:
# 
# $$
# z = |z|\left(\frac{e^{i\theta}+e^{-i\theta}}{2} + i \frac{e^{i\theta}-e^{-i\theta}}{2i}\right)=|z|e^{i\theta}.
# $$
# 
# From the above it is easy to see $e^{i\theta}=\cos\theta+i\sin\theta$. **This is known as Euler's formula.**
# 
# These different methods of writing complex numbers are useful when considering different algebraic operations.
# 
# 1. The algebraic form $x+iy$ is more convenient for addition/subtraction
# 
# 2. The polar and exponential forms are more convenient for multiplication and division
# 
# To see this, consider the complex multiplication $z_1z_2$ written in polar form:
# 
# $$
# z_1 = r_1\left(\cos\theta_1+i\sin\theta_1\right),\ z_2 = r_2\left(\cos\theta_2+i\sin\theta_2 \right)
# $$
# 
# then
# 
# $$
# z_1z_2 = r_1r_2\left(\cos\theta_1\cos\theta_2-\sin\theta_1\sin\theta_2 + i\left(\cos\theta_1\sin\theta_2 + \cos\theta_2\sin\theta_1 \right) \right)
# $$
# 
# and double angle formulae give
# 
# $$
# z_1z_2 = r_1r_2\left(\cos(\theta_1+\theta_2) + i\sin(\theta_1+\theta_2)\right).
# $$
# 
# Similarly:
# 
# $$
# \frac{z_1}{z_2}=\frac{r_1}{r_2}\left( \cos(\theta_1-\theta_2) + i \sin(\theta_1-\theta_2)\right);
# $$
# 
# and (for integers, $n$)
# 
# $$
# z^n=r^n e^{in\theta}.
# $$
# 
# ```{note} 
# The result $e^{in\theta}=\cos(n\theta)+i\sin(n\theta)$ is known as **DeMoivre's theorem**.
# ```
# 
# ## Curves and regions in the complex plane
# 
# ```{prf:example} 
# :label: example34
# 
# The equation of a circle.
# 
# In Cartesian coordinates, the equation of a circle with radius $R$, centred on $(x_0,y_0)$ is:
# 
# $$
# 	(x-x_0)^2 + (y-y_0)^2=R^2,
# $$
# 
# which, in complex form is: $|z-z_0|=R$, where $z_0=x_0+iy_0$. Employing the exponential notation above, this may also be written in the compact form: $z=z_0+Re^{i\theta}$.
# ```
# 
# By simple extension, regions in the complex plane may be defined via inequalities such as: $a<|z-z_0|<b$.
# 
# ```{figure} ../../../images/ConcentricCircles.png
# ---
# height: 350px
# ---
# The region in the complex plane between the two concentric circles is defined by $a<|z-z_0|<b$
# ```
