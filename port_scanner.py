#!/usr/bin/env python
# coding: utf-8

# In[7]:


import socket
 
s = socket.socket()
 
result = s.connect_ex(('shippinglot.com', 22))
 
if(result == 0):
  print('Port is open')
else:
  print('Port is closed')


# In[ ]:





# In[ ]:




