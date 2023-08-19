#!/usr/bin/env python
# coding: utf-8

# In[87]:


import pandas as pd
import requests
from bs4 import BeautifulSoup

brand_list = []

def scrape_brands():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    url = "https://olefloridaflyshop.com/shop-by-brand/"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        brand_names = soup.find_all("div", class_="vc_column-inner")
        
        for names in brand_names:
            brand_name_element = names.find("li", class_="brand-list-brand")
            
            if brand_name_element is not None:
                brand_name = brand_name_element.text
                brand_list.append(brand_name)
            else:
                print("Brand not found")
    
    else:
        print("Failed to retrieve the page:", response.status_code)
    
    return brand_list

# Scrape brand names
brands = scrape_brands()

# Scrape products for each brand
def scrape_products_for_brands(brand_list, num_pages):
    all_dataframes = []
    
    for brand in brand_list:
        base_url = f"https://olefloridaflyshop.com/brand/{brand}/page/"
        result_df = scrape_products(base_url, num_pages)
        result_df["Brand"] = brand  # Add a "Brand" column to the DataFrame
        all_dataframes.append(result_df)
    
    # Concatenate all DataFrames into a single DataFrame
    combined_df = pd.concat(all_dataframes, ignore_index=True)
    
    return combined_df

# Number of pages to scrape for each brand
num_pages = 3

# Scrape products for each brand and store in a DataFrame
combined_dataframe = scrape_products_for_brands(brands, num_pages)

# Print the combined DataFrame
print(combined_dataframe)


# In[90]:


combined_dataframe


# In[96]:


combined_dataframe.to_excel('ole_florida_scrape.xlsx', index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




