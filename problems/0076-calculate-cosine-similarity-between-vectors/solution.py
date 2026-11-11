import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    if(v1.ndim!=v2.ndim or len(v1)!=len(v2)):
        return -1
    num=np.dot(v1,v2)
    l2_1=float(np.sqrt(np.sum(v1**2)))
    l2_2=float(np.sqrt(np.sum(v2**2)))
    ans=float(num/(l2_1*l2_2))
    return ans
    pass