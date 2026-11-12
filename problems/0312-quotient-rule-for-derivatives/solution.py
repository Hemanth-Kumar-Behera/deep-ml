import numpy as np
def evaluate(coeffs,x):
    degree=len(coeffs)-1
    val=0.0
    der=0.0

    for i,c in enumerate(coeffs):
        power=degree-i
        val+=c*(x**power)
        if power>0:
            der+=c*power*(x**(power-1))
    return val,der
def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    gval,gder=evaluate(g_coeffs,x)
    hval,hder=evaluate(h_coeffs,x)

    return (gder*hval-hder*gval)/(hval**2)

    # Your code here
    pass