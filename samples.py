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
==============================================
# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Access data for each column by column name
    print('Column1:', row['Column1'], 'Column2:', row['Column2'])
====================================================
import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3, 4], 'Column2': ['A', 'B', 'C', 'D']})

# Select the 'Column1' column
column1 = df['Column1']

# Convert the column to a list
column1_list = column1.tolist()

print(column1_list)
============= merege df and dict ================
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value_1': [1, 2, 3, 4]})

# Create the dictionary
d = {'key': 'B', 'value_2': 10}

# Convert the dictionary to a dataframe
d = pd.DataFrame(d, index=[0])

# Merge the two dataframes based on the 'key' column
df = pd.merge(df, d, on='key', how='left')

print(df)
=============================================
for index, row in df.iterrows():
    r = requests.get(row['ListOfURLs'])
    if r.status_code == 200:
        df.at[index, ['Status Code', 'Result', 'Error']] = (r.status_code, '[OK]', np.nan)

print(df)
================================================
def get_algo_mcs(self):
    df_algo_names = df_algo_names[df_algo_names['Algo Name'].apply(lambda x: isinstance(x, str))]
    df_algo_names = df_algo_names[df_algo_names['Algo Name'].apply(lambda x: len(x) >= 5)]

    for index, row in df_algo_names.iterrows():
        algo = row['Algo Name']
        algoid, status = self._search(algo)
        if algoid != "ERR":
            df_algo_names.at[index, 'mode'] = "modelunumer"
====================================================            
lgEnt = [lg.get("code") for lg in md_data["info"]["legalENT"] if lg.get("code") is not None]
isEASY = 'Y' if 'EASY' in lgEnt else 'N'
===============================================
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}
print(even_dict)
# Output: {'b': 2, 'd': 4}
=================compare DFs==============================
import pandas as pd

df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']
})

df2 = pd.DataFrame({
    'A': ['A2', 'A3', 'A4', 'A5'],
    'B': ['B2', 'B3', 'B4', 'B5'],
    'C': ['C2', 'C3', 'C4', 'C5'],
    'D': ['D2', 'D3', 'D4', 'D5']
})

merged_left = df1.merge(df2, on=['A', 'B'], how='left')
merged_right = df1.merge(df2, on=['A', 'B'], how='right')
merged_outer = df1.merge(df2, on=['A', 'B'], how='outer')
=================================html=================================
<html>
<head>
  <title>My HTML Page</title>
  <script>
    function sayHello() {
      alert("Hello, World!");
    }
  </script>
</head>
<body>
  <h1>Hello, World!</h1>
  <p>This is a simple HTML page.</p>
  <button onclick="sayHello()">Click Me</button>
</body>
</html>

==========
<script>
  function filterTable(event) {
    var filter = event.target.value.toUpperCase();
    var rows = document.querySelector("#myTable tbody").rows;
    for (var i = 0; i < rows.length; i++) {
      var firstCol = rows[i].cells[0].textContent.toUpperCase();
      var secondCol = rows[i].cells[1].textContent.toUpperCase();
      var thirdCol = rows[i].cells[2].textContent.toUpperCase();
      // Repeat for all 15 columns
      if (firstCol.indexOf(filter) > -1 || secondCol.indexOf(filter) > -1 || thirdCol.indexOf(filter) > -1) {
        rows[i].style.display = "";
      } else {
        rows[i].style.display = "none";
      }
    }
  }
  document.querySelector('#myInput').addEventListener('input', filterTable);
</script>

<input type="text" id="myInput" placeholder="Search for names..">
