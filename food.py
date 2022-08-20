#this project aims to analyze usda food database json file created by Ashley Williams,
#and extracted from the link: https://github.com/CJOlsen/perfect-meal-win , 
#following Wes Mckinney's guide on Python for Data Analysis

from pandas import DataFrame
import pandas as pd
import json
import matplotlib.pyplot as plt

db = (json.load(open("foods-2011-10-03.json")))
# print(db[0].keys())
#created database


info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns= info_keys)
#organized database

# pd.value_counts(info.key)[:10]
# print(pd.value_counts(info.group)[:10])


nutrients = []

for rec in db:
    fnuts = DataFrame(rec["nutrients"])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

#created a series for nutrients

nutrients = pd.concat(nutrients,ignore_index=True)
nutrients.duplicated().sum()
nutrients = nutrients.drop_duplicates()
# print(nutrients)
# organized nutrients series

col_mapping = {"description":"food",
                "group":"fgroup"}

info = info.rename(columns=col_mapping, copy=False)
#column names changed

col_mapping = {"description":"nutrient",
                "group":"nutgroup"}

nutrient = nutrients.rename(columns=col_mapping, copy=False)
#column names changed


ndata = pd.merge(nutrients,info, on='id', how='outer')
# print(ndata.iloc[30000])
#series and database merged

result = ndata.groupby(['description', 'fgroup'])['value'].quantile(0.5)

result['Zinc, Zn'].sort_values().plot(kind='barh')
# plt.show()
by_nutrient = ndata.groupby(['group', 'description'])

get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())

max_foods = by_nutrient.apply(get_maximum)[['value','food']]

max_foods.food = max_foods.food.str[:50]

max_foods.loc['Amino Acids']['food']

#several ways to investigate the database can get more according to what is wished to be examined