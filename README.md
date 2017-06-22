# Cython level API for CuPy

Please install CuPy from one of my branch.

https://github.com/yuyu2172/cupy/tree/cython-API

(go there and `python setup.py develop`)


Install the module in this repository.

```
pip install -e .
```




### Demo

```
python run.py
```

This demo runs `dot_gpu` and NumPy's `dot`.
`dot_gpu` takes NumPy arrays as inputs and returns dot product of them.
Internally, it sends the NumPy arrays to GPU, take dot product by calling cuBLAS and send them back to CPU.

Please note that, the function `dot_gpu.dot_gpu` calls CuPy functions at Cython level.
In order to call them at Cython level, I needed to modify CuPy code base to expose some of its API at this level.
The changes were relatively straightforward.
