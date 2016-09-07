
# coding: utf-8

# In[8]:

# Problem Set 1
# Name: SC You
# Time: about an hour

#Write a program that computes and prints the 1000th prime number. 

#initialize the variables
i = 2
primetuple = (2,)


#get tuple of 1000 prime numbers
while (len(primetuple)<1000):
    for k in primetuple:
        if i % k == 0:
            i = i+1
     
    primetuple = primetuple + (i,)
    i=i+1    
    
#print the last prime number, which is the 1000th
print (primetuple[-1])

