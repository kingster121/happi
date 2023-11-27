import pandas as pd
from read_email import read_email

emails = read_email()

#--- For demo, can get weiren to forward 5 emails he want to see being summarised ---#
function_arguments = ray_function(read_email[:4])

# function_arguments = [
#     {"date": "7th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
#     {"date": "8th Dec 2023, 12pm", "summary": "Good food!"}
# ]


# Output to excel
df = pd.DataFrame(function_arguments)
excel_filename = "output.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created.")