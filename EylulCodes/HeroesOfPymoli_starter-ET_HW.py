#!/usr/bin/env python
# coding: utf-8

# ### Note
# * Instructions have been included for each segment. You do not have to follow them exactly, but they are included to help you think through the steps.

# In[2]:


# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
file_to_load = "purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data_pd = pd.read_csv(file_to_load)
purchase_data_df = pd.DataFrame(purchase_data_pd)
purchase_data_df.head()


# ## Player Count

# * Display the total number of players
# 

# In[3]:


# Total Number of Players
total_players = purchase_data_pd["SN"].count()
total_players


# In[4]:


# Number of unique items

Unique_item_id = len(purchase_data_pd["Item ID"].unique())
Unique_item_id


# In[5]:


# Total Purchase count

total_purchases = purchase_data_pd["Purchase ID"].count()
total_purchases


# In[6]:


# Total Revenue

total_revenue = purchase_data_pd["Price"].sum()
total_revenue


# In[7]:


# Average Price

#Alternative: Average_Price = purchase_data_pd["Price"].mean()

Average_Price = total_revenue/total_purchases
Average_Price


# In[8]:


# Display of the data frame

P_Analysis_df = pd.DataFrame([{"Number of Unique Items": Unique_item_id,
                               "Average Price": Average_Price,
                               "Number of Purchases": total_purchases,
                              "Total Revenue":total_revenue}])
P_Analysis_df


# In[9]:


P_Analysis_df["Average Price"] = P_Analysis_df["Average Price"].map("${:,.2f}".format)
P_Analysis_df["Total Revenue"] = P_Analysis_df["Total Revenue"].map("${:,.2f}".format)
P_Analysis_df


# ## Purchasing Analysis (Total)

# * Run basic calculations to obtain number of unique items, average price, etc.
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame
# 

# In[10]:


#show data frame again

purchase_data_df.head()


# ## Gender Demographics

# * Percentage and Count of Male Players
# 
# 
# * Percentage and Count of Female Players
# 
# 
# * Percentage and Count of Other / Non-Disclosed
# 
# 
# 

# In[11]:


gender_count_df = purchase_data_df.groupby(by='Gender').count()
gender_count_df


# In[12]:


Sum = purchase_data_df['Gender'].count()
Sum


# In[13]:


Droped_Sum_df = gender_count_df.drop(columns = ['SN' , 'Age' , 'Item ID' , 'Item Name', 'Price'])
Droped_Sum_df


# In[14]:


new_df = gender_count_df / Sum
new_df


# In[15]:


Droped_new_df = new_df.drop(columns = ['SN' , 'Age' , 'Item ID' , 'Item Name', 'Price'])
Droped_new_df


# In[16]:


Droped_new_df['Purchase ID'] = Droped_new_df['Purchase ID'].mul(100).astype(int).astype(str).add('%')
Droped_new_df


# In[17]:


purchase_data_df.head()


# In[18]:


cut_sum = purchase_data_df.drop(columns = ['SN' , 'Age' , 'Item ID' , 'Item Name', 'Price'])
cut_sum


# In[19]:


Sum_df_I = cut_sum.groupby(by='Gender').count()
Sum_df_I


# In[20]:


New_df_display_df = pd.merge(Sum_df_I, Droped_new_df, on = 'Gender' , how = 'outer')
New_df_display_df


# In[21]:


Final_df = New_df_display_df.rename(columns = {"Purchase ID_x": "Total Count", "Purchase ID_y": "Percentage of Players"})
Final_df


# 
# ## Purchasing Analysis (Gender)

# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. by gender
# 
# 
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[22]:


purchase_data_df.head()


# In[23]:


Gender_Grouped_df = purchase_data_df.groupby(['Gender'])
Gender_Grouped_df


# In[24]:


Purchase_Count = Gender_Grouped_df["Purchase ID"].count()

Purchase_Count


# In[25]:


total_value = Gender_Grouped_df['Price'].sum()
total_value


# In[26]:


# Total purchase with dollar sign

sign_total_value  = total_value.map("${:,.2f}".format)
sign_total_value


# In[27]:


# avg purchase 

avg_purchase = Gender_Grouped_df['Price'].mean()
avg_purchase

avg_purchase_dec = avg_purchase.map("${:,.2f}".format)
avg_purchase_dec


# In[28]:


# Avg Total Purchase per Person

Group_by_person = purchase_data_df.groupby(['Gender', 'SN'])
Group_by_person


# In[29]:


per_person = Group_by_person["Price"].sum()
per_person


# In[30]:


Sum_pp = per_person.groupby('Gender').sum()
Sum_pp


# In[31]:


count_pp = per_person.groupby('Gender').count()
count_pp


# In[32]:


Normalized = Sum_pp / count_pp
Normalized

# Make it with $ sign

Normalized_d = Normalized.map("${:,.2f}".format)
Normalized_d


# In[33]:


organized_df = pd.DataFrame()
organized_df["Purchase Count"] = Purchase_Count
organized_df["Average Purchase Price"] =  avg_purchase_dec
organized_df["Total Purchase Value"] =  sign_total_value
organized_df["Avg Total Purchase per Person"] = Normalized_d

organized_df


# In[ ]:





# ## Age Demographics

# * Establish bins for ages
# 
# 
# * Categorize the existing players using the age bins. Hint: use pd.cut()
# 
# 
# * Calculate the numbers and percentages by age group
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: round the percentage column to two decimal points
# 
# 
# * Display Age Demographics Table
# 

# In[34]:


purchase_data_df.head()


# In[35]:


purchase_data_df["Age"].max()


# In[36]:


purchase_data_df["Age"].min()


# In[37]:


bins = [0, 9.99, 14.99, 19.99, 24.99, 29.99, 34.99, 39.99, 999]


# In[38]:


# naming my bins

Group_names = ['<10' , '10-14' , '15-19' , '20-24' , '25-29', '30-34' , '35-39' , '40+' ]


# In[43]:


purchase_data_df['Age Group'] = pd.cut(purchase_data_df.Age,bins, labels = Group_names)
purchase_data_df.head()


# In[45]:


purchase_data_df = purchase_data_df.groupby(['Age Group'])


# In[51]:


count_table = purchase_data_df.count()
count_table


# In[68]:


Drop_age_count = count_table.drop(columns = ['SN', 'Age' , 'Gender' , 'Item ID', 'Item Name', 'Price'])
Drop_age_count


# In[91]:


new_table_age = (count_table / total_players)*100
new_table_age


# In[92]:


Drop_Percentages = new_table_age.drop(columns = ['Age', 'Gender' , 'Item ID', 'Item Name' , 'Price' , 'SN'])
Drop_Percentages


# In[93]:


Drop_Percentages['Purchase ID'] = Drop_Percentages['Purchase ID'].map("{:,.2f}%".format)
Drop_Percentages


# In[94]:


Age_display_df = pd.merge(Drop_Percentages, Drop_age_count, on = 'Age Group' , how = 'outer')
Age_display_df


# In[98]:


Final_Age_df = Age_display_df.rename(columns = {"Purchase ID_x": "Percentage of Players", "Purchase ID_y": "Total Count"})
Final_Age_df


# ## Purchasing Analysis (Age)

# * Bin the purchase_data data frame by age
# 
# 
# * Run basic calculations to obtain purchase count, avg. purchase price, avg. purchase total per person etc. in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display the summary data frame

# In[102]:


sum_table = purchase_data_df.sum()
sum_table


# In[ ]:





# ## Top Spenders

# * Run basic calculations to obtain the results in the table below
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the total purchase value column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Popular Items

# * Retrieve the Item ID, Item Name, and Item Price columns
# 
# 
# * Group by Item ID and Item Name. Perform calculations to obtain purchase count, item price, and total purchase value
# 
# 
# * Create a summary data frame to hold the results
# 
# 
# * Sort the purchase count column in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the summary data frame
# 
# 

# In[ ]:





# ## Most Profitable Items

# * Sort the above table by total purchase value in descending order
# 
# 
# * Optional: give the displayed data cleaner formatting
# 
# 
# * Display a preview of the data frame
# 
# 

# In[ ]:




