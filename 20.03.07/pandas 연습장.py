%matplotlib inline
import pandas as pd
df = pd.read_csv('data/world_indexes.csv')
print(df.plot(kind='scatter', x='Life expectancy at birth- years', y='Internet users percentage of population 2014'))
print(df.plot(kind='scatter', x='Life expectancy at birth- years', y='Forest area percentage of total land area 2012'))
print(df.plot(kind='scatter', x='Life expectancy at birth- years', y='Carbon dioxide emissionsAverage annual growth'))
print(df.plot(kind='scatter', x='Internet users percentage of population 2014', y='Forest area percentage of total land area 2012'))
print(df.plot(kind='scatter', x='Internet users percentage of population 2014', y='Carbon dioxide emissionsAverage annual growth'))
print(df.plot(kind='scatter', x='Forest area percentage of total land area 2012', y='Carbon dioxide emissionsAverage annual growth'))
