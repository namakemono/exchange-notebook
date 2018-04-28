#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import glob
import pandas as pd

"""
ダウンロードした為替データをOHLC形式に変換し，"../input/exchange.csv"に保存

```
rate_date_time  rate_bid_open  rate_bid_high  rate_bid_low  \
0    2018-04-15 17:00:00        107.467        107.467       107.467   
1    2018-04-15 17:01:00        107.468        107.468       107.463   
2    2018-04-15 17:02:00        107.480        107.480       107.435   
3    2018-04-15 17:03:00        107.435        107.440       107.435   
4    2018-04-15 17:04:00        107.441        107.475       107.441   
5    2018-04-15 17:05:00        107.444        107.462       107.435   
```

"""

def to_snake(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def convert(fpath):
    print("Converting to OHLC format: %s" % fpath)
    df = pd.read_csv(fpath, parse_dates=["RateDateTime"])
    df = df.set_index("RateDateTime", drop=True)[["RateBid", "RateAsk"]].resample("1min").ohlc()
    df.columns = df.columns.map("_".join)
    df = df.reset_index()
    df.columns = df.columns.map(to_snake)
    return df

def run():
    fpath_list = sorted(glob.glob("../download/*/*/*.zip"))
    df = pd.concat(map(convert, fpath_list))
    df.to_csv("../input/exchange.csv", index=False)
    print(df.head())
    
if __name__ == "__main__":
    run()
