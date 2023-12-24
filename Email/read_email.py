from simplegmail import Gmail
import json


def read_email():
    gmail = Gmail()

    mails = gmail.get_messages() # Get those in normal inbox
    mails.extend(gmail.get_spam_messages())

    message_list = []
    for mail in mails:
        message_dict = {
            "To: ": mail.recipient,
            "From: ": mail.sender,
            "Subject: ": mail.subject,
            "Date: ": mail.date,
            "Preview: ": mail.snippet,
            "Message Body: ": mail.plain
        }
        message_list.append(message_dict)

    # Specify the file path
    file_path = 'output.json'

    return message_list

if __name__ == "__main__":
    message_list = read_email()
    print(message_list)