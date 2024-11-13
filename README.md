<h1>Numerics_discretization_of predator, pre differential equations.</h1> 
<h2 align =center> In this project I have implemented the following methods. </h2> 

- Euler's method -
- Modified Euler's method
- Heun's method to discretize the PDE.
  
<h3> The Differential equation is given below. </h3>
<p align = center> b' = lambda_b*b*(1-r/r_e)</p>
<p align = center >  r' = lambda_r * r * (b/b_e -1) </p>
<p> Here we will use Euler's method we will approximate the pde in its neighborhood by its tangent line meaning we will use the first step methods to check how the error propagates as the steps increase and it's also accumulates by increasing the number of steps. </p>
