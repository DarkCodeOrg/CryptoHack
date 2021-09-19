## the gram schimdt algorithm creates  orthogonal basis vectors v*_1, v*_2 , v*_3 , ....... , v*_n 
## if a basis v_1, v_2, v_3, .... v_n is given for a vector space V blongs to R_n
## 
## import numpy
'''import numpy as np 

## given basis vectors 
u =[[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]
u = np.array(u)
## final orthogonal basis initialization
v = [[0],[0],[0],[0]] 
v = np.array(v)

v[0] = u[0]
print(v[0]) ### debug


for i in range(1,4):
    for j in range(1,i):
        m = (u[i]*v[j])/(v[j]*v[j])
        
'''
import numpy as np 


def gram_schmidt(vectors):
    basis = []
    for v in vectors:
        w = v - np.sum( np.dot(v,b)*b  for b in basis )
        if (w > 1e-10).any():
            basis.append(w/np.linalg.norm(w))
    return np.array(basis)

u = np.array([[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]])

print(gram_schmidt(u))


