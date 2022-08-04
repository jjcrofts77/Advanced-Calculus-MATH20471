#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part2/Chapter1/ComplexFunc.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:





# # 1.2 Functions of a complex variable
# 
# Functions of a complex variable work in an analogous way to functions which operate on real numbers.
# 
# >**Definition 1.2.1** A function of a complex variable $f(z)$ (where $z=x+iy$) maps $z$ onto another complex variable $w=u+iv$. In general, we write:
# 
# $$
# 	w= f(z)=u(x,y)+iv(x,y)
# $$
# 
# Revisiting the examples from previously:
# 
# 1. if $f(z)=z^2$, then 
# 
# 	$$f(z) = (x+iy)^2 = (x^2-y^2)+i2xy$$ 
# 
# 	and so 
# 
# 	$$ u=x^2-y^2 \quad\& \quad v=2xy$$
# 
# 2. if $f(z)=\overline{z}$ then
# 
# 	$$f(z) = \overline{x+iy}=x-iy$$ 
#   
# 	and so 
#   
# 	$$u=x\quad \& \quad v=-y.$$
# 
# Another way to think about a function is as a mapping from the Argand plane representing the independent variable $z$ onto the Argand plane representing the dependent variable $w$ (see figure below).
# 
# For example, under the mapping $w=f(z)$ where $f(z)=z^2$, we obtain:
# 
# $$
# 	z&=0+0i \longrightarrow w=0+0i,\\
# 	z&=1+0i \longrightarrow w=1+0i,\\
# 	z&=0+i \longrightarrow w=-1+0i,\\
# 	z&=3+4i \longrightarrow w=-7+i24,
# $$
# 
# All the standard theorems of continuity of functions apply in the complex plane. For example, if two functions $f_1$ and $f_2$ are continuous in a complex set $X$ then,
# 
# $$
# 	f_1+f_2,\ f_1f_2,\ \tfrac{f_1}{f_2},
# $$
# 
# are continuous in $X$.
# 
# ```{figure} ../../../images/ComplexMapping.png
# ---
# height: 250px
# ---
# A complex function $f$ as a mapping between $z=x+iy$ and $w=u(x,y)+iv(x,y)$
# ```
# 
# 
