#!/usr/bin/env python
# coding: utf-8

# In[25]:


from sympy import *
import numpy as np


# In[26]:

def angle_calc(a1=69.08221435546875,b1=73.4642333984375,c1=119,h1=268.5776672363281,k1=114.11849975585938):
    c_0, c_1, c_2, c_3, c_4, c_5 = symbols('c_0, c_1, c_2, c_3, c_4, c_5')
    a, b, theta, h, k = symbols('a, b, theta, h, k')
    m, c = symbols('m, c')
    A, B, C = symbols('A, B, C')
    x = symbols('x')
    phi = symbols('phi')


    # In[27]:
    y = Function('y')(x)


    # In[28]:


    c_0 = (cos(theta)**2)/(a**2) + (sin(theta)**2)/(b**2)
    c_1 = (cos(theta)**2)/(b**2) + (sin(theta)**2)/(a**2)
    c_2 = (sin((2*theta)))/(a**2) - (sin((2*theta)))/(b**2)
    c_3 = -(2*h*(cos(theta)**2))/(a**2) - (k*sin(2*theta))/(a**2) - (2*h*(sin(theta)**2))/(b**2) + (k*sin(2*theta))/(b*2*2)
    c_4 = -(2*k*(cos(theta)**2))/(b**2) - (h*sin(2*theta))/(a**2) - (2*k*(sin(theta)**2))/(a**2) + (h*sin(2*theta))/(b**2)
    c_5 = (h*h*(cos(theta)**2))/(a**2) + (h*k*sin(2*theta))/(a**2) + (k*k*(sin(theta)**2))/(a**2) + (h*h*(sin(theta)**2))/(b**2) - (h*k*sin(2*theta))/(b**2) + (k*k*(cos(theta)**2))/(b**2) - 1


    # In[29]:


    ellipse = c_0*(x**2) + c_1*(y)**2 + c_2*x*y + c_3*x + c_4*y + c_5


    # In[30]:


    fin_eq = Poly(ellipse.subs(y, m*x + c), x)
    # [A, B, C] = fin_eq.coeffs()


    # In[34]:


    eq = ellipse.subs(y, m*x + c)
    sub_eq = eq.subs([(m, 0), (c, c1), (h, h1), (k, k1), (a, a1), (b, b1), (theta,0)])



    # In[35]:


    [x1, x2] = solve(sub_eq, x)
    y1 = (m*x1 + c).subs([(m, 0), (c, c1)])
    y2 = (m*x2 + c).subs([(m, 0), (c, c1)])
    [(x1, y1), (x2, y2)]


    # In[36]:


    diff_eq = diff(ellipse, x).subs([(h, h1), (k, k1), (a, a1), (b, b1), (theta,0), (diff(y, x),  phi)])


    # In[37]:


    ans1 = solve(diff_eq.subs(y, y1), phi)[0].subs(x, x1)
    ans2 = solve(diff_eq.subs(y, y2), phi)[0].subs(x, x2)
    
    ans1,ans2 = [np.arctan(float(ans1))*180/np.pi,  np.arctan(float(ans2))*180/np.pi]
    if ans1>0:
        ans1 = ans1-180
        ans2 = 180+ans2
    return [ans1,ans2]

