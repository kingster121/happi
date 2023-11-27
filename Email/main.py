import pandas as pd

# Given data
function_arguments = [
    {"date": "7th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
    {"date": "8th Dec 2023, 12pm", "summary": "Good food!"}
]

df = pd.DataFrame(function_arguments)

# Save the DataFrame to an Excel file
excel_filename = "output.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created.")