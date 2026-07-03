from report import generate_report

summary = """
Rows: 100
Columns: 8
Missing Values: 0
Duplicate Rows: 2
"""

insights = """
Dataset Overview:
The dataset contains employee records.

Business Recommendation:
Increase salary analysis.
"""

file = generate_report(summary, insights)

print(file)
