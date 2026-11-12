import numpy as np

def woodbury_solve(sigma_diag, X, B):
    sigma_diag=np.asarray(sigma_diag,dtype=float)
    X=np.asarray(X,dtype=float)
    B=np.asarray(B,dtype=float)
    sigma_inv=1.0/sigma_diag
    sigma_X=sigma_inv[:,None]*X
    D=X.shape[1]
    M=np.eye(D)+X.T@sigma_X

    if B.ndim==1:
        sigma_inv_B=sigma_inv*B
    else:
        sigma_inv_B=sigma_inv[:,None]*B
    
    rhs=X.T@sigma_inv_B
    M_inv_B=np.linalg.solve(M,rhs)
    return sigma_inv_B-sigma_X@M_inv_B

    

def sherman_morrison(A_inv, u, v):

    u=np.asarray(u,dtype=float).ravel()
    v=np.asarray(v,dtype=float).ravel()

    A_inv_u=A_inv@u
    V_A_inv=v@A_inv
    denom=float(1.0+np.dot(v,A_inv_u))
    if abs(denom)<=1e-12:
        raise ValueError("Rank-1 update produces singular matrix"
        )
    return A_inv-np.outer(A_inv_u,V_A_inv)/denom
    pass

def logdet_rank_one_update(logdet_A, A_inv, u, v):
    u=np.asarray(u,dtype=float).ravel()
    v=np.asarray(v,dtype=float).ravel()
    factor=float(1.0+np.dot(v,A_inv@u))
    if factor<=0.0:
        raise ValueError("Updated Det is not positive")
    return float(logdet_A+np.log(factor))
    pass
