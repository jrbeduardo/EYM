import numpy as np

np.set_printoptions(suppress=True, formatter={'float_kind':'{:.4e}'.format})
CONST_K=9e9

def fuerza_coulomb(q1,q2,r2, p1, p2):	
	global CONST_K
	return CONST_K*q1*q2*(p1-p2)/((np.linalg.norm(p1-p2)*r2)) 

_A = np.array([0,0])
_B = np.array([4,3])

q1 = -10e-6
q2 = 2.5e-6
r2 =  25e-4

print(fuerza_coulomb( q1, q2, r2, _A, _B))

