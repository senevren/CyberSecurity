#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scapy.all import *
 
for pkt in sniff(iface='en0', count=5):
    print('Packet: ' + str(pkt.summary()) + '\n')

