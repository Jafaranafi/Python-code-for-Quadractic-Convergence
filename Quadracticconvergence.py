import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return x**3+x-1
def g(x):
	return 2*x**2+1
n=18
#x=2
u=np.zeros(19)
u[0]=1

for i in range(n):
	u[i+1]=u[i]-f(u[i])/g(u[i])
	t=abs(u[i+1]-u[0])
	d=(abs(u[i]-u[0]))**2
	c=(abs(u[i+1]-u[0]))/(abs(u[i]-u[0]))**2
	print (c)


