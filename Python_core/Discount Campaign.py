#!/usr/bin/env python
# coding: utf-8

# In[7]:


#A business women wants to start a discount campaign in her shop to boost her business. 
#Of course, she has something to program for you again. 
#You should simplify the calculation of the reduced prices with an if-elif-else structure. Note the following:

#Items costing between 0 and 20 thalers (inclusive) will be reduced by 20%; 
#items costing between 20 (not inclusive) and 50 thalers (inclusive) will be reduced by 40%. 
#All other items, i.e. items costing more than 50 thalers, will be reduced by 60%.

price = 34 #enter the price

if price <=20:
    price = price * 0.8
elif price <= 50:
    price = price * 0.6
else:
    price = price * 0.4

print(price)


# In[13]:


# Now calculate for each of the old prices from the prices list the appropriate reduced prices 
#and save them in the new_prices list. Finally output this list.

prices = [4, 53, 23, 50, 74]
new_prices = []

for price in prices:
    if price <=20:
        price = price * 0.8
    elif price <= 50:
        price = price * 0.6
    else:
        price = price * 0.4
        
    new_prices.append(price)
    
    
print(new_prices)


# In[ ]:




