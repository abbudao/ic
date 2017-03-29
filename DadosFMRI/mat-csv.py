import scipy.io as sio
import pandas as pd
mat = sio.loadmat("HippocampalSubfieldsMRI.mat")
la =sio.whosmat("HippocampalSubfieldsMRI.mat")
#print(la)
test= mat['final']
#print(test)
#print(len(test[0][0][0]))
subject=[i[ind] for ind,i in enumerate([x for x in test[0][0][1]]) if ind<58] 
# Subject é uma matriz com linhas que correspondem aos valores de um individuo em cada subcampo,
# as colunas dessa matriz, correspondem aos valores para diferentes individuos do mesmo subcampo. 
#print(len(subject))
#print(subject)
subfield_names= [x[0][0] for  x in test[0][0][0]]
#print(subfield_names)
df= pd.DataFrame(dict(zip(subfield_names,subject)))
print(df)
#mat = {k:v for k, v in mat.items() if k[0] != '_'}
#print(mat)
# data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.iteritems()})
# data.to_csv("example.csv")
