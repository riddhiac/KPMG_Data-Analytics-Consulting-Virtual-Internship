#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the required libraries

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[119]:


url = '/Users/riddhi/Documents/DS/KPMG/KPMG_VI_New_raw_data_update_final.xlsx'

transactions = pd.read_excel(url, sheet_name='Transactions')
customer_demographic = pd.read_excel(url, sheet_name='CustomerDemographic')
customer_add = pd.read_excel(url, sheet_name='CustomerAddress')
new_customer_lists = pd.read_excel(url, sheet_name='NewCustomerList')


# # 1. Exploring the Transactions Dataset

# In[3]:


transactions.head()


# In[4]:


transactions.info()


# The values in the **product_first_sold_date** columns are not correct as it shows everything happening the same day at different times. 

# In[11]:


#convert date columns from integer to datetime
transactions['product_first_sold_date'] = pd.to_datetime(transactions['product_first_sold_date'], unit='s')
transactions['product_first_sold_date'].head()


# In[13]:


transactions.shape


# In[14]:


print("Rows : ", transactions.shape[0])
print("Columns : ", transactions.shape[1])


# In[15]:


transactions.describe()


# ### Explore missing values
# 

# In[16]:


# returns the bool value if there is any missing value in dataset
transactions.isna().values.any()


# In[17]:


transactions.isna().sum()


# ##### We can decide to drop missing values depending on the objective of our analysisa as there are 2000 entries in our dataset.

# In[28]:


# transactions.dropna(subset=['online_order','brand','product_line','product_class','product_size','standard_cost','product_first_sold_date'])
#    __OR__
# transactions = transactions[-transactions["online_order"].isnull()]
#    __OR__
transactions.dropna(inplace=True)
transactions


# In[29]:


#to check for unique values

transactions.nunique()


# In[30]:


transactions.duplicated().sum()


# In[31]:


transactions[transactions.duplicated()]  #to check for duplicate values


# In[32]:


transactions.columns


# In[43]:


transactions['online_order'].value_counts()


# In[44]:


transactions['order_status'].value_counts()


# In[45]:


transactions['brand'].value_counts()


# In[46]:


transactions['product_line'].value_counts()


# In[47]:


transactions['product_class'].value_counts()


# In[48]:


transactions['product_size'].value_counts()


# #### All the columns appear to have consistent and correct information.
# 

# In[197]:


# will add "profit" column. Formulae = List price - Standard Cost

transactions["profit"] = transactions["list_price"] - transactions["standard_cost"]
transactions.head()


# In[51]:


transactions.isnull().values.any()


# # 2. Exploring New Customer List Dataset

# In[52]:


new_customer_lists.head()


# In[53]:


new_customer_lists.info()


# In[54]:


new_customer_lists.nunique()


# In[55]:


new_customer_lists['gender'].value_counts()


# In[56]:


new_customer_lists[new_customer_lists.gender == 'U']


# In[61]:


index_name = new_customer_lists[new_customer_lists.gender == "U"].index
new_customer_lists.drop(index_name, inplace = True)
new_customer_lists[new_customer_lists.gender == 'U']


# In[174]:


# Drop Unnamed Column
cols = ['Unnamed: 16','Unnamed: 17','Unnamed: 18','Unnamed: 19','Unnamed: 20','Rank','Value']
new_customer_lists = new_customer_lists.drop(cols, axis=1)


# In[64]:


new_customer_lists.isna().values.any()


# In[65]:


new_customer_lists.isna().sum()


# In[67]:


new_customer_lists.duplicated().sum()


# There are no duplicate values in the dataset
# 

# In[176]:


new_customer_lists['year'] = pd.DatetimeIndex(new_customer_lists['DOB']).year
new_customer_lists['month'] = pd.DatetimeIndex(new_customer_lists['DOB']).month
new_customer_lists['age'] = 2021 - new_customer_lists['year']

new_customer_lists.head()


# In[177]:


new_customer_lists[new_customer_lists.age >= 100]


# In[71]:


new_customer_lists['state'].value_counts()


# In[179]:


new_customer_lists['state'] = new_customer_lists['state'].replace('QLD','Queensland')
new_customer_lists['state'] = new_customer_lists['state'].replace('NSW','New South Wales')
new_customer_lists['state'] = new_customer_lists['state'].replace('VIC', 'Victoria')
new_customer_lists.head()


# In[76]:


new_customer_lists['state'].value_counts()


# In[130]:


new_customer_lists['country'].value_counts()


# In[131]:


new_customer_lists['owns_car'].value_counts()


# In[132]:


new_customer_lists['job_title'].value_counts()


# In[133]:


new_customer_lists['job_industry_category'].value_counts()


# In[134]:


new_customer_lists['wealth_segment'].value_counts()


# # 3. Exploring Customer Demographic Data Set¶
# 

# In[87]:


customer_demographic.head()


# In[88]:


customer_demographic.info()


# In[93]:


customer_demographic.drop('default', axis=1,inplace=True)
customer_demographic.head()


# In[94]:


print("Rows: ", customer_demographic.shape[0])
print("Columns: ", customer_demographic.shape[1])


# In[95]:


customer_demographic.describe()


# In[96]:


customer_demographic.isna().values.any()


# In[99]:


customer_demographic.isna().sum()


# In[100]:


customer_demographic.dropna(subset = ['DOB','job_title','job_industry_category','tenure'])


# In[213]:


customer_demographic.nunique()


# In[214]:


customer_demographic.gender.unique()


# In[225]:


customer_demographic['gender'] = customer_demographic['gender'].replace(['F, Femal'], 'Female')
customer_demographic['gender'] = customer_demographic['gender'].replace('M', 'Male')
customer_demographic['gender'] = customer_demographic['gender'].replace('U', 'Unspecified')


# In[226]:


customer_demographic['gender'].value_counts()


# In[170]:


customer_demographic['year'] = pd.DatetimeIndex(customer_demographic['DOB']).year
customer_demographic['month'] = pd.DatetimeIndex(customer_demographic['DOB']).month
customer_demographic['age'] = 2021 - customer_demographic['year']


# In[160]:


customer_demographic.head()


# In[161]:


customer_demographic[customer_demographic.age > 100]


# **customer_id - 34** : Age is coming **178** which is not a correct age hence will drop this value.
# (Max age is 122)

# In[162]:


customer_demographic.drop(33,inplace=True)


# In[112]:


customer_demographic[customer_demographic.age > 100]


# In[113]:


customer_demographic['gender'].value_counts()


# In[114]:


customer_demographic['job_title'].value_counts()


# In[115]:


customer_demographic['job_industry_category'].value_counts()


# In[116]:


customer_demographic['wealth_segment'].value_counts()


# In[117]:


customer_demographic['deceased_indicator'].value_counts()


# In[118]:


customer_demographic['owns_car'].value_counts()


# # 4. Exploring Customer Address Dataset

# In[120]:


customer_add.head()


# In[121]:


customer_add.info()


# In[122]:


print("Rows: ", customer_add.shape[0])
print("Columns: ", customer_add.shape[1])


# In[123]:


customer_add.isna().values.any()


# In[124]:


customer_add.columns


# In[125]:


customer_add['state'] = customer_add['state'].replace('QLD','Queensland')
customer_add['state'] = customer_add['state'].replace('NSW','New South Wales')
customer_add['state'] = customer_add['state'].replace('VIC','Victoria')


# In[126]:


customer_add['state'].value_counts()


# In[127]:


customer_add['postcode'].value_counts()


# In[128]:


customer_add['country'].value_counts()


# In[129]:


customer_add['property_valuation'].value_counts()


# # Merging of all Customer datasets into one for analysis
# 

# All the dataset contains the customer id except NewCustomerList Dataset. So, We need to add 'Customer Id' column to new_customer_lists to enable us merge the tables vertically

# In[135]:


new_customer_lists.head()


# In[137]:


new_customer_lists.shape


# In[140]:


customer_demographic.shape


# In[143]:


customer_demographic['customer_id'].iloc[-1] #returns total number of rows of customer_id columns


# In[144]:


#  add 'Customer Id' column to new_customer_lists
new_customer_lists.insert(0, 'customer_id', range(4001, 4001 + len(new_customer_lists)))


# In[145]:


new_customer_lists.head()


# In[146]:


new_customer_lists.tail()


# #### We need to merge the Customer Demographic with the Customer Address table

# In[147]:


customer_add.head()


# In[151]:


customer_add.shape


# In[163]:


customer_demographic.head()


# In[152]:


customer_demographic.shape


# In[149]:


# Merge dataframes using the customer_id column
customer_demographic = pd.merge(customer_demographic, customer_add, how='left', on='customer_id')


# In[164]:


customer_demographic.tail()


# In[154]:


customer_demographic.drop('default',axis=1,inplace=True)


# In[165]:


customer_demographic.head()


# In[166]:


customer_demographic.info()


# In[171]:


customer_demographic['age-group'] = pd.cut(customer_demographic['age'], [0,30,40,50,60,200], labels = ['<30','30-40','40-50','50-60','60+'])


# In[172]:


customer_demographic.head()


# In[180]:


new_customer_lists.head()


# In[183]:


new_customer_lists["age_group"] = pd.cut(new_customer_lists.age, [0,30,40,50,60,9999], labels=['<30','30-40','40-50','50-60','60+'])


# In[184]:


new_customer_lists.head()


# In[185]:


new_customer_lists.info()


# In[186]:


customer_demographic.info()


# From the above information both dataframe have equal columns so 
# will merge both data sets: **new_customer_lists & customer_demographic**

# In[187]:


df = pd.concat([customer_demographic, new_customer_lists], ignore_index=True, sort=False)


# In[229]:


customer_demographic = df


# In[231]:


customer_demographic.head()


# #### Merge Transction dataframe with customer demographic dataframe to make a one single dataframe 

# In[198]:


transactions_customer = transactions


# In[199]:


transactions_customer.head()


# In[244]:


transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","gender"]], on="customer_id", how="left")


# In[245]:


transactions_customer.head()


# In[246]:


transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","past_3_years_bike_related_purchases"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","age"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","age_group"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","job_title"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","job_industry_category"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","wealth_segment"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","owns_car"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","postcode"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","state"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","property_valuation"]], on="customer_id", how="left")
transactions_customer = pd.merge(transactions_customer,customer_demographic[["customer_id","country"]], on="customer_id", how="left")


# In[247]:


transactions_customer.head()


# In[248]:


transactions_customer.sort_values(["transaction_date"], ascending=False)


# In[255]:


transactions_customer.head()

