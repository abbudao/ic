import pandas as pd
import numpy as np

n_state=5
alpha=0.9
set_size=19
nodes_to_use=[1,2,3,7,38]

df=pd.read_csv("dataset1.csv")
iter= df.itertuples()
ddf=[]

#Separating data from selected nodes in 5 bins
for i in range(len(df)):
    a=next(iter)
    temp=[a[node] for node in nodes_to_use]
    ddf.append(pd.qcut(temp,n_state))
print(ddf)
#
for i in range(len(df)):
    ind=np.roll(np.arange(1,len(df)),(-(i-1)))
    tomerge= ddf[:,:,ismember()]
