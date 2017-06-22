from dot_gpu import dot_gpu
import numpy as np
import time


a = np.random.uniform(size=(6000, 6000)).astype(np.float32)
b = np.random.uniform(size=(6000, 4000)).astype(np.float32)

dot_gpu(a, b)
start = time.time()
dot_gpu(a, b)
print('GPU {}ms'.format((time.time() - start) * 1000))

a.dot(b)
start = time.time()
a.dot(b)
print('CPU {}ms'.format((time.time() - start) * 1000))
