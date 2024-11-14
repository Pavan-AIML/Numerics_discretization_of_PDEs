<h1>Numerics_discretization_of predator, pre differential equations.</h1> 
<h2 align =center> I have implemented the following methods in this project. </h2> 

- Euler's method -
- Modified Euler's method
- Heun's method to discretize the PDE.
  
<h3> The Differential equation is given below. </h3>

<p align = center> $$ b_{dot} = \lambda_b \cdot b \cdot \left(1 - \frac{r}{r_e}\right) $$ </p>
<p align = center >  $$ r_{dot} = \lambda_r * r * \frac{b}{b_e -1} $$ </p>

<p>
$$
\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2} \right)
$$
</p>
