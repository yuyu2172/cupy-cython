from distutils.core import setup
from Cython.Build import cythonize
from distutils.extension import Extension

import numpy as np


ext_modules = [
    Extension('dot_gpu', ['dot_gpu.pyx'],
              language='c++')
]

setup(
    name = "Cython CuPy",
    ext_modules = cythonize(ext_modules),
    include_dirs=[np.get_include()]
)
