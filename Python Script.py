### Importing Necessary modules

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#### Loading the fiile

df = pd.read_csv(r'C:\Users\Chandrashekar\Desktop\Resume Projects\Python Projects\Input\netflix1.csv')

### checking the missing values and duplicates

print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())

#### Relacing the date formate

df['formatted_date'] = df['date_added'].replace('/', '-', regex = True)
print(df.head(10))

#### converting to date and time formate

df['formatted_date'] = pd.to_datetime(df['formatted_date'])
print(df.head(10))

df['year'] = df['formatted_date'].dt.year

df['After_2020'] = df['year'] >= 2020
print(df['After_2020'])

res = df['After_2020'].sum()
print(res)

res1 = pd.set_option('display.max_columns', None)
print(df.head())


### grouping the data (Movie and Tv shows) based on title column adding release_year column and performed count.

noofmovies = df.groupby('type')['release_year'].count()
print(noofmovies)


Movies_after_2020 = df[(df['release_year'] > 2020 ) & (df['type'].str.contains('Movie'))].count()
print(Movies_after_2020)


##### Count occurrences of 'Movies' and 'TV Show'

count_movies = df['type'].str.contains('Movie').sum()
count_tv_shows = df['type'].str.contains('TV Show').sum()
print(count_movies, count_tv_shows)

### # Create a dictionary to hold counts

counts = {'Movies': count_movies, 'TV Shows': count_tv_shows}


#### creating visualiztion

plt.figure(figsize=(8, 5))
plt.bar(counts.keys(), counts.values(), color=['blue', 'orange'])

##### Add labels and title

plt.xlabel('Type')
plt.ylabel('Count')
plt.title('Count of Movies and TV Shows')

print(plt.show())


# Saving the data in csv formate

finaldata = df.to_csv(r'C:\Users\Chandrashekar\Desktop\Resume Projects\Python Projects/finaldata.csv', index=False)
print('Final Data Saved successfully:')
