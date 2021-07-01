import boto3
import io
import pandas as pd
from pprint import pprint

bucket_name = 'data-eng-resources'

s3_client = boto3.client('s3')
bucket_list = s3_client.list_buckets()


# Retrieving fish data for Monday.

s3_fish_mon_obj = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-mon.csv',
)
data_frame_mon = pd.read_csv(s3_fish_mon_obj['Body'])


# Retrieving fish data for Tuesday.

s3_fish_tues_obj = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market-tues.csv',
)
data_frame_tues = pd.read_csv(s3_fish_tues_obj['Body'])


# Renaming the columns for both data sets.

data_frame_mon.rename(columns={'Weight': 'Weight Monday', 'Length1': 'Length1 Monday', 'Length2': 'Length2 Monday',
                               'Length3': 'Length3 Monday', 'Height': 'Height Monday', 'Width': 'Width Monday'},
                      inplace=True)

data_frame_tues.rename(columns={'Weight': 'Weight Tuesday', 'Length1': 'Length1 Tuesday', 'Length2': 'Length2 Tuesday',
                                'Length3': 'Length3 Tuesday', 'Height': 'Height Tuesday', 'Width': 'Width Tuesday'},
                       inplace=True)


# Grouping by species and retrieving the mean data for both data sets.

avg_fish_mon = data_frame_mon.groupby('Species').mean()
avg_fish_tues = data_frame_tues.groupby('Species').mean()


# Concatenating both dataset into a single data set.

fish_table = (pd.concat([avg_fish_mon, avg_fish_tues], axis=1))

cols = fish_table.columns.tolist()
cols.sort()
fish_combo = fish_table[cols]

print(fish_combo)


# Converting to CSV then pushing to AWS.

str_buffer = io.StringIO()
fish_table.to_csv(str_buffer)
s3_client.put_object(
    Bucket='data-eng-resources',
    Key='Data22/fish/mcosgrove.csv',
    Body=str_buffer.getvalue()
)


# Retrieving data from AWS.
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='Data22/fish/mcosgrove.csv'
)
pprint(s3_object["Body"])
fin_df = pd.read_csv(s3_object["Body"])
pprint(fish_combo)
