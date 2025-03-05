#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Python3 code to demonstrate each occurrence frequency using naive method 
# initializing string 
given_str = "Hey Ravindra, what's up?"

# using naive method to get count 
# of each element in string 
count_freq = {} 

for i in given_str:
    if i in count_freq:
        count_freq[i] += 1
    else:
        count_freq[i] = 1
        
# printing result
print ("Count of all characters in the given string is :\n " + str(count_freq)) 


# In[ ]:





# In[ ]:




