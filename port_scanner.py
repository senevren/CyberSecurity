#!/usr/bin/env python
# coding: utf-8

# In[8]:


import socket
 
s = socket.socket()
 
result = s.connect_ex(('example.com', 80))
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')


# In[ ]:





# In[ ]:




