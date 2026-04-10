import pandas as pd
import glob
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
folder_path = os.path.join(base_dir, "data", "listed")

csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

if not csv_files:
    raise ValueError(f"No CSV files found in {folder_path}")

master_df = pd.concat([pd.read_csv(f) for f in csv_files], ignore_index=True)


output_path = os.path.join(base_dir, "crmls_listed_final"
".csv")
master_df.to_csv(output_path, index=False)

print(f"Saved combined CSV to: {output_path}")
