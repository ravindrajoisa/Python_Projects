#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Elevator Prog

list_weight = [34, 56, 65, 55, 76, 99] 
tot_weight = 0
for element in list_weight:
    tot_weight = tot_weight + element
 #   print(tot_weight)
                                 #Elevator program logic
    if tot_weight > 300:
        print("Max weight allowed is 300. Elevator overloaded. Walk out")
        break


