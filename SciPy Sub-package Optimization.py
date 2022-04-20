#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from scipy import optimize


# In[5]:


def f(x):
    return x**2 + 5*np.sin(x)


# In[6]:


minimaValue = optimize.minimize(f,x0=2,method='bfgs',options={'disp':True})


# In[8]:


minimaValueWithoutOpt = optimize.minimize(f,x0=2,method='bfgs')


# In[9]:


minimaValueWithoutOpt


# In[ ]:




