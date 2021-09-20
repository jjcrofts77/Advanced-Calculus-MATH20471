# 2.1 Periodic, even and odd functions

We start this section by reviewing some of the most important properties of *periodic functions*. 

```{admonition} Definition
:class: tip
$f$ is a *periodic function* if there is an $a>0$ such that

$$
 f(x+a) = f(x), \quad \forall x \in\mathbb{R}.
$$

If this is the case then $a$ is called a *period* for $f$. Note that the period is not unique, but if there is 
a smallest such $a$, it is called the *prime period* of $f$.
```
The following points should be clear from the above definitions.

1. Observe that this means that $f(x) = c$ for some constant $c$ does not have a prime period.
2. Examples of periodic functions are $\sin{x}$ with prime period $2\pi$ and $\cos(2\pi x/a)$ with 
prime period $a$. Examples of non-periodic functions are $x$ and $x^2$.
3. Observe that if $f$ is defined on the half-open interval $(\alpha, \alpha+a]$ we can extend it 
to be a periodic function by demanding it is periodic with period $a$. This is called a *periodic extension*.

A concept that will prove useful moving forward is the following.

```{admonition} Definition
:class: tip
Formally, we define the *periodic extension*, $F$, of $f$ as follows: given $x\in\mathbb{R}$ there exists a unique integer $m$ 
such that $x-ma\in(\alpha, \alpha+a]$. If we then set $F(x) = f(x-ma)$, we can see that $F$ is periodic with period $a$.
```

## Properties of periodic functions
If $f, g$ are periodic functions with period $a$, then:
 1. $f, g$ are also periodic functions with period $na$ for any $n\in \mathbb{N}$;
 2. for any $\alpha, \beta \in \mathbb{R}$, $\alpha f + \beta g$ is periodic with period $a$;
 3. $fg$ is periodic with period $a$;
 4. for any $\lambda>0$, $f(\lambda x)$ is periodic with period $a/\lambda$,
 
$$
  f(\lambda(x+a/\lambda)) = f(\lambda x+a) = f(\lambda x);
$$

 \item for any $\alpha\in\mathbb{R}$,

$$
 \int_0^a f(x)\mathrm{d}x = \int_\alpha^{\alpha+a}f(x)\mathrm{d}x.
$$

## Odd and even functions

```{admonition} Definition
:class: tip
A function $f:\mathbb{R}\rightarrow\mathbb{R}$ is said to be *odd* if

$$
 f(x) = -f(-x), \qquad \forall x\in\mathbb{R}.
$$

```
For example, $\sin(\lambda x)$ for $\lambda\in\mathbb{R}$ and $x^{2n+1}$ for $n\in\mathbb{N}$ are both odd functions.

```{admonition} Definition
:class: tip
A function $g:\mathbb{R}\rightarrow\mathbb{R}$ is said to be *even* if

$$
 g(x) = g(-x), \qquad \forall x\in\mathbb{R}.
$$

```
Examples of even functions are $\cos(\lambda x)$ for $\lambda\in\mathbb{R}$ and $x^{2n}$ for $n\in\mathbb{N}$.

If $f, f_1$ are odd functions and $g, g_1$ are even functions then: 

 1. $f(0)=0$ because $f(0)=-f(-0)=-f(0)$;
 2. for any $\alpha\in\mathbb{R}$, we have that 
 $\displaystyle \int_{-\alpha}^\alpha f(x)\mathrm{d}x = 0;$

 3. for any $\alpha\in\mathbb{R}$, we have that
$
 \displaystyle \int_{-\alpha}^\alpha g(x)\mathrm{d}x = 2\int_0^\alpha g(x)\mathrm{d}x;
$

 4. the functions $h(x)=f(x)g(x)$, $h_1(x)=f(x)f_1(x)$ and $h_2(x)=g(x)g_1(x)$ are odd, even and even, respectively.