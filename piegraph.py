#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn
import matplotlib.pyplot as plt

def piegraph(labels = [],sizes = []):
    explode = (0, 0.1, 0, 0)  

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  

    plt.savefig('Demo_official.jpg')
    plt.show()
    fig1
    
    


# In[5]:


piegraph(['65-70','70-75','75-80','80-85'],[15, 30, 45, 10])


# In[ ]:




