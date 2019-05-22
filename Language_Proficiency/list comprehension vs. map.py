#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element is the result 
of some operations applied to each member of another sequence or iterable, 
or to create a subsequence of those elements that satisfy a certain condition.
'''


# In[ ]:


'''
A list comprehension consists of brackets containing an expression followed 
by a for clause, then zero or more for or if clauses. 

[expression, for clause, or 2nd for clause, or if clause]

'''


# In[4]:


# Finding squares using lists comprehensions

numbers = [1, 2, 3, 4]
#[expression, for clause, or for clause, or if clause]
squares = [n**2 for n in numbers]

print(squares)  # Output: [1, 4, 9, 16]


# In[ ]:


'''
Map applies a function on all the elements of specified iterable and return map object. 
'''


# In[6]:


def multiply2(x):
    return(x ** 2)

result = map(multiply2, [1,2,3,4])

print(list(result)) #coverting map to list


# In[15]:





# In[ ]:




