import pandas as pd
from read_email import read_email
from inboxslave import gpt_prompt
import os
from dotenv import load_dotenv
from openai import OpenAI
import json



load_dotenv()
api_key= os.getenv("OPENAI_APIKEY")
client = OpenAI(api_key=api_key)


emails = read_email()

#--- For demo, can get weiren to forward 5 emails he want to see being summarised ---#
email_outputs = gpt_prompt(emails[:5])

# email_outputs = [
#     {"date": "7th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
#     {"date": "8th Dec 2023, 12pm", "summary": "Good food!"}
# ]


# Output to excel
data = [json.loads(s) for s in email_outputs]
df = pd.DataFrame(data)
excel_filename = "output.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Excel file '{excel_filename}' has been created.")