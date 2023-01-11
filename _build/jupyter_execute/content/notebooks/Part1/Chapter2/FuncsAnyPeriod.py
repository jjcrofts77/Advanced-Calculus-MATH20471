#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/jjcrofts77/Advanced-Calculus-MATH20471/blob/main/content/notebooks/Part1/Chapter2/FuncsAnyPeriod.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # 2.4 Functions of Any Period
# 
# Consider a function $f$ of period $2L (L>0)$. We want a series in $\cos(n\pi x/L)$ and $\sin(n\pi x/L)$. To do this we make the transformation $X=\pi x/L$. Formally, we define $g(X) = f(x) = f(LX/\pi)$ so that
# 
# ````{margin}
# ```{note}
# This derivation is **not** examinable
# ```
# ````
# 
# <br>
# 
# $$
# g(X+2\pi) = f\left(\frac{L(X+2\pi)}{\pi}\right) = f\left(\frac{LX}{\pi}+2L\right) = f\left(\frac{LX}{\pi}\right) = g(X),
# $$
# 
# <br>
# 
# and $g(X)$ is $2\pi$ periodic. Hence the previous theory holds for $g$, *i.e.* if we can write
# 
# $$
#  g(X) = \frac{1}{2}a_0 + \sum_{n=1}^\infty\left[ a_n\cos(nX) + b_n\sin(nX)\right],
# $$ (geqn)
# 
# then
# 
# $$
# \nonumber a_n &= \frac{1}{\pi}\int_{-\pi}^\pi g(X)\cos(nX) \mathrm{d}X\\\nonumber
#  &= \frac{1}{\pi}\int_{-L}^L g\left(\frac{\pi x}{L}\right)\cos\left(\frac{n\pi x}{L}\right)\frac{\pi}{L} \mathrm{d}x\\
#  &=\frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right) \mathrm{d}x,
# $$
# 
# and
# 
# $$
# \nonumber b_n &= \frac{1}{\pi}\int_{-\pi}^\pi g(X)\sin(nX) \mathrm{d}X\\
#  &= \frac{1}{\pi}\int_{-L}^L g\left(\frac{\pi x}{L}\right)\sin\left(\frac{n\pi x}{L}\right)\frac{\pi}{L} \mathrm{d}x\\
#  &=\frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right) \mathrm{d}x.
# $$
# 
# So we can write
# 
# $$
#  f(x) = \frac{1}{2}a_0 + \sum_{n=1}^\infty\left[a_n\cos\left(\frac{n\pi x}{L}\right) + b_n\sin\left(\frac{n\pi x}{L}\right)\right],
# $$ (feqn)
# 
# then {eq}`geqn` holds, so
# 
# $$
# a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right) \mathrm{d}x, \quad b_n = \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right) \mathrm{d}x.
# $$
# 
# The series in {eq}`feqn` is called the Fourier series for $f$ and $a_n$ and $b_n$ are the Fourier coefficients of $f$. Again, we use $\sim$ if we are unsure whether or not the series converges. By Theorem 2.2, under suitable conditions the series in equation {eq}`geqn` converges to
# 
# $$
#  \frac{g(X_+)+g(X_-)}{2}
# $$
# 
# so we obtain
# 
# <br>
# 
# ```{prf:theorem} FS convergence
# :label: FSConv
# 
# Let $f$ be a periodic function of period $2L$ which is sufficiently well-behaved. Then the Fourier series of $f$ at $x$ converges to
# 
# $$
#  \frac{f(x_+)+f(x_-)}{2},
# $$
# 
# so that Equation {eq}`feqn` holds at any point where $f$ is continuous.
# ```
# 
# ````{prf:example} 
# :label: example21
# 
# Find the Fourier series of the $2L$-periodic extension of
# 
# $$
#  f(x) = \begin{cases}x & x\in(0, L]\\ 0 & x\in(-L, 0].\end{cases}
# $$ (FuncExample241)
# 
# ```{figure} ../../../images/Example23.png
# ---
# height: 200px
# name: FigExample241
# ---
# Plot of the function in {eq}`FuncExample241`
# ```
# 
# Hence show that
# 
# $$
#  \frac{\pi^2}{8} = \sum_{m=0}^\infty \frac{1}{(2m+1)^2}.
# $$ (Ex1)
# 
# ```{toggle}
# We have 
# 
# $$
# a_n = \frac{1}{L}\int_{-L}^L f(x)\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \frac{1}{L}\int_0^Lx\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \frac{L[(-1)^n-1]}{n^2\pi^2}, \quad n\neq 0.
# $$
# 
# So we have $a_{2m}=0$ for $m>0$ and
# 
# $$
#  a_{2m+1} = \frac{-2L}{(2m+1)^2\pi^2}.
# $$
# 
# For $a_0$ we calculate
# 
# $$
#  a_0 = \frac{1}{L}\int_{-L}^L f(x)\mathrm{d}x=\frac{1}{L}\int_0^L x\mathrm{d}x = \frac{L}{2},
# $$
# 
# and for $b_n$
# 
# $$
#  b_n &= \frac{1}{L}\int_{-L}^L f(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x\\
#  &=\frac{1}{L}\int_0^Lx\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x\\
#  &= \frac{1}{L}\left(\left[-\frac{Lx}{n\pi}\cos\left(\frac{n\pi x}{L}\right)\right]_0^L + \int_0^L\frac{L}{n\pi}\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x\right)\\
#  &=\frac{1}{L}\left(-\frac{L^2(-1)^n}{n\pi} + \left[\frac{L^2}{n^2\pi^2}\sin\left(\frac{n\pi x}{L}\right)\right]_0^L\right)\\
#  &= (-1)^{n+1}\frac{L}{n\pi}.
# $$
# 
# So
# 
# $$
#  f(x) \sim \frac{L}{4} + \sum_{m=0}^\infty \frac{-2L}{(2m+1)^2\pi^2}\cos\left[\frac{(2m+1)\pi x}{L}\right] + \sum_{m=1}^\infty (-1)^{m+1}\frac{L}{m\pi}\sin\left(\frac{m\pi x}{L}\right).
# $$ (FSEx1)
# 
# By Theorem 2.4.1, if $x\in [0,L)$ we obtain
# 
# $$
# x = \frac{L}{4}+ \sum_{m=0}^\infty \frac{-2L}{(2m+1)^2\pi^2}\cos\left[\frac{(2m+1)\pi x}{L}\right] + \sum_{m=1}^\infty (-1)^{m+1}\frac{L}{m\pi}\sin\left(\frac{m\pi x}{L}\right).
# $$
# 
# because $f$ is continuous on $[0,L)$. If we put $x=0$ we calculate
# 
# $$
# 0 = \frac{L}{4} + \sum_{m=0}^\infty\frac{-2L}{(2m+1)^2\pi^2},
# $$
# 
# which proves {eq}`Ex1`. If we set $x=L$ in equation {eq}`FSEx1` we obtain
# 
# $$
# \frac{f(L_+)+f(L_-)}{2} = \frac{L}{4} + \sum_{m=0}^\infty\frac{-2L}{(2m+1)^2\pi^2}\cos\left((2m+1)\pi\right),
# $$
# 
# giving
# 
# $$
#  \frac{0+L}{2} = \frac{L}{4} + \sum_{m=0}^\infty\frac{-2L}{(2m+1)^2\pi^2},
# $$
# 
# which gives equation {eq}`Ex1` again.
# 
# ````
# 
# ## Sine and cosine series
# 
# Given a function $f$ defined on $[0,L]$ we require an expansion with only cosine terms or only sine terms. This will be done by extending $f$ to be even (for only cosine terms) or odd (for only sine terms) on $(-L,L]$ and then extending to a $2L$-periodic function. The series obtained will then be valid on $(0,L)$.
# 
# <br>
# 
# ```{prf:definition} half-range cosine series
# 
# If $f$ is defined on $[0, L]$, the *even extension* for $f$, denoted by $f_e$, is the periodic extension of
# 
# $$
# f_e(x) = \begin{cases}
# f(x)& x\in[0,L),\\
# f(-x)& x\in(-L,0),
# \end{cases}
# $$
# 
# so that $f_e(x) = f_e(-x)$ for all $x$. Thus 
# 
# $$
# f_e(x)\sim \frac{a_0}{2}+\sum_{n=1}^\infty a_n\cos\left(\frac{n\pi x}{L}\right),
# $$
# 
# where
# 
# $$
#  a_n = \frac{1}{L}\int_{-L}^Lf_e(x)\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x = \frac{2}{L}\int_0^Lf(x)\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x,
# $$
# 
# is called the *half-range cosine series* of $f$.
# ```
# 
# ```{prf:definition} half-range sine series
# 
# The *odd extension* for $f$, denoted by $f_o$, is the periodic extension of
# 
# $$
# f_o(x) = \begin{cases}
# f(x)& x\in[0,L),\\
# -f(-x)& x\in(-L,0),
# \end{cases}
# $$
# 
# so that $f_o(x) = -f_o(-x)$ for all $x\neq nL$. Similarly, 
# 
# $$
# f_o(x)\sim \sum_{n=1}^\infty b_n \sin\left(\frac{n\pi x}{L}\right),
# $$
# 
# where
# 
# $$
#  b_n = \frac{2}{L}\int_0^Lf(x)\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x,
# $$
# 
# is called the *half-range sine series* for $f$.
# ```
# 
# ```{note} For $f_o$ to really be odd we must have $f_o(0)=0$ and also $f_o(L)=-f_o(-L)=-f_o(L)$ (the last equality follows from periodicity) giving $f_o(L)=0$ and therefore $f_o(nL)=0$ for all $n\in\mathbb{Z}$. However, the value of $f$ at these isolated points does not affect the Fourier series.
# ```
# 
# ````{prf:example}
# :label: example22
# 
# Find the half-range sine and cosine series  expansions of $f(x)=x$ for $x\in[0,L]$.
# 
# *Sine expansion:* 
# 
# ```{figure} ../../../images/Example24Odd.png
# ---
# height: 200px
# ---
# Odd extension of $f(x)=x$ for $x\in[0,L]$
# ```
# 
# The odd extension is defined by
# 
# $$
#  f_o(x) = \begin{cases} x&x\in[0,L],\\-(-x)&x\in(-L,0).\end{cases}
# $$
# 
# In this case 
# 
# $$
#  b_n = \frac{2}{L}\int_0^L x\sin\left(\frac{n\pi x}{L}\right)\mathrm{d}x = (-1)^{n+1}\frac{2L}{n\pi},
# $$
# 
# as in {prf:ref}`example21`. For $x\in[0,L)$ we therefore obtain
# 
# $$
#  x = \sum_{n=1}^\infty (-1)^{n+1}\frac{2L}{n\pi}\sin\left(\frac{n\pi x}{L}\right).
# $$
# 
# *Cosine expansion* 
# 
# ```{figure} ../../../images/Example24Even.png
# ---
# height: 200px
# ---
# Even extension of $f(x)=x$ for $x\in[0,L]$
# ```
# 
# The even extension is defined by
# 
# $$
#  f_e(x) = \begin{cases}x&x\in[0,L],\\-x&x\in(-L,0).\end{cases}
# $$
# 
# Now, 
# 
# $$
#  a_0 = \frac{2}{L}\int_0^L x\mathrm{d}x = L,
# $$
# 
# and
# 
# $$
#  a_n=\frac{2}{L}\int_0^L x\cos\left(\frac{n\pi x}{L}\right)\mathrm{d}x =
#  \begin{cases}0&n=2m \text{ even},\\ \frac{-4L}{(2m+1)^2\pi^2}&n=2m+1 \text{ odd}. \end{cases}
# $$
# ````

# In[ ]:




