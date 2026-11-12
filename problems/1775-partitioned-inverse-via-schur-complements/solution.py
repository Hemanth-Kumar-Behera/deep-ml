import numpy as np

def partitioned_inverse(M, k):
    E=M[:k,:k]
    F=M[:k,k:]
    G=M[k:,:k]
    H=M[k:,k:]

    H_inverse_G=np.linalg.solve(H,G)
    F_H_inverse=np.linalg.solve(H.T,F.T).T
    S=E-F@H_inverse_G
    S_inverse=np.linalg.inv(S)
    
    top_left=S_inverse
    top_right=-S_inverse@F_H_inverse
    bottom_left=-H_inverse_G@S_inverse
    bottom_right=np.linalg.inv(H)+H_inverse_G@S_inverse@F_H_inverse

    return np.block([[top_left,top_right],[bottom_left,bottom_right]])
    
    pass

def block_slogdet(M, k):
    E=M[:k,:k]
    F=M[:k,k:]
    G=M[k:,:k]
    H=M[k:,k:]

    H_inverse_G=np.linalg.solve(H,G)
    S=E-F@H_inverse_G
    sign_S,log_det_s=np.linalg.slogdet(S)
    sign_H,log_det_h=np.linalg.slogdet(H)
    return float(sign_S*sign_H),float(log_det_s+log_det_h)
    pass

def bordered_inverse(A_inv, b, c):
    b=np.asarray(b,dtype=float).ravel()
    u=A_inv@b
    s=float(c-np.dot(b,u))
    if(abs(s)<1e-12):
        raise ValueError("Matrix is singular or nearly singular")
    inv_s=1.0/s
    top_left=A_inv+inv_s*np.outer(u,u)
    top_right=(-inv_s*u).reshape(-1,1)
    bottom_left=(-inv_s*u).reshape(1,-1)
    bottom_right=np.array([[inv_s]])
    return np.block([[top_left,top_right],[bottom_left,bottom_right]])


    pass
