import matplotlib.pyplot as plt
import pandas as pd
import sys

names = ["Pedro","Carolina","Helena","Marina","Mario"]
births= [500,112,313,123,1000]
BabyDataset= list(zip(names,births))
df = pd.DataFrame(data=BabyDataset, columns=["Names","Births"])
print(df)
df.to_csv("births.csv",index=False,header=False)
Location= r"births.csv"
df2= pd.read_csv(Location,header=None)
print(df2)
print(df.Births.dtypes)
Sorted= df.sort_values(["Births"],ascending=False)
print(Sorted.head(1))
# Create graph
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print("The most popular name")
df[df['Births'] == df['Births'].max()]
#Sorted.head(1) can also be used

