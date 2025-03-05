#!/usr/bin/env python
# coding: utf-8

# In[8]:


# New and old prizes are mixed! Scroll through the items in the chaos list. 
# With a new price, simply drag the new value from the string and append it to the order list. 
# With an old price, however, you get the old value, calculate the new price and add this value to the order list.
# Finally, output the complete order list, which only contains new prices (and only numbers!).

chaos =["old price: 40", "new price: 21", "old price: 29", "old price: 50", "new price: 101"]
order = []

for i in chaos:
    price = int(i.split(": ")[1])
    #print(price)
    
    if "old" in i:
        if price <= 20:
            price = price * 0.8
        elif price <=50:
            price = price * 0.6
        else:
            price = price * 0.4
    order.append(price)
    
print(order)


# In[ ]:





# In[ ]:




