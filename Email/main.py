import pandas as pd
from read_email import read_email
from inboxslave import gpt_prompt

emails = read_email()

#--- For demo, can get weiren to forward 5 emails he want to see being summarised ---#
email_outputs = gpt_prompt(read_email[:4])

# email_outputs = [
#     {"date": "7th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
#     {"date": "8th Dec 2023, 12pm", "summary": "Good food!"}
# ]


# Output to excel
df = pd.DataFrame(email_outputs)
excel_filename = "output.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created.")