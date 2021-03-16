import numpy as np

np.set_printoptions(suppress=True, formatter={'float_kind':'{:.4e}'.format})
CONST_K=9e9

def campo_magnetico(q1,r2, p, p1):	
	global CONST_K
	print(f"escalar = {CONST_K*q1/r2}  vector unitario = {(p-p1)}   norma = {np.linalg.norm(p-p1)}" )
	return  CONST_K*q1*(p-p1)/(np.linalg.norm(p-p1)*r2)



_A = np.array([0,0,0])
_B = np.array([0,3,0])
_C = np.array([4,0,1])


_P = np.array([0,0,1])
_Q = np.array([4,3,0])
_R = np.array([4,3,2])


print(campo_magnetico(-8e-6, 29e-4, _R, _A))

print(campo_magnetico(2e-6, 20e-4, _R, _B))

print(campo_magnetico(6e-6, 10e-4, _R, _C))


print(campo_magnetico(-8e-6, 29e-4, _R, _A)+campo_magnetico(2e-6, 20e-4, _R, _B)+campo_magnetico(6e-6, 10e-4, _R, _C))