#!/usr/bin/env python
# coding: utf-8

# In[3]:


#twitter bot - Politician

import random

print(random.randint(0,5))  #randint() to generate random numbers in the given range.


# In[4]:


part1 = ["Putin,", "Hillary,", "Obama", "Fake News,", "Mexico,", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["no talent,", "on the way down,", "really poor numbers,", "nasty tone,", "looking like a fool,", "bad hombre,"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd.", "will pay for the wall."]
part4 = ["So sad", "Apologize", "So true", "Media won't report", "Big trouble", "Fantastic job", "Stay tuned"]


# In[6]:


best_match = [part1, part2, part3, part4]
print(best_match)


# In[31]:


#tweeter generator

best_tweet = []

for part in best_match:
   # print(len(part))
    r = random.randint(0, len(part) -1)
  #  print(part[r])
  #  print(r)
    best_tweet.append((part[r]))

# print(best_tweet)
print(" ".join(best_tweet) + "!")


# In[ ]:




