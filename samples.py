# scratchpad
=================
import pandas as pd
import json

# Load Excel file into a pandas DataFrame
df = pd.read_excel('file.xlsx')

# Load JSON schema into a pandas DataFrame
with open('schema.json') as json_file:
    schema = json.load(json_file)
    schema_df = pd.DataFrame(schema, columns=['l3', 'other_columns'])

# Merge the two DataFrames based on the l3 column with outer join
merged_df = pd.merge(df, schema_df, on='l3', how='outer')
====================================

import pandas as pd
import json

# Load Excel file into a pandas DataFrame
df = pd.read_excel('file.xlsx')

# Load JSON schema into a pandas DataFrame
with open('schema.json') as json_file:
    schema = json.load(json_file)
    schema_df = pd.DataFrame(schema, columns=['l3', 'other_columns'])

# Merge the two DataFrames based on the l3 column
merged_df = pd.merge(df, schema_df, on='l3')

========================================
import pandas as pd

# Load data into a pandas DataFrame
df = pd.read_excel('file.xlsx')

# Get rows with NaN values
rows_with_NaN = df[df.isna().any(axis=1)]
============merge two dataframes ===============
import pandas as pd

# Load the data into two DataFrames
df1 = pd.read_excel("df1.xlsx")
df2 = pd.read_excel("df2.xlsx")

# Merge the two DataFrames on a common column
df_merged = df1.merge(df2[['common_column_name', 'desired_column_name']], on='common_column_name', how='left')
# Sort the DataFrame by the date column in ascending order
df = df.sort_values(by='date_column', ascending=True)
