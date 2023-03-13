#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[19]:


import os

# Get current working directory
cwd = os.getcwd()

# Print current working directory
print("Current working directory:", cwd)

os.chdir('/Users/thanhnguyen/Desktop/Data_analysis/DE_k2/project2')

# Get current working directory
cwd = os.getcwd()

# Print current working directory
print("Current working directory:", cwd)


# In[3]:


nobel = pd.read_csv('nobel.csv')
nobel.head()


# USA dominance, visualized

# In[8]:


nobel['us'] = nobel['birth_country'] == 'United States of America'
nobel['decade'] =(nobel['year']//10)*10 

us = nobel.groupby('decade')['us'].mean().reset_index()
us
# us = nobel[nobel['birth_country'] == 'United States'].groupby('decade').agg({'full_name': 'count', 'us_born_winner': 'mean'}).reset_index()
# us.columns = ['decade', 'count', 'us']


# In[9]:


#plot
import seaborn as sns
# Set the plot style
sns.set_style("ticks", {"axes.facecolor": "#F5F5F5", "grid.color": "white", "grid.linestyle": "-", "grid.linewidth": 1.5})

plt.figure(figsize=(12,8))


ax = sns.lineplot(data=us, x='decade', y='us', color='blue')

#ax.fill_between(nobel['decade'], nobel['us']+0.01,nobel['us']-0.01, alpha=0.2, color='blue')

plt.xlabel('decade', fontsize=16)
plt.ylabel('us_born_winner',fontsize=16) 
mean_value = us['us'].mean()
# Add grid lines
plt.grid(True)


                  


# What is the gender of a typical Nobel Prize winner?

# In[10]:


nobel['female'] = nobel['sex'] == 'Female'
nobel.head()


# In[11]:



female_nobel = nobel.groupby(['decade','category'])['female'].mean().reset_index()
type(female_nobel)


# In[12]:



sns.set_style("ticks", {"axes.facecolor": "#F5F5F5", "grid.color": "white", "grid.linestyle": "-", "grid.linewidth": 1.5})

plt.figure(figsize=(12,8))
ax = sns.lineplot(data=female_nobel, x='decade', y='female', hue='category', palette='colorblind')
plt.xlabel('decade', fontsize=16)
plt.ylabel('female_winner',fontsize=16) 

# Add grid lines
plt.grid(True)


# Repeat laureates: For most scientists/writers/activists a Nobel Prize would be the crowning achievement of a long career. But for some people, one is just not enough, and few have gotten it more than once. Who are these lucky few?

# In[13]:


#count the number of time a full name of scientists/writers/activists appear
appear = nobel.groupby('full_name').count().reset_index()
#check if the number of time he/she got the nobel is more than on, year is choose to check because it is distinct
repeat_laureats = appear[appear['year']>1]
print("Repeat Laureates:")
for i, name in enumerate(repeat_laureats.full_name):
    print(f"{i+1}. {name}")


# How old are you when you get the prize?

# In[14]:



# Convert birth_date from string to datetime
nobel['birth_date'] = pd.to_datetime(nobel['birth_date'], format='%Y-%m-%d', errors='coerce')
# Get birth year to calculate age
nobel['birth_year'] = nobel['birth_date'].dt.year

# Calculate the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_year']

# Plot the age of Nobel Prize winners over time
sns.set(style="darkgrid")
sns.lmplot(x='year', y='age', data=nobel, height=4.5, aspect=2)

# Add axis labels and a title
sns.set(font_scale=1.5)
plt.xlabel("Year")
plt.ylabel("Age")
plt.title("Age of Nobel Prize Winners Over Time")

# Display the plot
plt.show()


# Age differences between prize categories

# In[15]:


sns.set(style="darkgrid", font_scale=1.2)
fig, axes = plt.subplots(nrows=5, figsize=(10, 40), sharex=True)
categories = nobel['category'].unique()
for i, category in enumerate(categories):
    category_df = nobel[nobel['category'] == category]
    sns.regplot(x='year', y='age', data=category_df, ax=axes[i], scatter_kws={'color': 'blue', 'alpha': 0.3}, line_kws={'color': 'red'})
    axes[i].set_title('category='+category, fontsize=14)
    axes[i].set_xlabel('')
    axes[i].set_ylabel('Age', fontsize=12)
    axes[i].set_xlim(1900, 2020)
plt.suptitle('Age of Nobel Prize Winners Over Time by Category', fontsize=18, y=0.95)

# Adjust the spacing between subplots
plt.tight_layout()

# Display the plot
plt.show()


# In[ ]:




