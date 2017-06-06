#importing libraries, SDToolbox to solve model
import matplotlib.pyplot as plt
from SDToolbox import *
from matplotlib.legend_handler import HandlerLine2D

#intro
print "Author: Artur Abratanski"
print "CJ detonation of oxygen and hydrogen"

#Input of starting parameters
P1=101325.15; 
T1=273.15;
mech = 'wang_highT.cti';

#number or calculating points
n_h = 30

#creating space to store CJ speed, pressure, temperature and concentrations, density 
CJ=np.zeros(n_h)  
P=np.zeros(n_h)     
T=np.zeros(n_h)     
CH=np.zeros(n_h)  
CP=np.zeros(n_h)
vcj=np.zeros(n_h)

#loop through points of calculations
for k in range(n_h):
    c_h=.03*k+0.025    
#input of mixture
    q='H2:{0} O2:{1}'.format(c_h, 1-c_h) 
#calculation explosion speed
    [cj_speed,R2] = CJspeed(P1, T1, q, mech, 0);    
#implementing model of gas
    gas = PostShock_eq(cj_speed, P1, T1, q, mech)   
#calculation of state after explosion
    P[k] = gas.P/101325.15
    T[k] = gas.T
    CJ[k] = cj_speed  
    CH[k] = c_h
    vcj[k] = gas.density
    print k

#saving to files txt
np.savetxt("p.txt", P, delimiter = ',')
np.savetxt("t.txt", T, delimiter = ',')
np.savetxt("cj.txt", CJ, delimiter = ',')
np.savetxt("ro.txt", vcj, delimiter = ',')
#inform about finish
print "finish"