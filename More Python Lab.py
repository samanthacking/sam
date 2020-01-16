#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#rule 3

def rule3(dA,dB):
    dQ = np.sqrt(dA**2+dB**2)
    return dQ


# In[22]:


#rule 4

def rule4(q,m,dA,A,n,dB,B,o,dC,C):
    dQ = q*np.sqrt((m*dA/A)**2+(n*dB/B)**2+(o*dC/C)**2)
    return dQ


# In[11]:


L = 1.05
dL = 0.001
change_L = 0.00125
dchange_L = 0.00001
T_initial = 23.4
T_final = 92.5
dT_initial = 0.3
dT_final = 0.1


# In[27]:


change_T = T_final-T_initial
print ("change in T",change_T,"degrees celsius")


# In[26]:


alpha = change_L/L/(T_final-T_initial)
print ("alpha =",alpha,"1/degrees celsius")


# In[28]:


dchange_T = rule3(dT_initial,dT_final)
print ("uncertainty in change in T",dchange_T,"degrees celsius")


# In[29]:


dalpha = rule4(alpha,1,dchange_L,change_L,1,dL,L,1,dchange_T,change_T)
print ("uncertainty in alpha",dalpha,"1/degrees celsius")


# 

# In[ ]:




