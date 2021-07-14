import pandas as pd
import numpy as np
dict1={'Success':[]}
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
"labels" :['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']}
# All the dataframe
dataframe = pd.DataFrame(exam_data)
dataframe=dataframe.set_index("labels")
#Print the 3 first row
print("The 3 first rows","\n",dataframe.head(3))
#Delete rows with Nan values
dataframe=dataframe.dropna()
print("Dataframe without the nan Values","\n",dataframe)
#Extract the name and score columns
df1=dataframe[['name','score']]
print("Score and names extracted from the dataframe","\n",df1)
#Add the row with Suresh
dataframe.loc['k'] = ["Suresh", 15.5, '1',"yes"]
print("Add a new row k","\n",dataframe)

#Delete the column attempts
dataframe=dataframe.drop("attempts",axis=1)
print("DataFrame without the column attempts","\n",dataframe)
#Add the success column
for i in dataframe.itertuples():
    if i[2]>=10:
        dict1['Success'].append(1)
    else:
         dict1['Success'].append(0)
dataframe['success']=dict1['Success']
print(dataframe)
#Export to to_csv
dataframe.to_csv("Data.csv")
