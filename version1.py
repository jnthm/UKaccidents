import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

acc_05_07 = pd.read_csv("../input/accidents_2005_to_2007.csv", index_col='Accident_Index')
acc_09_11 = pd.read_csv("../input/accidents_2009_to_2011.csv", index_col='Accident_Index')
acc_12_14 = pd.read_csv("../input/accidents_2012_to_2014.csv", index_col='Accident_Index')

acc_05_07.head()
acc_09_11.head()
acc_12_14.head()
print(acc_05_07.columns.equals(acc_09_11.columns)) # check if the columns are same in both data sets
print(acc_05_07.columns.equals(acc_12_14.columns))

acc_by_day = acc_05_07.groupby('Day_of_Week')['Year'].count()
print(acc_by_day)
plt.hist(acc_by_day)

acc_05_07['Day_of_Week'].unique()
acc_05_07['Day_of_Week'].value_counts()

plt.hist(acc_05_07.Day_of_Week)
type(acc_05_07.Day_of_Week)
acc_05_07.info()
acc_05_07.Day_of_Week.describe()

acc_05_07['Day_of_Week'] = acc_05_07['Day_of_Week'].astype('int')
acc_05_07.Day_of_Week.describe()
