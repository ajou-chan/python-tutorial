
# coding: utf-8

# In[11]:

i = 0
N = 3
primelist = [2]
trueprime = 1

while (len (primelist)<1000):
    for prime in primelist:
        if N % prime == 0:
            trueprime = 0
            N = N+1
            break
    if trueprime ==1:
        primelist = primelist + [N,]
        N = N+1
    trueprime = 1
    
print(primelist[-1])

