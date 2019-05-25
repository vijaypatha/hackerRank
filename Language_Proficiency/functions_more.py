#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a function Double the list [1,2,3,4] to [1,4,9,16]


# In[7]:


def double(li):
    new_list = []
    for i in range(0, len(li)):
        result = li[i] * li[i]
        new_list.append(result)
    return new_list
print(double([1,2,3,4]))


# In[10]:


def dbling(li):
    dblist = []
    for i in range(0, len(li)):
        dub = li[i] * li[i]
        dblist.append(dub)
    return dblist
print(dbling([1,2,3,54]))


# In[ ]:


'''
Have the function CheckNums(num1,num2) take both parameters being 
passed and return the string true if num2 is greater than num1, 
otherwise return the string false. 
If the parameter values are equal to each other then return the string -1. 

'''


# In[17]:


def CheckNums(num1,num2):
    if num1 > num2:
        return 'True'
    elif num1 == num2:
        return '-1'
    else:
        return 'False'
# keep this function call here  
print(CheckNums(22,300))


# In[21]:


'''
Find the longest word in the string 

feature = 'I love you'
label = love
'''


# In[45]:


longword = 'i love you'
lw = longword.split(' ')
print (max(lw, key=len))


# In[50]:


def longword(lw):
    lword = lw.split(' ')
    return max(lword, key = len)
longword('I Love You 44@@# 5553344')


# In[ ]:


# find even values from a list 
# then find the doubles of the evens
# reduce 

# using both named and anonymous function


# In[11]:


alist = [1,3,4,5,6,7,33,22]
evens = list(filter(lambda n : n % 2 == 0,alist))
print(evens)
doubles = list(map(lambda i : i * 2, evens))
print(doubles)


# In[16]:


alist = [1,3,4,5,6,7,33,22]
even2 = list(map(lambda i : i % 2 == 0, alist))
print(even2)


# In[20]:


list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
print(list(map(lambda x,y : x + y, list_a, list_b)))


# In[22]:


list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
print(list(map(lambda x,y : x * y, list_a, list_b)))


# In[26]:


list_a = [1, 2, 3]
list_b = [10, 20, 30]
  
print(list(map(lambda x,y : x / y, list_a, list_b)))


# In[33]:


dist = int(input("how many mile?: "))
kms = dist * 1.6
print('{} miles is'.format(dist),kms, 'kms')


# In[ ]:




