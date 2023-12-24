from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '6929876322:AAGrtdUZ6g9hvuj4rbBAKUPThBgpZB_EPAA'
BOT_USERNAME = '@sstarter_bot'

### --- Test Data --- ###
email_outputs = [
    {"date": "7th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
    {"date": "8th Dec 2023, 12pm", "summary": "Good food!"},
    {"date": "9th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
    {"date": "10th Dec 2023, 12pm", "summary": "Good food!"},
    {"date": "11th Dec 2023, 10am", "summary": "AI Research Seminar (AIRS) Series"},
    {"date": "12th Dec 2023, 12pm", "summary": "Good food!"}
]

### --- Commands --- ###
async def retrieve_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sets it to retrieve the last 5 emails summary"""
    text = ""
    for index in range(5):
        date = email_outputs[index]["date"]
        summary = email_outputs[index]["summary"]
        text += f"{date}: {summary}\n"

    print(text)
    await update.message.reply_text(text)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for chatting with me! Bare with me as I am still learning!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Type something so that I can respond!")


# Responses
def handle_response(text: str) -> str:
    processed = text.lower()

    if "hello" in processed:
        return "Hey there!"
    
    if "how are you" in processed:
        return "I am good!"
    
    if "i love python" in processed:
        return "Remember to subscribe!"
    
    return "I don't understand you!"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text

    print(f"User ({update.message.chat.id} in {message_type}: {text})")

    if message_type == "group":
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, "").strip()
            response =handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print(f"Bot: {response}")
    await update.message.reply_text(response)

async def errors(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")
    

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("retrieve", retrieve_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(errors)

    # Polling (How often to check for new messages)
    print("Polling...")
    app.run_polling(poll_interval=3)