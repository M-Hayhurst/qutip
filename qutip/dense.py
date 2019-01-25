# custom functions for dense matricies
import numpy as np

def is_hermitian(x, tol=1e-8):
    return np.allclose(x, np.conjugate(x.T), atol=tol)
