import numpy as np
y=np.random.rand(5)
print(y)

z=np.random.randint(2,10,5)
print(z)
  

z=np.random.randint(2,10,5,dtype="int32")
print(z)
  


ar=np.array([[1,2],[3,4]])
print(ar.ndim)
print(ar.size)
print(ar.shape)
print(ar.dtype)
print(ar.itemsize)
print(ar.data)
print(id(ar))



a=np.array([[1,2],[3,4]])
a1=np.array([[1,2],[2,1]])
r=np.add(a,a1)
print(r)

print(a+a1)
print(  a,"\n",a1)
d=np.dot(a, a1)
print("\n\n\n", d)
s=np.matmul(a,a1)
print(s)
x=a@a1
print(x)

print(a*a1)
print(a)
print(a.T)
