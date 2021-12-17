#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import os
stock_prices = {}

for fn in os.listdir("prices"):
    #fn je naziv fajla
    name = fn.split(".")[0]
    stock_prices[name] = pd.read_csv(os.path.join("prices", fn))   


# In[6]:


stock_prices["aapl"].head()
#stock prices je dict
#gde su keys imena fajlova, tj stock symbols
# a values su df-ovi


# In[7]:


avg_closing_prices = {}

for stock_symbol in stock_prices:
    avg_closing_prices[stock_symbol] = stock_prices[stock_symbol]["close"].mean()


# In[9]:


for stock_symbol in stock_prices:
    print(stock_symbol, avg_closing_prices[stock_symbol])


# In[33]:


pairs = [(avg_closing_prices[stock_symbol], stock_symbol) for stock_symbol in stock_prices]
print(type(pairs))
pairs_sorted_2 = dict(sorted(avg_closing_prices.items(), key = lambda x: x[1], reverse=True))

first2pairs = {k: pairs_sorted_2[k] for k in list(pairs_sorted_2)[:2]}
print(first2pairs)
last2pairs = {k: pairs_sorted_2[k] for k in list(pairs_sorted_2)[-2:]}
print(last2pairs)
print('\n')

pairs.sort()
print("Two minimum average closing prices:")
print(pairs[0])
print(pairs[1])

print("Two maximum average closing prices:")
print(pairs[-1])
print(pairs[-2])


# In[26]:


maxi = max(avg_closing_prices, key = avg_closing_prices.get)
print(maxi)


# In[34]:


trades_by_day = {}
for stock_sym in stock_prices:
    for index, row in stock_prices[stock_sym].iterrows():
        day = row["date"]
        volume = row["volume"]
        pair = (volume, stock_sym)
        #samo napravi praznu listu [] za taj dan pa onda ubaci par!
        if day not in trades_by_day:
            trades_by_day[day] = []
        trades_by_day[day].append(pair)
#trades by day je dict gde sy keys datumi a values liste sa parovima volume, stock_symbol


# In[40]:


#print(trades_by_day["2007-01-04"])


# In[38]:


most_traded_by_day = {}

for day in trades_by_day:
    #tardes_by_day[day] je list, tako da moze da se sortira, po vrednosti
    #sortira se asc, tako da uzimam poslednji par kao najvecu vrednost
    trades_by_day[day].sort()
    most_traded_by_day[day] = trades_by_day[day][-1]
    
print(most_traded_by_day['2007-01-03'])
print(most_traded_by_day['2007-01-04'])
print(most_traded_by_day['2007-01-05'])
print(most_traded_by_day['2007-01-08'])


# In[43]:


daily_volumes = []

for day in trades_by_day:
    day_volume = sum([vol for vol, _ in trades_by_day[day]])
    daily_volumes.append((day_volume, day))

daily_volumes.sort()
daily_volumes[-10:]


# In[46]:


percentages = []

for stock_sym in stock_prices:
    prices = stock_prices[stock_sym]
    initial = prices.loc[0, "close"]
    #loc ne podrzava negativne indexe kao slices, mora preko ukupnog br redova
    final = prices.loc[prices.shape[0]-1, "close"]
    perc = ((final - initial)/initial)*100
    percentages.append((perc, stock_sym))
    
percentages.sort()

percentages[-10:]


# In[ ]:




