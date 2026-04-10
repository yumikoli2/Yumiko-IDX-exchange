import pandas as pd
import glob

files = glob.glob("data/sold/*.csv")

df = pd.concat(
    [pd.read_csv(f, low_memory=False) for f in files],
    ignore_index=True
)

df.to_csv("crmls_sold_final.csv", index=False)
