# Chapter 3 The heat equation

Before we move on to complex integration, we need to consider singularities in functions of a complex variable.

A singular point of a complex function $f(z)$ is a point in the complex plane at which $f$ is \emph{not} analytic. To be pedantic, earlier in the course, I have used the terms ``analytic'' and ``differentiable'' interchangeably. However, this isn't strictly the case.

The derivative of a function exists at $z=z_0$ if 
\[ 
\lim_{z\to z_0}\f{f(z)-f(z_0)}{z-z_0}
\]
exists, independent of the way in which $z\to z_0$. Such a derivative exists at a point if and only if the Cauchy-Riemann conditions are satisfied. 

However, a function is ``analytic'' at the point $z_0$ if its derivative exists in some \emph{neighbourhood} of $z_0$. A neighbourhood of a complex number $z_0$ is defined as the disc in the complex plane obeying $|z-z_0|<\epsilon$ for some small positive number, $\epsilon$.\label{definition1}

This may not seem important but, considering the function $f(z)=x^2-iy^2$. Taking the various derivatives:
\[
	\f{\p u}{\p x}=2x,\ \f{\p u}{\p y}=0,\ \f{\p v}{\p x}=0,\ \f{\p v}{\p y}=-2y,
\]
and so the Cauchy-Riemann conditions not satisfied unless $y=-x$. So the first derivative exists only along that line. However, for any non-zero $\epsilon$, the neighbourhood of any $z_0$ on the line $y=-x$ contains points at which $f$ is not analytic; the function $f(z)=x^2-iy^2$ is nowhere analytic.\label{ex6}

\paragraph{Definition:} If $f(z)$ is analytic at every point within a set $S\in \mathbb{C}$, $f$ is ``analytic on $S$''.
If $f(z)$ is analytic at every point within $\mathbb{C}$, $f$ is ``entire''.
