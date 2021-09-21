# 2.2 Fourier series for functions of period $2\pi$

Let $f$ be a function of period $2\pi$. We would like to get an expansion for $f$ of the form

$$
 f(x) = \frac{1}{2}a_0 +\sum_{n=1}^\infty \left[a_n\cos(nx) + b_n\sin(nx)\right],
 \label{eqn:FS}
$$

where the $a_n$ and $b_n$ are constants. Remember that $\sin(nx)$ and $\cos(nx)$ are periodic with period $2\pi$. 

Such an expansion is know as a Fourier series (FS).

We have two questions to answer about the above series:

**Question 1:** If the series on the RHS of (\ref{eqn:FS}) converges, can we find constants $a_0, a_n$ and $b_n$ in terms of the function $f$?

**Question 2:** with these $a_n, b_n$, for what values of $x\in\mathbb{R}$ does our FS equation hold?

## Question 1

Suppose the above equation is true and that we can integrate it term by term (\emph{i.e} the series on the RHS above converges *uniformly*) so that

$$
\int_{-\pi}^\pi f(x)\mathrm{d}x = \frac{1}{2}a_0\int_{-\pi}^\pi\mathrm{d}x +\sum_{n=1}^\infty \left[a_n\int_{-\pi}^\pi\cos(nx)\mathrm{d}x + b_n\int_{-\pi}^\pi\sin(nx)\mathrm{d}x\right],
$$

Since 

$$
\int_{-\pi}^\pi \mathrm{d}x = 2\pi, \quad \int_{-\pi}^\pi \cos(nx)\mathrm{d}x = 0, \quad \int_{-\pi}^\pi\sin(nx)\mathrm{d}x=0,
$$

we must have

$$
a_0 = \frac{1}{\pi}\int_{-\pi}^\pi f(x)\mathrm{d}x.
$$

Thus if equation the FS holds, then we know $a_0$.

```{admonition} Lemma 2.1
:class: tip
Let $n, m\in\mathbb{N}\backslash 0$. We then have the following equalities:

$$
\int_{-\pi}^\pi \sin(mx)\cos(nx)\mathrm{d}x = 0,\label{eqnSC}
$$

$$
 \int_{-\pi}^\pi\sin(mx)\sin(nx)\mathrm{d}x = \pi\delta_{nm},\label{eqn:SS}
$$

$$
 \int_{-\pi}^\pi\cos(mx)\cos(nx)\mathrm{d}x = \pi\delta_{nm}.\label{eqnCC}
$$

where $\delta_{mn}$ is the *Kronecker delta* defined by

$$
 \delta_{mn} = \begin{cases}0& n\neq m\\1&n=m.\end{cases}
$$
```
```{admonition} Proof
:class: tip, dropdown

hi

```