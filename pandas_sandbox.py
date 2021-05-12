import pandas as pd
import numpy as np

# create a df using lists
# df2 = pd.DataFrame([
#   [1, 'San Diego', 100],
#   [2, 'Los Angeles', 120],
#   [3, 'San Francisco', 90],
#   [4, 'Sacramento', 115]
# 	],
#   columns=['Store ID', 'Location', 'Number of Employees'])
#
# print(df2)
#
# df3 = pd.read_csv('sample.csv')
# df3.to_csv('new_csv.csv')  # I think this will push to a csv file
#
# print(df3.head())
# print(df3.info())
#
# locations = df2.Location  # Returns a Series (column) from dataframe df2
# locations = df2['Location']  # These are equivalent as long as column name conforms to variable rules

# test of importing csv into dataframe.
train_data = pd.read_csv('train_data_sample.csv')
#print(train_data.info())
#print(train_data.head())
points_committed = train_data['pts_committed']
#print(points_committed)
train1_R416 = train_data[(train_data.train_id == 1) & (train_data.release == 'R416')]
#print(train1_R416)
r316_r416 = train_data[train_data.release.isin(['R316', 'R416'])]
#print(r316_r416.head())

top_accepted = train_data.groupby('release').pts_accepted.apply(lambda pts: np.percentile(pts, 75)).reset_index()
#print(top_accepted)

#testing pivot table addressing
train_data_subset = train_data[['train_id', 'release', 'pts_committed']]
train_data_pivot = train_data_subset.pivot(columns='release',
                                            index='train_id',
                                            values='pts_committed').reset_index()
print(train_data_pivot)
test_series = train_data_pivot.R416
print(test_series)
print(train_data_pivot.info())
