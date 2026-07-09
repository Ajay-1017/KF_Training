

import pandas as pd
import os

base_dir = os.path.dirname(__file__)
source = os.path.join(base_dir,"source_data")

df = pd.read_csv(os.path.join(source,"orders.csv"))



