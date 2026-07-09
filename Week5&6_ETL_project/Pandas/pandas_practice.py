import pandas as pd
import os

base_dir = os.path.dirname(__file__)

# Load the dataframe of csv file
df = pd.read_csv(os.path.join(base_dir,'orders.csv')) 
print(df)