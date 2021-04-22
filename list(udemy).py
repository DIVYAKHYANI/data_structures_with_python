#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Creating a list and accessing the list


# In[2]:


hello=[1,20,'bye',0.5]


# In[3]:


print(type(hello))


# In[4]:


print(hello)


# In[5]:


print(hello[0])


# In[6]:


print(hello[9])


# In[7]:


print(hello[:2])


# In[8]:


print(hello[-1])


# In[9]:


print(hello[-2])


# In[10]:


#adding elements(append,insert,extend)


# In[11]:


hello.append([10,29])


# In[12]:


print(hello)


# In[13]:


hello.insert(0,30)#0th index


# In[14]:


print(hello)


# In[15]:


hello.extend([91,22])


# In[16]:


print(hello)


# In[17]:


#deleting Elements(remove,pop,clear)


# In[19]:


hello.pop()#removes the last element(done twice)


# In[20]:


print(hello)


# In[21]:


hello.remove('bye')


# In[22]:


print(hello)


# In[23]:


hello.clear()#clears the complete list


# In[24]:


print(hello)


# In[25]:


#other functions (index,count,sort)


# In[30]:


hello=[1,20,0.5,10]


# In[31]:


hello.sort()


# In[32]:


print(hello)


# In[34]:


print(hello.count(10))


# In[35]:


print(hello.index(10))


# In[ ]:




