import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    
    Args:
        gradient: A list representing the gradient vector
    
    Returns:
        Dictionary containing:
        - magnitude: The L2 norm of the gradient
        - direction: Unit vector in direction of steepest ascent
        - descent_direction: Unit vector in direction of steepest descent
    """
    # Your code here
    m={}
    magnitude=np.linalg.norm(gradient,ord=2)

    if magnitude==0:
        direction=np.zeros(len(gradient))
        descent_direction=np.zeros(len(gradient))
    else:
        direction=np.array(gradient)/magnitude
        descent_direction=-direction
    m['magnitude']=magnitude
    m['direction']=direction
    m['descent_direction']=descent_direction
    return m
    pass