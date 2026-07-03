from eda import load_data
from visualization import create_visualizations

# Load sample dataset
file = open("data/employees_dataset_200.csv", "rb")

df = load_data(file)

# Create charts
create_visualizations(df)

print("Charts created successfully!")
