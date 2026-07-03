from gemini_ai import generate_insights

summary = """
Rows: 5

Columns: 4

Column Names:
Name, Age, Department, Salary

Missing Values:
0

Duplicate Rows:
0

Average Salary:
55000
"""

result = generate_insights(summary)

print(result)
