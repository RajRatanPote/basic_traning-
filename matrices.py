# -*- coding: utf-8 -*-
"""Matrices.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WifCMUltcnLCjLxq-wzg4Q9yXzWwxPVb
"""

# addition 
import numpy as np
a=np.array([[2,5],[3,4]])
b=np.array([[7,2],[5,9]])
c= a+b
print(c)

# multiplacation
a=np.array([[3,6,9],[8,-5,2]])
b=np.array([[1,1],[7,2],[-3,3]])
c=a.dot(b)
print(c)

#Transpose 
a = np.array([[1,2],[99,8],[878,-25]])
print(a  ,a.transpose())

# access matrix through row and columns 
a=np.array([2,4,8,16,32,64])
print("a[0] = ", a[0])
print("a[0] = " ,a[2])
print("a[-1]= " ,a[-1])

# access in 2D matrix
a=np.array([[1,58,85,987],[98,75,32,49],[75,35,15,95],[14,58,93,28]])
print("a[0][0]",a[0][0])
print("a[1][3]",a[1][3])
print("a[-1][-1]",a[-1][-1])

# access Row of a matrix
a=np.array([[1,58,85,987],[98,75,32,49],[75,35,15,95],[14,58,93,28]])
print("a[0] = " ,a[0])
print("a[-1] = " ,a[-1])
print("a[2] =" ,a[2])

# access Columns of a matrix 
a=np.array([[1,58,85,987],[98,75,32,49],[75,35,15,95],[14,58,93,28]])
print("a[:,0]",a[:,0])
print("a[:,3] ", a[:,3])
print("a[:,-1]", a[:,-1])

#slicing in 1D matrix
a=np.array([2,4,8,16,32,64])
print(a[2:5])
print(a[:-5])
print(a[5:])
print(a[::-1])
print(a[1::2])

# slicing in 2D matrix
a=np.array([[1,58,85,987],[98,75,32,49],[75,35,15,95],[14,58,93,28]])
print(a[:,:])
print(a[:3, :2])
print(a[:,2])
print(a[2,2:5])

