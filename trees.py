#!/usr/bin/env python
# coding: utf-8

# In[54]:


class Node(object):
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
        
    def inorder(root):
        if root:
            #left - root - right
            inorder(root.left)
            print(root.value)
            inorder(root.right)
    
    def postorder(root):
        if root:
            #left - right - root
            postorder(root.left)
            postorder(root.right)
            print(root.value)
             
    def preorder(root):
        if root:
            #root - left - right
            print(root.value)
            preorder(root.left)
            preorder(root.right)
            
    def count_nodes(root):
        if root is None:
            return 0
        return (1+ count_nodes(root.left)+ count_nodes(root.right))
    
    def height(root):
        if root is None:
            return -1
        
        left_height=height(root.left)
        right_height=height(root.right)
        
        return (1 + max(left_height,right_height))
    
        
            
            


# In[55]:


root=Node(1)


# In[56]:


root.left=Node(2)


# In[57]:


root.right=Node(3)


# In[58]:


print(root.left.value)


# In[59]:


print(root.right.value)


# In[60]:


print(root.value)


# In[ ]:




