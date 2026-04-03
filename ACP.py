import numpy as np

arr=np.array([0,3,6,9])

new=np.where(arr%2 ==0, -1, arr) #If number in arr is even, replace with -1, otherwise leave it as arr
print(new)


arr2=np.array([1,2,3,4,5,6,7,8])
newarr=arr2.reshape(2,4)
print(newarr)

sum=0
for i in arr2:
    sum=sum+i
print(sum)



