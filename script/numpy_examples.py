import numpy as np

# Create np arrays
a = np.array([[1,2,3],
             [4,5,6]])

# Create np arrays based on range
b = np.arange(1,10, 2)

# shape arrange to 2D
c = np.arange(1,10).reshape(3, 3)

# retrieve properties of np arrays
print(a.ndim)
print(a.size)
print(a.dtype)
print(a.shape)

# create zeros/ones/arrange/linespace np arrays
np.zeros((5,5))
np.ones((5,5))
np.array([[1,2,3],[4,5,6]], dtype=complex)
np.arange(1,10,2) # separated by 2
np.linspace(1,100,5) # divide to 5 parts

# create random np arrays
np.random.random((5,5))

# universal functions sum, minus, multiplication, division operations on np arrays
d = np.arange(3,9).reshape(2,3)
print(a + d)
print(a + 3)

# sin, cos, log, sqrt
print(np.sin(a))

# aggregate functions
print(np.sum(a))
print(np.min(a))
print(np.max(a))
print(np.mean(a))
print(np.std(a))

# slicing
print(a[1])
e = np.arange(10,19).reshape(3,3)
print(e)
e[1,2] = 23
print(e)

# flatten out array into lazy iterator
a.flat

# apply operation across an axis
print(np.apply_along_axis(np.max, 1, a))

 def half(n):
     return n/2

print(np.apply_along_axis(half, 1, a))

# subsetting of arrays based on condition
a[a < 3]

# reshaping nd arrays
#reshape returns a new array
a.reshape(4,3)
#shape modifies the existing array
a.shape = (4,3)
#converting 2-dimensional array to 1-dimensional array
a.ravel()

# ways to split / subset nd arrays
#np.hstack / np.vstack
np.hstack((np.zeros(4), np.ones(4), np.arange(0,4)))
np.vstack((np.zeros(4), np.ones(4), np.arange(0,4)))
np.column_stack((np.zeros(4), np.ones(4), np.arange(0,4)))
np.row_stack((np.zeros(4), np.ones(4), np.arange(0,4)))
#np.hsplit / np.vsplit / np.split
np.hsplit(a, 2)
np.vsplit(a, 2)
#np.split
np.split(a,1)

# copying np array
# When using assignment, it is referencing the same copy. 
# Same with slicing where it just creates a copy that reference the same underlying buffer.
k = np.copy(a)

# save/load np arrrays
np.save('my_np_array', a)
np.load('my_np_array')

# load from csv
np.genfromtxt('filename.csv', delimiter=',', names=True)

# unstructured
np.array([(1, 'First', 2.22), (2, 'Second', 3.34)], dtype=('i2, a6, f2'))

