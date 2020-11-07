import numpy as np

arr = np.array([100,200,300,400,500])
print(arr)
print(np.__version__)

print(arr[5:1:-1])
print(arr[4:2:-1])


twoDarr = np.array([[[1,5,15],[6,9,12],[10,20,30]]])
print(twoDarr)

print(arr.ndim)
print(twoDarr.ndim)