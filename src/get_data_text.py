import pandas as pd

# path + input filename
filename = './data/BIOGRID_human.txt'
# filename = './9606_protein.txt'
df = pd.read_csv(filename, delimiter = "\t")

print(df.columns.values) # print column name
print(df.head())        # print first few rows

# renaming the protein
# df['protein1'] = df['protein1'].apply(lambda x: x.replace('0000000',""))    
# df['protein1'] = df['protein1'].apply(lambda x: x[5:])
# df['protein2'] = df['protein2'].apply(lambda x: x[5:])

# print(df.head()) # print first few rows