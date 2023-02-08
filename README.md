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
