import scipy.io as sio
import pandas as pd
mat = sio.loadmat("HippocampalSubfieldsMRI.mat")
#print(mat)
test= mat["final"]
#"final" foi o nome dado para o array no MatLab
subject=[i[ind] for ind,i in enumerate([x for x in test[0][0][1]]) if ind<58] 
# Subject é uma matriz com linhas que correspondem aos valores de um individuo em cada subcampo
# e com colunas correspondendo aos valores para diferentes individuos do mesmo subcampo. 
subfield_names= [x[0][0] for  x in test[0][0][0]]
df= pd.DataFrame(dict(zip(subfield_names,subject)))
df.to_csv("dataset1.csv",index=False)
