#this project analyses 2012 US Federal Election Commission Database following 
#Wes Mckinney's Python for Data Analysis
#database can be found at https://github.com/wesm/pydata-book/tree/3rd-edition/datasets/fec

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fec = pd.read_csv('P00000001-ALL.csv', low_memory=False)
# print(fec.iloc[123])

unique_cands = fec.cand_nm.unique()
# print(unique_cands)
#get the names of the candidates

parties = {'Bachmann, Michelle':'Republican',
            'Romney, Mitt':'Republican',
            'Obama, Barack':'Democrat',
            "Roemer, Charles E. 'Buddy' III":'Republican',
            'Pawlenty, Timothy':'Republican',
            'Johnson, Gary Earl':'Republican',
            'Paul, Ron':'Republican', 
            'Santorum, Rick':'Republican',
            'Cain, Herman':'Republican',
            'Gingrich, Newt':'Republican',
            'McCotter, Thaddeus G':'Republican',
            'Huntsman, Jon':'Republican',
            'Perry, Rick': 'Republican'}

fec['party']=fec.cand_nm.map(parties)  
#add parties to the db

fec['party'].value_counts()

fec = fec[(fec.contb_receipt_amt>0)]
#filters out 0 contribution

fec_mrbo = fec[fec.cand_nm.isin(['Obama, Barack', 'Romney, Mitt'])] #main candidates

contributors_analysis = fec.contbr_occupation.value_counts()[:10] #most contributing occupations

occ_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
    'INFORMATION REQUESTED' : 'NOT PROVIDED',
    'INFORMATION REQUESTED (BEST EFFORTS)' : 'NOT PROVIDED',
    'C.E.O.' : 'CEO'
}

f= lambda x: occ_mapping.get(x,x)
fec.contbr_occupation = fec.contbr_occupation.map(f)


emp_mapping = {
    'INFORMATION REQUESTED PER BEST EFFORTS' : 'NOT PROVIDED',
    'INFORMATION REQUESTED' : 'NOT PROVIDED',
    'SELF' : 'SELF-EMPLOYED',
    'SELF-EMPLOYED' : 'SELF-EMPLOYED'
}
f= lambda x: emp_mapping.get(x,x)
fec.contbr_employer = fec.contbr_employer.map(f)

by_occupation = fec.pivot_table('contb_receipt_amt', index = 'contbr_occupation', columns = 'party', aggfunc='sum')
#makes a table for occupations and contribution amount


over_2m = by_occupation[by_occupation.sum(1)>2000000]
over_2m.plot(kind='barh')
# plt.show()
#bar graph for contribution by occupation over 2m 

def get_top_amounts(group,key, n=5):
    totals=group.groupby(key)['contb_receipt_amt'].sum()

    return totals.sort_values(ascending = False)[:n]

grouped = fec_mrbo.groupby('cand_nm')

grouped.apply(get_top_amounts,'contbr_occupation',n=7)
grouped.apply(get_top_amounts,'contbr_employer',n=10)
#top contributions

bins = np.array([0,1,10,100,1000,10000,100000,1000000,10000000])

labels = pd.cut(fec_mrbo.contb_receipt_amt,bins)
# print(labels)

grouped = fec_mrbo.groupby(['cand_nm',labels])
grouped.size().unstack()
#groups contributions for intervals

bucket_sums = grouped.contb_receipt_amt.sum().unstack(0)
#total amount made in the intervals
normed_sums = bucket_sums.div(bucket_sums.sum(axis=1),axis= 0 )
#percentage in the intervals

grouped = fec_mrbo.groupby(['cand_nm','contbr_st'])
totals = grouped.contb_receipt_amt.sum().unstack(0).fillna(0)
totals = totals[totals.sum(1)>100000]
percent = totals.div(totals.sum(1), axis = 0)
#contribution by states
