cimport numpy as np

from cupy.core.core cimport ndarray
from cupy.core.core cimport array
from cupy.core.core cimport dot


cpdef np.ndarray dot_gpu(np.ndarray a, np.ndarray b):
    cdef a_gpu = array(a)
    cdef b_gpu = array(b)

    cdef ndarray c = dot(a_gpu, b_gpu)
    return c.get()  # cupy.ndarray -> numpy.ndarray
