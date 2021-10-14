# 4.1 Derivation in one space dimension (optional)

In this chapter we look at the wave equation, concentrating on applications to waves on strings. We 
discuss methods for solution and also uniqueness of solutions.

Our derivation will depend upon a number of modelling assumptions. The string of length $L$ will be of uniform mass density and fixed rigidly at both ends as in Figure \ref{fig:string}(a). The vertical displacement ($y(x, t)$) will be small compared to $L$. We will also neglect stretching and bending of the string; meaning energy losses associated with dampening in the distortion of the string are neglected. Other external forces such as gravity will also be ignored.

Consider a segment of string from $x$ to $x +\Delta{x}$ as in Figure \ref{fig:string}(b). The Tension $T$ is always tangential 
to the string. Breaking this vector into its horizontal and vertical components we have

$$
 T_y = -T\sin{\theta},\\
 T_x = -T\cos{\theta},
$$

where $\theta$ is the angular displacement from the horizontal. The horizontal component $T_x$ can be neglected since every 
point on the string has another tension vector in the opposite direction. The slope of the string at any point $x$ can be described as 
$\partial{y}/\partial{x}=\tan{\theta}$ (Figure \ref{fig:tension}(a)). Additionally, since $y(x,t)$ is small compared to 
$L$, $\cos{\theta}\approx 1$ so $\tan{\theta} \approx \sin{\theta}$. 