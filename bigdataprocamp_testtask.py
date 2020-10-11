#!/usr/bin/env python
# coding: utf-8

import pandas as pd;
import numpy as np;
df = pd.read_csv(r"test-task_dataset_summer_products.csv");
df["origin_country"].replace({np.nan:''}, inplace=True);#preserving rows with  empty value in origin_country 
df=df.groupby('origin_country').agg({'price':'mean', 'rating_count':'sum','rating_five_count':'sum'});
print (df);




