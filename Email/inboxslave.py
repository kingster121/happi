import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

api_key= os.getenv("OPENAI_APIKEY")
client = OpenAI(api_key=api_key)



# function_arguments = {
#   "date": "7th Dec 2023, 10am",
#   "summary": "AI Research Seminar (AIRS) Series"
# }


#--- Created function to allow multiple emails to be parsed ---#
def gpt_prompt(emails):

    extract_function = [
    {
        "name": "extract_info",
        "description": "extract parameters and summarise content",
        "parameters": {
            "type":"object",
            "properties":{
                "date":{
                    "type":"string",
                    "description": "date and time of the event happening",},
                "summary":{
                    "type":"string",
                    "description": "10 word max summary of what the event is",
                },
                "venue":{
                    "type":"string",
                    "description": "retrieve the venue if any. else return NA",
                }

            },
            "required": ["date","summary","venue"]
        }
    }
                    ]
    

    email_outputs = []


    for email in emails:
        prompt = f"please extract the important information from this email{email}"
        messages = [{"role":"user","content":prompt}]

        response = client.chat.completions.create(
            model = "gpt-3.5-turbo-0613",
            messages=messages,
            functions=extract_function,
            function_call="auto"
        )

        ##extracting json output of function call👇
        choices = response.choices

        # Assuming there's at least one choice and it contains a function call
        if choices and choices[0].message and choices[0].message.function_call:
            function_call = choices[0].message.function_call

            # Now you have the FunctionCall object
            function_name = function_call.name
            function_arguments = function_call.arguments
            print(function_arguments)

            email_outputs.append(function_arguments)
    print(email_outputs)
    return email_outputs

            