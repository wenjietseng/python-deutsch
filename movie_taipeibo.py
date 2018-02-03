# Scrap data from taipeibo movie website
#

import re
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


# get html data
yrs = [2016, 2017, 2018]
target_url = ["http://www.taipeibo.com/year/" + str(year) for year in (yrs)]
# print(target_url) 
responses = [requests.get(url) for url in target_url]

all_rows = [] #空的list
for html in responses:
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, "lxml")
    all_rows.append(soup.find_all("tr"))

# what are the data look like in all_rows?
# print(len(all_rows[0]) + len(all_rows[1]) + len(all_rows[2]))
# first row is header
column_name_tag = all_rows[0][0]
# use stripped_strings to extract the value
print([text for text in column_name_tag.stripped_strings])
column_name = [text for text in column_name_tag.stripped_strings]

all_rows = all_rows[0][1:] + all_rows[1][1:] + all_rows[2][1:]

# use pandas to build DataFrame
movie_df = pd.DataFrame(columns = column_name)
movie_df

for index, row in enumerate(all_rows):
    data_want = [line for line in row.stripped_strings]
    print(data_want) # for debug
    movie_df.loc[index] = data_want

# print(movie_df.head())

#funcion(var)
#var.function

# add a column to specify which year
which_year = np.repeat(yrs, [100, 100, 47], axis=0)
# print(movie_df.shape)
# print(len(which_year))
movie_df['which_year'] = which_year
print(movie_df.head())
movie_df.to_csv("csv_results/movie_16-18.csv", index=False, encoding="utf-8")

# you can combine two DataFrame by DataFrame.append
# DF = df1.append(df2)
