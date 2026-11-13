import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X=np.asarray(X,dtype=float)
    term=X.T@X
    inv_term=np.linalg.inv(term)
    rhs=X.T@y
    theta=inv_term@rhs

    return theta