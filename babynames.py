#get the data from https://www.ssa.gov/oact/babynames/limits.html national file and choose a year

from time import process_time_ns
from matplotlib.pyplot import axes, legend, title, xticks, yticks
import pandas as pd
from pymongo import ASCENDING

names2007 = pd.read_csv("names/yob2007.txt", names=["names", "sex", "births"])
#you have the file in data columns that gives the baby name given, baby's sex, and number of times the name is given

namesex = names2007.groupby("sex").births.sum()
#you have the number of births for the given sex

#now take all the years into the bubble
years = range(1880,2021)
pieces= []
columns = ["name", "sex", "births"]
for year in years:
    path = "names/yob%d.txt" % year
    frame = pd.read_csv(path, names = columns)

    frame["year"] = year
    pieces.append(frame)

    names= pd.concat(pieces, ignore_index=True)



total_births = names.pivot_table("births", index= "year",  columns="sex",aggfunc=sum)
#you have the last 5 years grouped for births and sex

total_births.plot(title="Total births by sex and year")

def add_prop(group):
    births = group.births.astype(float)

    group["prop"] = births / births.sum()
    return group

names = names.groupby(["year","sex"]).apply(add_prop)

#check
import numpy as np
np.allclose(names.groupby(['year','sex']).prop.sum(), 1)



def get_top1000(group):
    return group.sort_values(by="births", ascending=False)[:1000]

grouped = names.groupby(["year", "sex"])
top1000 = grouped.apply(get_top1000)
top1000 = top1000.append(top1000, ignore_index=True)
boys = top1000[top1000.sex== "M"]
girls = top1000[top1000.sex== "F"]

total_births = top1000.pivot_table("births", index="year", columns="name",aggfunc=sum)
subset = total_births[["John","Mary","Harry", "Marilyn"]]

table = top1000.pivot_table("prop", index = "year", columns="sex", aggfunc=sum)
table.plot(title="Sum of table1000.prop by year and sex", yticks = np.linspace(0,1.2,13), xticks = range(1880,2020,10))

df = boys[boys.year ==2010]
prop_cumsum = df.sort_values(by = "prop", ascending=False).prop.cumsum()
# print(prop_cumsum)

df = boys[boys.year ==1900]
in1900 = df.sort_values(by = "prop", ascending=False).prop.cumsum()
# print(in1900.searchsorted(0.5)+1)

def get_quantile_count(group, q=0.5):
    group = group.sort_values(by="prop", ascending=False)
    return group.prop.cumsum().searchsorted(q)+1

diversity = top1000.groupby(["year","sex"]).apply(get_quantile_count)
diversity = diversity.unstack("sex")
# print(diversity.head())
diversity.plot(title="number of popular names in 50%")
#gives the change of name diversity plot




#shows the last letter change by year
get_last_letter = lambda x:x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = "last_letter"

table = names.pivot_table("births",index=last_letters, columns=["sex","year"], aggfunc=sum)

subtable = table.reindex(columns=[1910,1960,2020], level="year")
# print(subtable.sum())

letter_prop = subtable / subtable.sum().astype(float)

import matplotlib.pyplot as plt
fig, axes = plt.subplots(2,1,figsize=(10,8))
letter_prop["M"].plot(kind="bar",rot=0,ax=axes[0], title="Male")
letter_prop["F"].plot(kind="bar",rot=0,ax=axes[1], title="Female", legend=False)

