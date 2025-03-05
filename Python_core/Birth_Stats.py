#!/usr/bin/env python
# coding: utf-8

# In[11]:


occurances = 0

with open("../data/names.csv", "r") as file:
    for line in file:
        splitit = line.strip().split(",")
        if splitit[2] == "Year":
            continue
        year = int(splitit[2])
       # print(splitit)
       # break
        if splitit[1] == "Max" and year >= 1950 and year <= 2000 and splitit[3] == "M" and splitit[4] == "CA":
            occurances = occurances + int(splitit[5])
            
print(occurances)
        


# In[ ]:





# In[ ]:




