import pandas as pd
import glob
import os

# Get base directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Path to "sold" CSV files
folder_path = os.path.join(base_dir, "data", "sold")

# Get all CSV files
csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

# Check if files exist
if not csv_files:
    raise ValueError(f"No CSV files found in {folder_path}")

# Read and combine all CSVs (safe dtype handling)
master_df = pd.concat(
    [pd.read_csv(f, dtype=str, low_memory=False) for f in csv_files],
    ignore_index=True
)

# Output file path
output_path = os.path.join(base_dir, "crmls_sold_final.csv")

# Save combined CSV
master_df.to_csv(output_path, index=False)

print(f"Saved combined CSV to: {output_path}")
