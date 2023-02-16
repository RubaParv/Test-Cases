#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
from ipywidgets import widgets, HBox, Output, interactive


CandiList=pd.read_excel("D:\\Hackathon\\Files Used\\Sample Synthetic Candidates Table.xlsx")


# In[46]:


CandiList


# In[47]:


# Initialize Priority Tag as 0 to All
CandiList['Priority Tag']=0


# In[48]:


# Give priority tag to candidates who are in the same city and with at least 50% match with training, skills or knowledge
# requirements

CandiList.loc[CandiList['Same City?'] == 'Yes', 'Priority Tag'] = 1


# In[49]:


# Give priority tag also to candidates from another cities, and who are willing to relocate, and with at least 50% match with 
# training, skills or knowledge requirements

CandiList.loc[(CandiList['Same City?'] == 'No') & (CandiList['Will Relocate To Rural Area?'] == 'Yes') & (CandiList['At least 50% req. match with training, skill or knowledge?'] == 'Yes'), 'Priority Tag'] = 1


# In[50]:


CandiList


# In[51]:


# Filter data of priority and non-priority groups
prioCandi=CandiList[CandiList['Priority Tag']==1]
nonprioCandi=CandiList[CandiList['Priority Tag']==0]


# In[52]:


# Reorder the priority groups based on their Regular Evaluation Score (Highest to Lowest Score)
dfp=prioCandi.sort_values(['Regular Evaluation Score'], ascending=[False])


# In[53]:


# Reorder the non-priority groups based on their Regular Evaluation Score (Highest to Lowest Score)
dfnp=nonprioCandi.sort_values(['Regular Evaluation Score'], ascending=[False])


# In[54]:


# Join the two groups again with their reorders
frame=[dfp,dfnp]
sortedCandidates=pd.concat(frame)
sortedCandidates


# In[63]:


# Show the top 10 candidates now
Top10=sortedCandidates.head(10)
Top10List=Top10[['Candidate ID','First Name','Last Name','Email','Gender','Category']]
Top10List


# In[64]:


def click(b):
    with out:
        print (Top10List)

out=widgets.Output()
button=widgets.Button(description='FindTop10Candidates')
button.on_click(click)
display(out)
display(button)


# In[65]:


Top10List


# In[ ]:




