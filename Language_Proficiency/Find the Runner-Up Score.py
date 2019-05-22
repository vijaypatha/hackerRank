#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Find the Runner-Up Score!

#Given list is [2,3,4,5,6]. The maximum score is 6, second maximum is 5 . Hence, we print 5 as the runner-up score.


# In[25]:


#Method 1: Max - 1
listA = [1,22,4]
print(max(listA)-1)
#Method 1 did not work


# In[69]:


listA = [1,22,22,10,4]
print(listA)


# In[70]:


#Method 2: Remove the max and then print the next max
listA = [1,22,22,10,4]
max_el = max(listA)
listA.remove(max(listA))
print(max(listA))
#Results: This approch will fail if there couple of same max elements in the lists


# In[72]:


#Method 2.2: Adding a while loop to address this issue 
listA = [1,22,22,10,11,4]
max_el = max(listA)
while max(listA) == max_el:
    listA.remove(max(listA))
print(max(listA))


# In[67]:


#Testing 2.2
a_list = [2,3,6,6,5]
max_el = max(a_list)
while max(a_list) == max_el:
    a_list.remove(max(a_list))
print(max(a_list))


# In[ ]:




