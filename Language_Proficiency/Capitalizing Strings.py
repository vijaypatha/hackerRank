#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.
'''


# In[23]:


first_name = input("Enter your first name : lower case ")
last_name = input("Enter your last name : lower case ")
print("Your name is ",first_name.capitalize() + " " + last_name.capitalize())


# In[27]:


name = input("input your full name: ")
print(name.capitalize())


# In[28]:


#However i want both first and last name to be capitalize 


# In[30]:


name = input("input your full name: ")
name.title()


# In[31]:


def solve(s):
    return s.title()
solve('hello world')


# In[34]:


def solve(s):
    return s.title()
solve(input("input your full name: "))


# In[39]:


import string 
print(string.capwords(input(), ' '))


# In[ ]:




