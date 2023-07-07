#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns


# ## Importing the dataset

# In[ ]:


pd.set_option('display.max_colwidth', 1000)


# In[ ]:


df = pd.read_csv('each_ball_records.csv')
match1 = df[df['match_no'] == 1]
match1


# In[ ]:


df.shape


# In[ ]:


match1.shape


# ## Analysis of match1

# ## Task 1.1: How many balls played by inning 1 and 2

# In[ ]:


balls_played1 = len(match1[match1['inningno'] == 1])
balls_played2 = len(match1[match1['inningno'] == 2])
print(balls_played1)
print(balls_played2)


# ## Task 1.2: Find out how many wickets took in inning1 and 2

# In[ ]:


match1['outcome'].unique()


# In[ ]:


wickets1 = len(match1[(match1['inningno'] == 1) & (match1['outcome'] == 'w')])
wickets2 = len(match1[(match1['inningno'] == 2) & (match1['outcome'] == 'w')])
print(wickets1)
print(wickets2)


# In[ ]:


match1['score']=match1['outcome'].replace(['0', '1lb', '1', '4', 'w', '6', '1nb', '4lb', '2', '1b', '1wd',
       '2nb'],[0,1,1,4,0,6,1,4,2,1,1,2])
match1


# In[ ]:


## 7 wickets took in inning1 and 5 inning2


# ## Task 1.3: How many wide balls in inning 1 and 2

# In[ ]:


wide1 = len(match1[(match1['inningno'] == 1) & (match1['outcome'] == '1wd')])
wide2 = len(match1[(match1['inningno'] == 2) & (match1['outcome'] == '1wd')])
print(wide1)
print(wide2)


# ## Task 1.4: Score of both teams

# In[ ]:


## In outcome column, only w is replace by 0 and other have integer that will tell use score


# In[ ]:


data1 = match1
data1


# In[ ]:


data1['Score'] = data1['outcome'].replace(['0', '1lb', '1', '4', 'w', '6', '1nb', '4lb', '2', '1b', '1wd',
       '2nb'], [0,1,1,4,0,6,1,4,2,1,1,2])
data1


# In[ ]:


score_data = data1.groupby('inningno').agg(scored = ('outcome', 'sum')).reset_index()
score_data


# In[ ]:


## Team1 scores 178 runs and Team2 scores 182 runs


# ## Task 1.5: How many catches in inning 1 and inning 2

# In[ ]:


inning1_catch = match1[(match1['comment'].str.contains('Wicket - c.*b')) & (match1['inningno'] == 1)]
inning2_catch = match1[(match1['comment'].str.contains('Wicket - c.*b')) & (match1['inningno'] == 2)]
print(len(inning1_catch))
print(len(inning2_catch))


# In[ ]:


match1[(match1['comment'].str.contains('Wicket .*b'))].shape 


# In[ ]:


## it means 5 players catch out in inning1 and 4 were in inning2.


# ## Task 1.6: How many run out in inning 1 and inning 2

# In[ ]:


runout1 = match1[(match1['inningno'] == 1) & (match1['comment'].str.contains("Wicket - runout"))]
runout2 = match1[(match1['inningno'] == 2) & (match1['comment'].str.contains("Wicket - runout"))]
print(len(runout1))
print(len(runout2))


# In[ ]:


## it means there were no runout in inning1 and no runout in inning 2


# ## Task 1.7: How many stump out in inning 1 and inning 2

# In[ ]:


stumpout1 = match1[(match1['inningno'] == 1) & (match1['comment'].str.contains("Wicket - b"))]
stumpout2 = match1[(match1['inningno'] == 2) & (match1['comment'].str.contains("Wicket - b"))]
print(len(stumpout1))
print(len(stumpout2))


# In[ ]:


## it means 2 players were stump out in inning 1 and 1 was in inning2


# In[ ]:




